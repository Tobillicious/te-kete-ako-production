"""
Curriculum Data Validator
Validates scraped curriculum data before uploading to Supabase
"""

import json
import logging
from typing import List, Dict, Tuple
from pathlib import Path
from collections import Counter

from config import VALIDATION_RULES

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CurriculumValidator:
    """Validates curriculum statement data"""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.stats = {
            'total_statements': 0,
            'valid_statements': 0,
            'invalid_statements': 0,
            'warnings': 0
        }
    
    def validate_statement(self, statement: Dict, index: int) -> Tuple[bool, List[str], List[str]]:
        """Validate a single curriculum statement"""
        errors = []
        warnings = []
        
        # Check required fields
        for field in VALIDATION_RULES['required_fields']:
            if field not in statement or not statement[field]:
                errors.append(f"Statement {index}: Missing required field '{field}'")
        
        # Validate statement text length
        statement_text = statement.get('statement_text', '')
        min_len = VALIDATION_RULES['min_statement_length']
        max_len = VALIDATION_RULES['max_statement_length']
        
        if len(statement_text) < min_len:
            errors.append(f"Statement {index}: Text too short ({len(statement_text)} chars, min {min_len})")
        elif len(statement_text) > max_len:
            warnings.append(f"Statement {index}: Text very long ({len(statement_text)} chars, max {max_len})")
        
        # Check for invalid phrases (placeholders)
        statement_lower = statement_text.lower()
        for phrase in VALIDATION_RULES['invalid_phrases']:
            if phrase.lower() in statement_lower:
                errors.append(f"Statement {index}: Contains invalid phrase '{phrase}'")
        
        # Validate curriculum version
        valid_versions = ['2007_nzc', 'temataiaho_2025', 'draft_2025']
        if statement.get('curriculum_version') not in valid_versions:
            errors.append(f"Statement {index}: Invalid curriculum_version '{statement.get('curriculum_version')}'")
        
        # Validate year levels (if present)
        year_levels = statement.get('year_levels', [])
        if year_levels:
            if not isinstance(year_levels, list):
                errors.append(f"Statement {index}: year_levels must be a list")
            elif not all(isinstance(y, int) and 0 <= y <= 13 for y in year_levels):
                errors.append(f"Statement {index}: Invalid year_levels {year_levels} (must be 0-13)")
        
        # Validate phase OR level is present (Te Mātaiaho vs 2007 NZC)
        if not statement.get('phase') and statement.get('level') is None:
            errors.append(f"Statement {index}: Must have either 'phase' or 'level'")
        
        # Validate element (for Te Mātaiaho)
        if statement.get('curriculum_version') == 'temataiaho_2025':
            if statement.get('element') not in ['Knowledge', 'Practices', None]:
                warnings.append(f"Statement {index}: Unexpected element '{statement.get('element')}'")
        
        return (len(errors) == 0, errors, warnings)
    
    def validate_file(self, file_path: Path) -> Dict:
        """Validate all statements in a JSON file"""
        logger.info(f"\n{'='*60}")
        logger.info(f"Validating: {file_path.name}")
        logger.info(f"{'='*60}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in {file_path}: {e}")
            return {
                'file': file_path.name,
                'status': 'json_error',
                'error': str(e)
            }
        
        statements = data.get('statements', [])
        file_errors = []
        file_warnings = []
        valid_count = 0
        invalid_count = 0
        
        self.stats['total_statements'] += len(statements)
        
        # Validate each statement
        for idx, statement in enumerate(statements, 1):
            is_valid, errors, warnings = self.validate_statement(statement, idx)
            
            if is_valid:
                valid_count += 1
                self.stats['valid_statements'] += 1
            else:
                invalid_count += 1
                self.stats['invalid_statements'] += 1
                file_errors.extend(errors)
            
            if warnings:
                file_warnings.extend(warnings)
                self.stats['warnings'] += len(warnings)
        
        # Log results
        logger.info(f"Total statements: {len(statements)}")
        logger.info(f"Valid: {valid_count}")
        logger.info(f"Invalid: {invalid_count}")
        logger.info(f"Warnings: {len(file_warnings)}")
        
        if file_errors:
            logger.error(f"\n{len(file_errors)} ERRORS:")
            for error in file_errors[:10]:  # Show first 10 errors
                logger.error(f"  - {error}")
            if len(file_errors) > 10:
                logger.error(f"  ... and {len(file_errors) - 10} more errors")
        
        if file_warnings:
            logger.warning(f"\n{len(file_warnings)} WARNINGS:")
            for warning in file_warnings[:5]:  # Show first 5 warnings
                logger.warning(f"  - {warning}")
            if len(file_warnings) > 5:
                logger.warning(f"  ... and {len(file_warnings) - 5} more warnings")
        
        # Generate statistics
        strands = [s.get('strand') for s in statements if s.get('strand')]
        elements = [s.get('element') for s in statements if s.get('element')]
        
        strand_counts = Counter(strands)
        element_counts = Counter(elements)
        
        logger.info(f"\nStrands: {dict(strand_counts)}")
        logger.info(f"Elements: {dict(element_counts)}")
        
        return {
            'file': file_path.name,
            'status': 'valid' if invalid_count == 0 else 'has_errors',
            'total': len(statements),
            'valid': valid_count,
            'invalid': invalid_count,
            'warnings': len(file_warnings),
            'errors': file_errors[:100],  # Keep first 100 errors
            'strand_distribution': dict(strand_counts),
            'element_distribution': dict(element_counts)
        }
    
    def validate_directory(self, directory: Path) -> Dict:
        """Validate all JSON files in a directory"""
        results = []
        
        json_files = list(directory.glob('*.json'))
        # Exclude summary files
        json_files = [f for f in json_files if 'summary' not in f.name.lower()]
        
        if not json_files:
            logger.warning(f"No JSON files found in {directory}")
            return {'status': 'no_files', 'results': []}
        
        logger.info(f"Found {len(json_files)} files to validate")
        
        for json_file in json_files:
            result = self.validate_file(json_file)
            results.append(result)
        
        # Generate overall summary
        logger.info(f"\n{'='*60}")
        logger.info("VALIDATION SUMMARY")
        logger.info(f"{'='*60}")
        logger.info(f"Total files: {len(results)}")
        logger.info(f"Total statements: {self.stats['total_statements']}")
        logger.info(f"Valid statements: {self.stats['valid_statements']}")
        logger.info(f"Invalid statements: {self.stats['invalid_statements']}")
        logger.info(f"Warnings: {self.stats['warnings']}")
        
        valid_files = [r for r in results if r['status'] == 'valid']
        error_files = [r for r in results if r['status'] == 'has_errors']
        
        logger.info(f"\nFiles with no errors: {len(valid_files)}")
        logger.info(f"Files with errors: {len(error_files)}")
        
        if error_files:
            logger.warning("\nFiles with errors:")
            for r in error_files:
                logger.warning(f"  - {r['file']}: {r['invalid']} invalid statements")
        
        # Save validation report
        report_file = directory / 'validation_report.json'
        report = {
            'validation_date': __import__('datetime').datetime.now().isoformat(),
            'stats': self.stats,
            'files': results,
            'summary': {
                'total_files': len(results),
                'valid_files': len(valid_files),
                'error_files': len(error_files)
            }
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"\n✓ Validation report saved to: {report_file}")
        
        return report


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate scraped curriculum data')
    parser.add_argument('directory', help='Directory containing JSON files to validate')
    
    args = parser.parse_args()
    
    directory = Path(args.directory)
    if not directory.exists():
        logger.error(f"Directory not found: {directory}")
        return 1
    
    validator = CurriculumValidator()
    report = validator.validate_directory(directory)
    
    # Exit with error code if there are invalid statements
    if validator.stats['invalid_statements'] > 0:
        logger.error(f"\n❌ Validation failed: {validator.stats['invalid_statements']} invalid statements")
        return 1
    else:
        logger.info(f"\n✅ Validation passed: All {validator.stats['total_statements']} statements are valid!")
        return 0


if __name__ == "__main__":
    exit(main())

