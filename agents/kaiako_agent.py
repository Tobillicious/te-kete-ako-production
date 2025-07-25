import os
import json
import random

class KaiakoAgent:
    """
    An agent for creating and enriching educational content.
    """
    def __init__(self, project_root):
        self.project_root = os.path.abspath(project_root)
        self.whakatauki_list = [
            {"mi": "He aha te mea nui o te ao? He tangata, he tangata, he tangata.", "en": "What is the most important thing in the world? It is the people, it is the people, it is the people."},
            {"mi": "Whāia te mātauranga hei oranga mō koutou.", "en": "Seek after learning for the sake of your wellbeing."},
            {"mi": "He waka eke noa.", "en": "We are all in this together."},
            {"mi": "Mā te kōrero, ka mōhio; mā te mōhio, ka mārama; mā te mārama, ka mātau; mā te mātau, ka ora.", "en": "Through discussion comes awareness; through awareness comes understanding; through understanding comes knowledge; through knowledge comes life."},
            {"mi": "Poipoia te kakano kia puawai.", "en": "Nurture the seed and it will blossom."}
        ]

    def add_whakatauki(self, dry_run=True):
        """
        Adds a whakataukī to all HTML files that are missing one.
        """
        html_files = self._find_html_files()
        report = {"files_to_modify": [], "total_files_scanned": len(html_files)}

        for file_path in html_files:
            if self._needs_whakatauki(file_path):
                relative_path = os.path.relpath(file_path, self.project_root)
                report["files_to_modify"].append(relative_path)
                if not dry_run:
                    self._add_whakatauki(file_path)
        
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

    def _needs_whakatauki(self, file_path):
        """Checks if an HTML file is missing a whakataukī."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read().lower()
            return "whakatauki" not in content and "whakataukī" not in content
        except IOError:
            return False

    def _add_whakatauki(self, file_path):
        """Adds a random whakataukī to the sidebar of an HTML file."""
        whakatauki = random.choice(self.whakatauki_list)
        whakatauki_html = f'''
            <div class="sidebar-widget">
                <h3 class="sidebar-widget-title">Today's Whakataukī</h3>
                <p style="font-style: italic; color: var(--color-secondary);">"{whakatauki["mi"]}"</p>
                <p style="font-size: 0.9rem;">{whakatauki["en"]}</p>
            </div>
        '''
        try:
            with open(file_path, 'r+', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                # Add to sidebar if it exists, otherwise skip
                if '<aside class="left-sidebar no-print">' in content:
                    content = content.replace('<aside class="left-sidebar no-print">', f'<aside class="left-sidebar no-print">{whakatauki_html}')
                    f.seek(0)
                    f.write(content)
                    f.truncate()
        except IOError as e:
            print(f"Could not modify {file_path}: {e}")


if __name__ == '__main__':
    import json
    agent = KaiakoAgent(project_root="/Users/admin/Documents/te-kete-ako-clean")
    # Perform a dry run first to see what will be changed
    dry_run_report = agent.add_whakatauki(dry_run=True)
    print("Dry Run Report:")
    print(json.dumps(dry_run_report, indent=4))

    # If the dry run looks good, run the agent to actually modify the files
    agent.add_whakatauki(dry_run=False)
    print("\nWhakataukī added.")
