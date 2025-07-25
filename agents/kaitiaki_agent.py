import os
import json

class KaitiakiAgent:
    """
    An agent responsible for auditing the quality and consistency of HTML resources.
    """
    def __init__(self, project_root):
        self.project_root = os.path.abspath(project_root)

    def audit_html_files(self):
        """
        Performs a comprehensive audit of all HTML files in the project.
        """
        html_files = self._find_html_files()
        
        report = {
            "total_files_found": len(html_files),
            "files_by_directory": self._categorize_by_directory(html_files),
            "quality_assessment": self._assess_quality(html_files)
        }
        
        return report

    def _find_html_files(self):
        """Finds all HTML files within the project directory."""
        html_files = []
        for root, _, files in os.walk(self.project_root):
            # Exclude the 'adk' and 'agents' directories from the audit
            if 'adk' in root or 'agents' in root:
                continue
            for file in files:
                if file.endswith(".html"):
                    html_files.append(os.path.join(root, file))
        return html_files

    def _categorize_by_directory(self, files):
        """Categorizes a list of files by their parent directory, relative to the project root."""
        categorized = {}
        for file_path in files:
            relative_path = os.path.relpath(file_path, self.project_root)
            # Get the directory part of the relative path
            dir_name = os.path.dirname(relative_path)
            if not dir_name:
                dir_name = "(root)"
            
            if dir_name not in categorized:
                categorized[dir_name] = []
            categorized[dir_name].append(os.path.basename(file_path))
        return categorized

    def _assess_quality(self, files):
        """Assesses the quality of HTML files based on a set of simple heuristics."""
        assessment = []
        for file_path in files:
            issues = []
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
            except IOError as e:
                issues.append(f"Could not read file: {e}")
                assessment.append({
                    "file": os.path.basename(file_path),
                    "path": os.path.relpath(file_path, self.project_root),
                    "issues": issues
                })
                continue

            # Heuristic checks
            if "<title>" not in content or "<title></title>" in content:
                issues.append("Missing or empty <title> tag")
            if 'href="css/main.css"' not in content and 'href="../css/main.css"' not in content:
                issues.append("Potentially missing main stylesheet link")
            if "whakatauki" not in content.lower() and "whakataukī" not in content.lower():
                issues.append("Missing Whakataukī")
            
            if issues:
                assessment.append({
                    "file": os.path.basename(file_path),
                    "path": os.path.relpath(file_path, self.project_root),
                    "issues": issues
                })
        return assessment

if __name__ == '__main__':
    # The script is now more robust and provides a clearer report.
    agent = KaitiakiAgent(project_root="/Users/admin/Documents/te-kete-ako-clean")
    audit_report = agent.audit_html_files()
    print(json.dumps(audit_report, indent=4))