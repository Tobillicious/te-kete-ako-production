"""
Curriculum Uploader - Upload validated statements to Supabase
"""

import json
import os
import logging
from typing import List, Dict
from pathlib import Path
from tqdm import tqdm
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CurriculumUploader:
    """Uploads curriculum statements to Supabase"""
    
    def __init__(self):
        # Initialize Supabase client
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_SERVICE_KEY')
        
        if not supabase_url or not supabase_key:
            raise ValueError(
                "Missing Supabase credentials. Set SUPABASE_URL and SUPABASE_SERVICE_KEY in .env file"
            )
        
        self.client: Client = create_client(supabase_url, supabase_key)
        logger.info("✓ Connected to Supabase")
        
        self.stats = {
            'total_processed': 0,
            'inserted': 0,
            'skipped_duplicates': 0,
            'errors': 0
        }
    
    def check_duplicate(self, statement: Dict) -> bool:
        """Check if statement already exists in database"""
        try:
            result = self.client.table('curriculum_statements').select('id').eq(
                'curriculum_version', statement['curriculum_version']
            ).eq(
                'learning_area', statement['learning_area']
            ).eq(
                'statement_text', statement['statement_text']
            ).limit(1).execute()
            
            return len(result.data) > 0
        except Exception as e:
            logger.warning(f"Error checking duplicate: {e}")
            return False
    
    def prepare_statement_for_db(self, statement: Dict) -> Dict:
        """Convert scraped statement to database format"""
        # Map scraped format to database schema
        db_statement = {
            'curriculum_version': statement['curriculum_version'],
            'version_status': self._get_version_status(statement['curriculum_version']),
            'learning_area': statement['learning_area'],
            'statement_text': statement['statement_text'],
            'phase': statement.get('phase'),
            'level': statement.get('level'),
            'strand': statement.get('strand'),
            'sub_strand': statement.get('sub_strand'),
            'element': statement.get('element'),
            'context': statement.get('context'),
            'examples': statement.get('examples', []),
            'year_levels': statement.get('year_levels', []),
            'tahurangi_url': statement.get('tahurangi_url'),
            'section_id': statement.get('section_id'),
            'quality_score': 100,  # Verbatim from MoE = perfect quality
        }
        
        # Add effective date based on version
        if statement['curriculum_version'] == 'temataiaho_2025':
            db_statement['effective_date'] = '2025-01-01'
        elif statement['curriculum_version'] == 'draft_2025':
            db_statement['version_status'] = 'consultation'
            db_statement['consultation_end_date'] = '2026-04-30'
        
        return db_statement
    
    def _get_version_status(self, version: str) -> str:
        """Get version status based on curriculum version"""
        if version == 'temataiaho_2025':
            return 'mandatory'
        elif version == 'draft_2025':
            return 'consultation'
        elif version == '2007_nzc':
            return 'active'
        else:
            return 'draft'
    
    def upload_statements(self, statements: List[Dict], batch_size: int = 50) -> Dict:
        """Upload statements in batches"""
        total = len(statements)
        logger.info(f"Uploading {total} statements in batches of {batch_size}...")
        
        inserted = 0
        skipped = 0
        errors = 0
        
        # Process in batches
        for i in tqdm(range(0, total, batch_size), desc="Uploading batches"):
            batch = statements[i:i + batch_size]
            batch_results = []
            
            for statement in batch:
                # Check for duplicates
                if self.check_duplicate(statement):
                    logger.debug(f"Skipping duplicate: {statement['statement_text'][:50]}...")
                    skipped += 1
                    continue
                
                # Prepare for database
                db_statement = self.prepare_statement_for_db(statement)
                batch_results.append(db_statement)
            
            # Insert batch
            if batch_results:
                try:
                    self.client.table('curriculum_statements').insert(batch_results).execute()
                    inserted += len(batch_results)
                    logger.info(f"✓ Inserted batch of {len(batch_results)} statements")
                except Exception as e:
                    logger.error(f"Error inserting batch: {e}")
                    errors += len(batch_results)
        
        self.stats['total_processed'] += total
        self.stats['inserted'] += inserted
        self.stats['skipped_duplicates'] += skipped
        self.stats['errors'] += errors
        
        return {
            'total': total,
            'inserted': inserted,
            'skipped': skipped,
            'errors': errors
        }
    
    def upload_file(self, file_path: Path) -> Dict:
        """Upload statements from a single JSON file"""
        logger.info(f"\n{'='*60}")
        logger.info(f"Uploading: {file_path.name}")
        logger.info(f"{'='*60}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            logger.error(f"Error reading file: {e}")
            return {'status': 'error', 'error': str(e)}
        
        statements = data.get('statements', [])
        
        if not statements:
            logger.warning("No statements found in file")
            return {'status': 'no_statements', 'file': file_path.name}
        
        result = self.upload_statements(statements)
        result['file'] = file_path.name
        result['status'] = 'success' if result['errors'] == 0 else 'partial'
        
        logger.info(f"\nResults for {file_path.name}:")
        logger.info(f"  Inserted: {result['inserted']}")
        logger.info(f"  Skipped (duplicates): {result['skipped']}")
        logger.info(f"  Errors: {result['errors']}")
        
        return result
    
    def upload_directory(self, directory: Path) -> Dict:
        """Upload all JSON files in a directory"""
        results = []
        
        json_files = list(directory.glob('*.json'))
        # Exclude summary/report files
        json_files = [
            f for f in json_files 
            if 'summary' not in f.name.lower() and 'report' not in f.name.lower()
        ]
        
        if not json_files:
            logger.warning(f"No curriculum JSON files found in {directory}")
            return {'status': 'no_files', 'results': []}
        
        logger.info(f"Found {len(json_files)} files to upload")
        
        for json_file in json_files:
            result = self.upload_file(json_file)
            results.append(result)
        
        # Generate summary
        logger.info(f"\n{'='*60}")
        logger.info("UPLOAD SUMMARY")
        logger.info(f"{'='*60}")
        logger.info(f"Total files processed: {len(results)}")
        logger.info(f"Total statements processed: {self.stats['total_processed']}")
        logger.info(f"Inserted: {self.stats['inserted']}")
        logger.info(f"Skipped (duplicates): {self.stats['skipped_duplicates']}")
        logger.info(f"Errors: {self.stats['errors']}")
        
        # Refresh materialized view
        try:
            logger.info("\nRefreshing curriculum_navigation materialized view...")
            self.client.rpc('refresh_curriculum_navigation').execute()
            logger.info("✓ Materialized view refreshed")
        except Exception as e:
            logger.warning(f"Could not refresh materialized view: {e}")
        
        # Save upload report
        report_file = directory / 'upload_report.json'
        report = {
            'upload_date': __import__('datetime').datetime.now().isoformat(),
            'stats': self.stats,
            'files': results
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"\n✓ Upload report saved to: {report_file}")
        
        return report
    
    def verify_upload(self) -> Dict:
        """Verify uploaded data"""
        logger.info(f"\n{'='*60}")
        logger.info("VERIFYING UPLOAD")
        logger.info(f"{'='*60}")
        
        # Count statements by version
        versions = ['temataiaho_2025', 'draft_2025', '2007_nzc']
        counts = {}
        
        for version in versions:
            try:
                result = self.client.table('curriculum_statements').select(
                    'id', count='exact'
                ).eq('curriculum_version', version).execute()
                counts[version] = result.count
                logger.info(f"{version}: {result.count} statements")
            except Exception as e:
                logger.error(f"Error counting {version}: {e}")
                counts[version] = None
        
        # Check for statements without phase or level
        try:
            result = self.client.table('curriculum_statements').select(
                'id', count='exact'
            ).is_('phase', 'null').is_('level', 'null').execute()
            
            if result.count > 0:
                logger.warning(f"⚠️  Found {result.count} statements without phase OR level!")
            else:
                logger.info("✓ All statements have phase OR level")
        except Exception as e:
            logger.error(f"Error checking phase/level: {e}")
        
        return counts


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Upload validated curriculum data to Supabase')
    parser.add_argument('directory', help='Directory containing validated JSON files')
    parser.add_argument('--file', help='Upload specific file only')
    parser.add_argument('--no-verify', action='store_true', help='Skip post-upload verification')
    
    args = parser.parse_args()
    
    directory = Path(args.directory)
    if not directory.exists():
        logger.error(f"Directory not found: {directory}")
        return 1
    
    try:
        uploader = CurriculumUploader()
        
        if args.file:
            # Upload specific file
            file_path = directory / args.file
            if not file_path.exists():
                logger.error(f"File not found: {file_path}")
                return 1
            result = uploader.upload_file(file_path)
        else:
            # Upload all files
            result = uploader.upload_directory(directory)
        
        # Verify upload
        if not args.no_verify:
            uploader.verify_upload()
        
        # Return success/failure
        if uploader.stats['errors'] > 0:
            logger.error(f"\n❌ Upload completed with {uploader.stats['errors']} errors")
            return 1
        else:
            logger.info(f"\n✅ Upload successful: {uploader.stats['inserted']} statements inserted!")
            return 0
    
    except Exception as e:
        logger.error(f"Upload failed: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    exit(main())

