/**
 * DOWNLOAD MANAGER - P1-9
 * Adds download buttons to all resources (PDF/DOCX)
 * Priority Score: 1.20 | Impact: 15% users | Effort: 4h
 */

class DownloadManager {
    constructor() {
        this.init();
    }
    
    init() {
        // Add download buttons to resource cards
        this.addDownloadButtons();
        
        // Listen for dynamic content loads
        document.addEventListener('DOMContentLoaded', () => {
            setTimeout(() => this.addDownloadButtons(), 1000);
        });
    }
    
    addDownloadButtons() {
        // Find all resource links/cards
        const resourceElements = document.querySelectorAll('a[href*="/public/"], a[href*="/lessons/"], a[href*="/handouts/"], a[href*="/units/"]');
        
        resourceElements.forEach(element => {
            // Skip if already has download button
            if (element.querySelector('.download-btn')) {
                return;
            }
            
            const href = element.getAttribute('href');
            if (!href || href.startsWith('#')) return;
            
            // Create download button group
            const downloadGroup = document.createElement('div');
            downloadGroup.className = 'download-buttons';
            downloadGroup.innerHTML = `
                <button class="download-btn download-pdf" onclick="event.preventDefault(); event.stopPropagation(); window.DownloadManager.downloadPDF('${href}');" title="Download as PDF">
                    📥 PDF
                </button>
                <button class="download-btn download-print" onclick="event.preventDefault(); event.stopPropagation(); window.DownloadManager.printResource('${href}');" title="Print this resource">
                    🖨️ Print
                </button>
            `;
            
            // Add to card footer or append
            const cardFooter = element.querySelector('.card-footer, .flex.gap-2');
            if (cardFooter) {
                cardFooter.appendChild(downloadGroup);
            }
        });
    }
    
    /**
     * Download resource as PDF
     */
    downloadPDF(resourcePath) {
        // Open in new window and trigger browser print-to-PDF
        const printWindow = window.open(resourcePath, '_blank');
        
        if (printWindow) {
            printWindow.onload = () => {
                setTimeout(() => {
                    printWindow.print();
                }, 500);
            };
        } else {
            alert('Please allow popups to download PDF');
        }
    }
    
    /**
     * Print resource directly
     */
    printResource(resourcePath) {
        const printWindow = window.open(resourcePath, '_blank');
        
        if (printWindow) {
            printWindow.onload = () => {
                printWindow.print();
            };
        }
    }
    
    /**
     * Future: Download as DOCX (editable)
     * Would require server-side conversion
     */
    downloadDOCX(resourcePath) {
        // Placeholder for future implementation
        alert('DOCX download coming soon! For now, use PDF and convert if needed.');
    }
}

// CSS for download buttons
const downloadButtonsCSS = `
<style>
.download-buttons {
    display: flex;
    gap: 0.5rem;
    margin-top: 0.75rem;
    flex-wrap: wrap;
}

.download-btn {
    padding: 0.5rem 1rem;
    border: 2px solid #cbd5e1;
    background: white;
    border-radius: 8px;
    font-size: 0.875rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    white-space: nowrap;
}

.download-pdf {
    border-color: #3b82f6;
    color: #1e40af;
}

.download-pdf:hover {
    background: #3b82f6;
    color: white;
    transform: translateY(-2px);
}

.download-print {
    border-color: #10b981;
    color: #065f46;
}

.download-print:hover {
    background: #10b981;
    color: white;
    transform: translateY(-2px);
}

/* Mobile responsive */
@media (max-width: 640px) {
    .download-buttons {
        width: 100%;
    }
    
    .download-btn {
        flex: 1;
        font-size: 0.75rem;
        padding: 0.4rem 0.75rem;
    }
}

/* Print - hide download buttons */
@media print {
    .download-buttons {
        display: none !important;
    }
}
</style>
`;

// Inject CSS
document.head.insertAdjacentHTML('beforeend', downloadButtonsCSS);

// Auto-initialize
if (typeof window !== 'undefined') {
    window.DownloadManager = new DownloadManager();
}

