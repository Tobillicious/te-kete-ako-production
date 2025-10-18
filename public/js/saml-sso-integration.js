/**
 * SAML SSO Integration - Te Kete Ako
 * Enterprise school authentication and single sign-on
 * Phase 3 of Tech Stack Evolution
 */

class TeKeteSSO {
    constructor() {
        this.samlProvider = null;
        this.schoolConfig = null;
        this.init();
    }

    async init() {
        await this.loadSAMLProvider();
        this.setupSSOConfiguration();
        this.setupEnterpriseAuthentication();
        this.setupSchoolManagement();
    }

    async loadSAMLProvider() {
        // Load SAML.js library
        if (window.saml) {
            this.samlProvider = window.saml;
            return;
        }

        return new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/saml-js@latest/dist/saml.min.js';
            script.onload = () => {
                this.samlProvider = window.saml;
                resolve();
            };
            script.onerror = reject;
            document.head.appendChild(script);
        });
    }

    setupSSOConfiguration() {
        // Enterprise school configurations
        this.schoolConfigs = {
            'auckland-grammar': {
                name: 'Auckland Grammar School',
                ssoUrl: 'https://ags.school.nz/saml/sso',
                entityId: 'https://ags.school.nz/saml/metadata',
                certificate: 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...',
                attributes: {
                    email: 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress',
                    name: 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name',
                    role: 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/role',
                    department: 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/department'
                }
            },
            'wellington-college': {
                name: 'Wellington College',
                ssoUrl: 'https://wellingtoncollege.school.nz/saml/sso',
                entityId: 'https://wellingtoncollege.school.nz/saml/metadata',
                certificate: 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...',
                attributes: {
                    email: 'urn:oid:0.9.2342.19200300.100.1.3',
                    name: 'urn:oid:2.5.4.42',
                    role: 'urn:oid:2.5.4.32',
                    department: 'urn:oid:2.5.4.11'
                }
            },
            'christchurch-boys': {
                name: 'Christchurch Boys High School',
                ssoUrl: 'https://cbhs.school.nz/saml/sso',
                entityId: 'https://cbhs.school.nz/saml/metadata',
                certificate: 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...',
                attributes: {
                    email: 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress',
                    name: 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name',
                    role: 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/role',
                    yearLevel: 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/yearlevel'
                }
            }
        };
    }

    setupEnterpriseAuthentication() {
        // SSO Login buttons
        document.querySelectorAll('.sso-login-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const schoolId = e.target.getAttribute('data-school-id');
                this.initiateSSOLogin(schoolId);
            });
        });

        // Handle SSO callback
        this.handleSSOCallback();
    }

    async initiateSSOLogin(schoolId) {
        try {
            const config = this.schoolConfigs[schoolId];
            if (!config) {
                throw new Error('School configuration not found');
            }

            // Create SAML request
            const samlRequest = this.createSAMLRequest(config);
            
            // Redirect to school SSO
            const ssoUrl = `${config.ssoUrl}?SAMLRequest=${encodeURIComponent(samlRequest)}`;
            window.location.href = ssoUrl;
            
        } catch (error) {
            console.error('SSO login error:', error);
            this.showError('SSO authentication failed. Please try again.');
        }
    }

    createSAMLRequest(config) {
        const requestId = this.generateRequestId();
        const timestamp = new Date().toISOString();
        
        const samlRequest = `
            <samlp:AuthnRequest xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
                               xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
                               ID="${requestId}"
                               Version="2.0"
                               IssueInstant="${timestamp}"
                               Destination="${config.ssoUrl}"
                               AssertionConsumerServiceURL="${window.location.origin}/sso-callback.html">
                <saml:Issuer>${window.location.origin}</saml:Issuer>
                <samlp:NameIDPolicy Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"
                                   AllowCreate="true"/>
            </samlp:AuthnRequest>
        `;
        
        return btoa(samlRequest);
    }

    handleSSOCallback() {
        const urlParams = new URLSearchParams(window.location.search);
        const samlResponse = urlParams.get('SAMLResponse');
        const relayState = urlParams.get('RelayState');
        
        if (samlResponse) {
            this.processSAMLResponse(samlResponse);
        }
    }

    async processSAMLResponse(samlResponse) {
        try {
            // Decode and parse SAML response
            const decodedResponse = atob(samlResponse);
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(decodedResponse, 'text/xml');
            
            // Extract user attributes
            const userAttributes = this.extractUserAttributes(xmlDoc);
            
            // Create or update user in Supabase
            await this.createOrUpdateUser(userAttributes);
            
            // Redirect to dashboard
            this.showSuccess('SSO authentication successful!');
            setTimeout(() => {
                window.location.href = '/teacher-dashboard.html';
            }, 2000);
            
        } catch (error) {
            console.error('SAML response processing error:', error);
            this.showError('SSO authentication failed. Please try again.');
        }
    }

    extractUserAttributes(xmlDoc) {
        const attributes = {};
        
        // Extract email
        const emailElement = xmlDoc.querySelector('Attribute[Name="email"] AttributeValue');
        if (emailElement) {
            attributes.email = emailElement.textContent;
        }
        
        // Extract name
        const nameElement = xmlDoc.querySelector('Attribute[Name="name"] AttributeValue');
        if (nameElement) {
            attributes.name = nameElement.textContent;
        }
        
        // Extract role
        const roleElement = xmlDoc.querySelector('Attribute[Name="role"] AttributeValue');
        if (roleElement) {
            attributes.role = roleElement.textContent;
        }
        
        // Extract department
        const departmentElement = xmlDoc.querySelector('Attribute[Name="department"] AttributeValue');
        if (departmentElement) {
            attributes.department = departmentElement.textContent;
        }
        
        return attributes;
    }

    async createOrUpdateUser(attributes) {
        try {
            // Initialize Supabase
            const supabase = window.supabase.createClient(
                window.ENV.SUPABASE_URL,
                window.ENV.SUPABASE_ANON_KEY
            );

            // Check if user exists
            const { data: existingUser } = await supabase
                .from('profiles')
                .select('*')
                .eq('email', attributes.email)
                .single();

            if (existingUser) {
                // Update existing user
                const { error } = await supabase
                    .from('profiles')
                    .update({
                        name: attributes.name,
                        role: attributes.role,
                        department: attributes.department,
                        last_login: new Date().toISOString(),
                        sso_provider: 'saml'
                    })
                    .eq('email', attributes.email);

                if (error) throw error;
            } else {
                // Create new user
                const { error } = await supabase
                    .from('profiles')
                    .insert({
                        email: attributes.email,
                        name: attributes.name,
                        role: attributes.role,
                        department: attributes.department,
                        sso_provider: 'saml',
                        created_at: new Date().toISOString()
                    });

                if (error) throw error;
            }
            
        } catch (error) {
            console.error('User creation/update error:', error);
            throw error;
        }
    }

    setupSchoolManagement() {
        // School admin dashboard
        this.setupSchoolAdminFeatures();
        this.setupBulkOperations();
        this.setupUserManagement();
    }

    setupSchoolAdminFeatures() {
        // School configuration
        document.addEventListener('submit', (e) => {
            const schoolConfigForm = e.target.closest('#school-config-form');
            if (schoolConfigForm) {
                e.preventDefault();
                this.handleSchoolConfiguration(schoolConfigForm);
            }
        });
    }

    async handleSchoolConfiguration(form) {
        try {
            const formData = new FormData(form);
            const schoolData = {
                name: formData.get('schoolName'),
                ssoUrl: formData.get('ssoUrl'),
                entityId: formData.get('entityId'),
                certificate: formData.get('certificate'),
                contactEmail: formData.get('contactEmail')
            };

            // Save school configuration
            const supabase = window.supabase.createClient(
                window.ENV.SUPABASE_URL,
                window.ENV.SUPABASE_ANON_KEY
            );

            const { error } = await supabase
                .from('school_configurations')
                .insert(schoolData);

            if (error) throw error;

            this.showSuccess('School configuration saved successfully!');
            
        } catch (error) {
            console.error('School configuration error:', error);
            this.showError('Failed to save school configuration. Please try again.');
        }
    }

    setupBulkOperations() {
        // Bulk user import
        document.addEventListener('change', (e) => {
            if (e.target.matches('#bulk-user-import')) {
                this.handleBulkUserImport(e.target.files[0]);
            }
        });
    }

    async handleBulkUserImport(file) {
        try {
            const csvContent = await this.readFileAsText(file);
            const users = this.parseCSV(csvContent);
            
            // Import users to Supabase
            const supabase = window.supabase.createClient(
                window.ENV.SUPABASE_URL,
                window.ENV.SUPABASE_ANON_KEY
            );

            const { error } = await supabase
                .from('profiles')
                .insert(users);

            if (error) throw error;

            this.showSuccess(`${users.length} users imported successfully!`);
            
        } catch (error) {
            console.error('Bulk import error:', error);
            this.showError('Failed to import users. Please check the CSV format.');
        }
    }

    setupUserManagement() {
        // User role management
        document.addEventListener('click', (e) => {
            if (e.target.matches('.role-update-btn')) {
                const userId = e.target.getAttribute('data-user-id');
                const newRole = e.target.getAttribute('data-new-role');
                this.updateUserRole(userId, newRole);
            }
        });
    }

    async updateUserRole(userId, newRole) {
        try {
            const supabase = window.supabase.createClient(
                window.ENV.SUPABASE_URL,
                window.ENV.SUPABASE_ANON_KEY
            );

            const { error } = await supabase
                .from('profiles')
                .update({ role: newRole })
                .eq('id', userId);

            if (error) throw error;

            this.showSuccess('User role updated successfully!');
            
        } catch (error) {
            console.error('Role update error:', error);
            this.showError('Failed to update user role. Please try again.');
        }
    }

    // Helper methods
    generateRequestId() {
        return 'req_' + Math.random().toString(36).substr(2, 9);
    }

    readFileAsText(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = (e) => resolve(e.target.result);
            reader.onerror = reject;
            reader.readAsText(file);
        });
    }

    parseCSV(csvContent) {
        const lines = csvContent.split('\n');
        const headers = lines[0].split(',');
        const users = [];
        
        for (let i = 1; i < lines.length; i++) {
            const values = lines[i].split(',');
            if (values.length === headers.length) {
                const user = {};
                headers.forEach((header, index) => {
                    user[header.trim()] = values[index].trim();
                });
                users.push(user);
            }
        }
        
        return users;
    }

    showSuccess(message) {
        this.showNotification(message, 'success');
    }

    showError(message) {
        this.showNotification(message, 'error');
    }

    showNotification(message, type) {
        const notification = document.createElement('div');
        notification.className = `fixed top-4 right-4 p-4 rounded-lg shadow-lg z-50 ${
            type === 'success' ? 'bg-green-500 text-white' : 'bg-red-500 text-white'
        }`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 5000);
    }
}

// Initialize SSO when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => new TeKeteSSO());
} else {
    new TeKeteSSO();
}

// Export for global access
window.TeKeteSSO = TeKeteSSO;
