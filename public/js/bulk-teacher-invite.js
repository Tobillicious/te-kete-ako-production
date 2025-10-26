// Bulk Teacher Invitation System
// Created: October 26, 2025
// Purpose: CSV upload for inviting multiple teachers at once (SIMULATION-DRIVEN!)

class BulkTeacherInvite {
    constructor() {
        this.teachers = [];
    }
    
    initUploadButton() {
        // Create CSV upload button in admin dashboard
        const uploadHTML = `
            <div style="margin: 2rem 0; padding: 2rem; background: #f9fafb; border-radius: 12px; border: 2px dashed #d1d5db;">
                <h3 style="color: #2F4F2F; margin: 0 0 1rem;">📤 Bulk Invite Teachers (CSV)</h3>
                <p style="color: #666; margin: 0 0 1rem;">
                    Upload a CSV file with teacher emails to invite multiple teachers at once.
                </p>
                
                <div style="margin-bottom: 1rem;">
                    <strong>CSV Format:</strong>
                    <code style="display: block; background: white; padding: 0.5rem; border-radius: 4px; margin-top: 0.5rem;">
                        name,email,subjects<br>
                        John Smith,j.smith@school.nz,Mathematics<br>
                        Emma Wilson,e.wilson@school.nz,English
                    </code>
                </div>
                
                <input 
                    type="file" 
                    id="csv-upload" 
                    accept=".csv" 
                    style="display: none;"
                    onchange="window.bulkTeacherInvite.handleCSVUpload(event)"
                />
                
                <button 
                    onclick="document.getElementById('csv-upload').click()" 
                    style="
                        background: #8B4513;
                        color: white;
                        padding: 1rem 2rem;
                        border: none;
                        border-radius: 8px;
                        font-weight: 600;
                        cursor: pointer;
                        font-size: 1rem;
                    "
                >
                    📁 Choose CSV File
                </button>
                
                <a 
                    href="/sample-teacher-invite.csv" 
                    download 
                    style="
                        display: inline-block;
                        margin-left: 1rem;
                        color: #8B4513;
                        text-decoration: underline;
                    "
                >
                    Download Sample CSV
                </a>
                
                <div id="csv-preview" style="margin-top: 1.5rem;"></div>
            </div>
        `;
        
        // Insert into admin dashboard if present
        const inviteSection = document.querySelector('.admin-content');
        if (inviteSection) {
            inviteSection.insertAdjacentHTML('beforeend', uploadHTML);
        }
    }
    
    async handleCSVUpload(event) {
        const file = event.target.files[0];
        if (!file) return;
        
        const reader = new FileReader();
        
        reader.onload = async (e) => {
            const csv = e.target.result;
            this.teachers = this.parseCSV(csv);
            this.showPreview();
        };
        
        reader.readAsText(file);
    }
    
    parseCSV(csv) {
        const lines = csv.trim().split('\n');
        const headers = lines[0].split(',').map(h => h.trim());
        
        const teachers = [];
        
        for (let i = 1; i < lines.length; i++) {
            const values = lines[i].split(',').map(v => v.trim());
            
            if (values.length >= 2) { // At minimum, need name and email
                teachers.push({
                    name: values[0] || '',
                    email: values[1] || '',
                    subjects: values[2] || ''
                });
            }
        }
        
        return teachers;
    }
    
