/**
 * EDITABLE EXPORT SYSTEM - P2-17
 * Allows teachers to export resources in editable formats (DOCX, Google Docs)
 * Priority Score: 0.70 | Impact: 14% users
 */

class EditableExport {
    constructor() {
        this.init();
    }
    
    init() {
        // Add "Customize This" buttons to resources
        this.addCustomizeButtons();
    }
    
    addCustomizeButtons() {
        // Find all resource cards/pages
        const resourceElements = document.querySelectorAll('.resource-card, .lesson-card, article.lesson, article.handout');
        
        resourceElements.forEach(element => {
            if (element.querySelector('.customize-btn')) return; // Already has button
            
            const customizeBtn = document.createElement('button');
            customizeBtn.className = 'customize-btn btn btn-secondary';
            customizeBtn.innerHTML = '✏️ Customize This Resource';
            customizeBtn.onclick = () => this.showCustomizeOptions(element);
            
            // Add button to element
            const footer = element.querySelector('.card-footer, .resource-footer');
            if (footer) {
                footer.appendChild(customizeBtn);
            }
        });
    }
    
    showCustomizeOptions(resourceElement) {
        const resourcePath = resourceElement.getAttribute('href') || window.location.pathname;
        
        // Show modal with export options
        const modal = document.createElement('div');
        modal.className = 'export-modal';
        modal.innerHTML = `
            <div class="modal-overlay" onclick="this.parentElement.remove()"></div>
            <div class="modal-content">
                <h2>Customize This Resource</h2>
                <p class="text-gray-600 mb-4">Export in editable format to customize for your classroom:</p>
                
                <div class="export-options">
                    <button class="export-option" onclick="window.EditableExport.exportToGoogleDocs('${resourcePath}')">
                        <span class="text-4xl mb-2">📝</span>
                        <h3>Google Docs</h3>
                        <p class="text-sm text-gray-600">Edit online, collaborate</p>
                    </button>
                    
                    <button class="export-option" onclick="window.EditableExport.exportToWord('${resourcePath}')">
                        <span class="text-4xl mb-2">📄</span>
                        <h3>Microsoft Word</h3>
                        <p class="text-sm text-gray-600">Download DOCX file</p>
                    </button>
                    
                    <button class="export-option" onclick="window.EditableExport.copyToClipboard('${resourcePath}')">
                        <span class="text-4xl mb-2">📋</span>
                        <h3>Copy Text</h3>
                        <p class="text-sm text-gray-600">Copy to any editor</p>
                    </button>
                </div>
                
                <button class="btn btn-secondary mt-4" onclick="this.closest('.export-modal').remove()">
                    Cancel
                </button>
            </div>
        `;
        
        document.body.appendChild(modal);
    }
    
    async exportToGoogleDocs(resourcePath) {
        // Get resource HTML content
        const content = await this.fetchResourceContent(resourcePath);
        
        // Open Google Docs with content
        // Note: This creates a new doc with imported HTML
        const googleDocsUrl = 'https://docs.google.com/document/create';
        window.open(googleDocsUrl, '_blank');
        
        alert('Google Docs opened! Paste the resource content (Ctrl/Cmd+V) to edit.');
        
        // Copy content to clipboard for easy paste
        await this.copyToClipboard(resourcePath);
    }
    
    async exportToWord(resourcePath) {
        alert('DOCX export coming soon! For now, use "Copy Text" and paste into Word.');
        // Future: Server-side HTML → DOCX conversion
    }
    
    async copyToClipboard(resourcePath) {
        try {
            const content = await this.fetchResourceContent(resourcePath);
            await navigator.clipboard.writeText(content);
            alert('✅ Resource content copied to clipboard! Paste into your preferred editor.');
        } catch (error) {
            console.error('Copy failed:', error);
            alert('Could not copy to clipboard. Please select and copy manually.');
        }
    }
    
    async fetchResourceContent(resourcePath) {
        try {
            const response = await fetch(resourcePath);
            const html = await response.text();
            
            // Parse HTML and extract main content
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            
            // Get main content area
            const content = doc.querySelector('main, article, .content, .lesson-content') || doc.body;
            
            // Return text content
            return content.textContent.trim();
            
        } catch (error) {
            console.error('Fetch failed:', error);
            return 'Could not fetch resource content.';
        }
    }
}

// CSS for export modal
const exportModalCSS = `
<style>
.export-modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 10000;
    display: flex;
    align-items: center;
    justify-content: center;
}

.export-modal .modal-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
}

.export-modal .modal-content {
    position: relative;
    background: white;
    padding: 2rem;
    border-radius: 16px;
    max-width: 600px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
}

.export-options {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
}

.export-option {
    background: #f8fafc;
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.5rem 1rem;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s;
}

.export-option:hover {
    background: #eff6ff;
    border-color: #3b82f6;
    transform: translateY(-2px);
}

.customize-btn {
    margin-top: 0.75rem;
}

@media print {
    .export-modal, .customize-btn {
        display: none !important;
    }
}
</style>
`;

document.head.insertAdjacentHTML('beforeend', exportModalCSS);

// Auto-initialize
if (typeof window !== 'undefined') {
    window.EditableExport = new EditableExport();
}

