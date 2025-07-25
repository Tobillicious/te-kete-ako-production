import os

class KaitoiAgent:
    """
    An agent for improving the visual design and styling of resources.
    """
    def __init__(self, project_root):
        self.project_root = os.path.abspath(project_root)

    def add_stylesheet_links(self, dry_run=True):
        """
        Adds a stylesheet link to all HTML files that are missing one.
        """
        html_files = self._find_html_files()
        report = {"files_to_modify": [], "total_files_scanned": len(html_files)}

        for file_path in html_files:
            if self._needs_stylesheet(file_path):
                relative_path = os.path.relpath(file_path, self.project_root)
                report["files_to_modify"].append(relative_path)
                if not dry_run:
                    self._add_stylesheet_link(file_path)
        
        return report

    def _find_html_files(self):
        """Finds all HTML files within the project directory."""
        html_files = []
        for root, _, files in os.walk(self.project_root):
            if 'adk' in root or 'agents' in root:
                continue
            for file in files:
                if file.endswith(".html"):
                    html_files.append(os.path.join(root, file))
        return html_files

    def _needs_stylesheet(self, file_path):
        """Checks if an HTML file is missing the main stylesheet."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            return 'href="css/main.css"' not in content and 'href="../css/main.css"' not in content
        except IOError:
            return False

    def _add_stylesheet_link(self, file_path):
        """Adds the main.css stylesheet link to the <head> of an HTML file."""
        depth = os.path.relpath(file_path, self.project_root).count(os.sep)
        stylesheet_path = '../' * depth + 'css/main.css'
        link_tag = f'<link rel="stylesheet" href="{stylesheet_path}">'

        try:
            with open(file_path, 'r+', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if '</head>' in content:
                    content = content.replace('</head>', f'    {link_tag}\n</head>')
                    f.seek(0)
                    f.write(content)
                    f.truncate()
        except IOError as e:
            print(f"Could not modify {file_path}: {e}")


if __name__ == '__main__':
    import json
    agent = KaitoiAgent(project_root="/Users/admin/Documents/te-kete-ako-clean")
    # Perform a dry run first to see what will be changed
    dry_run_report = agent.add_stylesheet_links(dry_run=True)
    print("Dry Run Report:")
    print(json.dumps(dry_run_report, indent=4))

    # If the dry run looks good, run the agent to actually modify the files
    agent.add_stylesheet_links(dry_run=False)
    print("\nStylesheet links added.")
