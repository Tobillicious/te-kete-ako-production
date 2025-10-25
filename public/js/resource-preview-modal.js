/**
 * RESOURCE PREVIEW MODAL - P1-11
 * Allows teachers to quickly preview resources before downloading
 * Priority Score: 1.80 | Impact: 18% users | Effort: 6h
 */

class ResourcePreviewModal {
    constructor() {
        this.modal = null;
        this.currentResource = null;
        this.init();
    }
    
    init() {
        // Create modal HTML
        this.createModalHTML();
        
        // Add event listeners to all resource links
        this.attachPreviewListeners();
        
        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && this.modal && this.modal.classList.contains('active')) {
                this.closeModal();
            }
        });
    }
    
    createModalHTML() {
        const modalHTML = `
            <div id="resource-preview-modal" class="preview-modal">
                <div class="modal-overlay" onclick="window.ResourcePreview.closeModal()"></div>
                <div class="modal-content">
                    <div class="modal-header">
                        <h2 id="modal-title">Resource Preview</h2>
                        <button class="modal-close" onclick="window.ResourcePreview.closeModal()">✕</button>
                    </div>
                    
                    <div class="modal-body">
                        <!-- Resource Info -->
                        <div id="modal-info" class="resource-info">
                            <div class="info-badges"></div>
                            <div class="info-meta"></div>
                        </div>
                        
                        <!-- Preview Content -->
                        <div id="modal-preview" class="preview-content">
                            <p class="text-gray-500">Loading preview...</p>
                        </div>
                    </div>
                    
                    <div class="modal-footer">
                        <button class="btn btn-secondary" onclick="window.ResourcePreview.printResource()">
                            🖨️ Print Preview
                        </button>
                        <button class="btn btn-secondary" onclick="window.ResourcePreview.downloadResource()">
                            📥 Download PDF
                        </button>
                        <button class="btn btn-primary" onclick="window.ResourcePreview.openResource()">
                            📖 Open Full Resource
                        </button>
                    </div>
                </div>
            </div>
        `;
        
        document.body.insertAdjacentHTML('beforeend', modalHTML);
        this.modal = document.getElementById('resource-preview-modal');
    }
    
    attachPreviewListeners() {
        // Add preview buttons to resource cards
        document.addEventListener('click', (e) => {
            const previewBtn = e.target.closest('[data-preview-resource]');
            if (previewBtn) {
                e.preventDefault();
                e.stopPropagation();
                const resourcePath = previewBtn.dataset.previewResource;
                this.showPreview(resourcePath);
            }
        });
        
        // Auto-add preview capability to resource links on page load
        document.addEventListener('DOMContentLoaded', () => {
            this.addPreviewButtons();
        });
        
        // Also run after a delay for dynamically loaded content
        setTimeout(() => this.addPreviewButtons(), 1000);
    }
    
    addPreviewButtons() {
        // Add preview buttons to resource cards that don't have them
        const resourceLinks = document.querySelectorAll('a[href*="/lessons/"], a[href*="/units/"], a[href*="/handouts/"]');
        resourceLinks.forEach(link => {
            if (!link.dataset.previewResource && !link.closest('.no-preview')) {
                link.dataset.previewResource = link.href;
            }
        });
    }
    
    async showPreview(resourcePath) {
        this.currentResource = resourcePath;
        
        try {
            // Get resource metadata from Supabase
            const supabase = await window.supabaseSingleton.getClient();
            const { data: resource } = await supabase
                .from('resources')
                .select('*')
                .eq('path', resourcePath)
                .single();
            
            if (resource) {
                // Update modal with resource info
                document.getElementById('modal-title').textContent = resource.title;
                
                // Add badges
                const badgesHTML = `
                    <span class="badge badge-primary">${resource.subject || 'General'}</span>
                    <span class="badge badge-secondary">${resource.level || 'All Levels'}</span>
                    <span class="badge badge-info">${resource.type || 'Resource'}</span>
                    ${resource.featured ? '<span class="badge badge-success">⭐ Featured</span>' : ''}
                    ${resource.cultural_elements?.cultural_integration_score >= 90 ? 
                      `<span class="badge" style="background: #10b981; color: white;">🌿 ${resource.cultural_elements.cultural_integration_score}% Cultural</span>` : ''}
                `;
                document.querySelector('.info-badges').innerHTML = badgesHTML;
                
                // Add meta info
                const metaHTML = `
                    <p class="text-gray-700">${resource.description || 'No description available'}</p>
                `;
                document.querySelector('.info-meta').innerHTML = metaHTML;
                
                // Load preview (first section of content)
                this.loadPreviewContent(resourcePath);
            }
            
            // Show modal
            this.modal.classList.add('active');
            document.body.style.overflow = 'hidden';
            
        } catch (error) {
            console.error('Preview error:', error);
            alert('Could not load resource preview. Please try opening the full resource.');
        }
    }
    
    async loadPreviewContent(resourcePath) {
        try {
            // Fetch the HTML content
            const response = await fetch(resourcePath);
            const html = await response.text();
            
            // Parse and extract main content (simplified preview)
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            
            // Get first meaningful section
            const content = doc.querySelector('main, .content, article, section') || doc.body;
            
            // Create preview (first 500 characters)
            const previewText = content.textContent.substring(0, 500) + '...';
            
            document.getElementById('modal-preview').innerHTML = `
                <div class="preview-scroll">
                    <p class="text-gray-700 leading-relaxed">${previewText}</p>
                    <p class="text-sm text-gray-500 mt-4 italic">
                        Preview showing first section. Open full resource to see complete content.
                    </p>
                </div>
            `;
            
        } catch (error) {
            document.getElementById('modal-preview').innerHTML = `
                <p class="text-gray-500">Preview not available. Please open the full resource.</p>
            `;
        }
    }
    
    closeModal() {
        if (this.modal) {
            this.modal.classList.remove('active');
            document.body.style.overflow = '';
        }
    }
    
    printResource() {
        if (this.currentResource) {
            window.open(this.currentResource, '_blank');
            setTimeout(() => window.print(), 500);
        }
    }
    
    downloadResource() {
        if (this.currentResource) {
            // For now, open in new tab (PDF generation would be added later)
            window.open(this.currentResource + '?download=true', '_blank');
        }
    }
    
    openResource() {
        if (this.currentResource) {
            window.location.href = this.currentResource;
        }
    }
}

// Auto-initialize
if (typeof window !== 'undefined') {
    window.addEventListener('DOMContentLoaded', () => {
        window.ResourcePreview = new ResourcePreviewModal();
    });
}