    showPreview() {
        const preview = document.getElementById('csv-preview');
        
        if (this.teachers.length === 0) {
            preview.innerHTML = `
                <div style="background: #fee2e2; color: #991b1b; padding: 1rem; border-radius: 8px;">
                    ❌ No valid teachers found in CSV. Please check the format.
                </div>
            `;
            return;
        }
        
        const tableHTML = `
            <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);">
                <h4 style="color: #2F4F2F; margin: 0 0 1rem;">
                    ✅ Found ${this.teachers.length} teacher${this.teachers.length !== 1 ? 's' : ''} to invite
                </h4>
                
                <table style="width: 100%; border-collapse: collapse;">
                    <thead>
                        <tr style="background: #f3f4f6;">
                            <th style="padding: 0.75rem; text-align: left; border-bottom: 2px solid #e5e7eb;">Name</th>
                            <th style="padding: 0.75rem; text-align: left; border-bottom: 2px solid #e5e7eb;">Email</th>
                            <th style="padding: 0.75rem; text-align: left; border-bottom: 2px solid #e5e7eb;">Subjects</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${this.teachers.map(t => `
                            <tr>
                                <td style="padding: 0.75rem; border-bottom: 1px solid #f3f4f6;">${t.name}</td>
                                <td style="padding: 0.75rem; border-bottom: 1px solid #f3f4f6;">${t.email}</td>
                                <td style="padding: 0.75rem; border-bottom: 1px solid #f3f4f6;">${t.subjects || 'Not specified'}</td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
                
                <div style="margin-top: 1.5rem; display: flex; gap: 1rem;">
                    <button 
                        onclick="window.bulkTeacherInvite.sendInvitations()" 
                        style="
                            flex: 1;
                            background: #16a34a;
                            color: white;
                            padding: 1rem;
                            border: none;
                            border-radius: 8px;
                            font-weight: 600;
                            cursor: pointer;
                            font-size: 1rem;
                        "
                    >
                        📧 Send Invitations to All ${this.teachers.length} Teachers
                    </button>
                    <button 
                        onclick="window.bulkTeacherInvite.clearPreview()" 
                        style="
                            background: #e5e7eb;
                            color: #374151;
                            padding: 1rem 2rem;
                            border: none;
                            border-radius: 8px;
                            font-weight: 600;
                            cursor: pointer;
                            font-size: 1rem;
                        "
                    >
                        Cancel
                    </button>
                </div>
            </div>
        `;
        
        preview.innerHTML = tableHTML;
    }
    
    async sendInvitations() {
        const preview = document.getElementById('csv-preview');
        
        preview.innerHTML = `
            <div style="background: #dbeafe; color: #1e40af; padding: 1.5rem; border-radius: 12px; text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">📧</div>
                <h4 style="margin: 0 0 0.5rem;">Sending Invitations...</h4>
                <p style="margin: 0;">Please wait while we send ${this.teachers.length} invitations.</p>
            </div>
        `;
        
        try {
            // Call the invite function for each teacher
            const promises = this.teachers.map(teacher => 
                fetch('/.netlify/functions/invite-teacher-to-school', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        name: teacher.name,
                        email: teacher.email,
                        subjects: teacher.subjects
                    })
                })
            );
            
            await Promise.all(promises);
            
            preview.innerHTML = `
                <div style="background: #d1fae5; color: #065f46; padding: 2rem; border-radius: 12px; text-align: center;">
                    <div style="font-size: 4rem; margin-bottom: 1rem;">🎉</div>
                    <h4 style="margin: 0 0 0.5rem;">Success!</h4>
                    <p style="margin: 0;">
                        ${this.teachers.length} invitation${this.teachers.length !== 1 ? 's' : ''} sent successfully!
                    </p>
                    <button 
                        onclick="location.reload()" 
                        style="
                            margin-top: 1.5rem;
                            background: #16a34a;
                            color: white;
                            padding: 1rem 2rem;
                            border: none;
                            border-radius: 8px;
                            font-weight: 600;
                            cursor: pointer;
                        "
                    >
                        Done
                    </button>
                </div>
            `;
            
            // Clear teachers array
            this.teachers = [];
            
        } catch (error) {
            console.error('Bulk invitation error:', error);
            
            preview.innerHTML = `
                <div style="background: #fee2e2; color: #991b1b; padding: 1.5rem; border-radius: 12px;">
                    <h4 style="margin: 0 0 0.5rem;">❌ Error Sending Invitations</h4>
                    <p style="margin: 0;">${error.message || 'Please try again or contact support.'}</p>
                    <button 
                        onclick="window.bulkTeacherInvite.clearPreview()" 
                        style="
                            margin-top: 1rem;
                            background: #dc2626;
                            color: white;
                            padding: 0.75rem 1.5rem;
                            border: none;
                            border-radius: 8px;
                            font-weight: 600;
                            cursor: pointer;
                        "
                    >
                        Close
                    </button>
                </div>
            `;
        }
    }
    
    clearPreview() {
        document.getElementById('csv-preview').innerHTML = '';
        document.getElementById('csv-upload').value = '';
        this.teachers = [];
    }
}

// Initialize global instance
if (typeof window !== 'undefined') {
    window.bulkTeacherInvite = new BulkTeacherInvite();
    
    // Auto-init on admin dashboard
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            if (window.location.pathname.includes('school-admin-dashboard')) {
                window.bulkTeacherInvite.initUploadButton();
            }
        });
    } else {
        if (window.location.pathname.includes('school-admin-dashboard')) {
            window.bulkTeacherInvite.initUploadButton();
        }
    }
}

