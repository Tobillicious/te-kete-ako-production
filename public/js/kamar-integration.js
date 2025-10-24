/**
 * KAMAR Integration - Te Kete Ako
 * School management system integration for seamless data flow
 * Phase 3 of Tech Stack Evolution
 */

class TeKeteKAMAR {
    constructor() {
        this.kamarApi = null;
        this.schoolConfig = null;
        this.init();
    }

    async init() {
        await this.loadKAMARSDK();
        this.setupKAMARConnection();
        this.setupStudentSync();
        this.setupClassSync();
        this.setupAssessmentSync();
    }

    async loadKAMARSDK() {
        // Load KAMAR API SDK
        if (window.KAMAR) {
            this.kamarApi = window.KAMAR;
            return;
        }

        return new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = 'https://api.kamar.co.nz/sdk/v1/kamar.min.js';
            script.onload = () => {
                this.kamarApi = window.KAMAR;
                resolve();
            };
            script.onerror = reject;
            document.head.appendChild(script);
        });
    }

    setupKAMARConnection() {
        // KAMAR school configurations
        this.schoolConfigs = {
            'auckland-grammar': {
                schoolId: 'AGS001',
                apiKey: 'kamar_ags_2024_key',
                baseUrl: 'https://ags.kamar.co.nz/api/v1',
                features: ['student_sync', 'class_sync', 'assessment_sync', 'attendance_sync']
            },
            'wellington-college': {
                schoolId: 'WC001',
                apiKey: 'kamar_wc_2024_key',
                baseUrl: 'https://wellington.kamar.co.nz/api/v1',
                features: ['student_sync', 'class_sync', 'assessment_sync']
            },
            'christchurch-boys': {
                schoolId: 'CBHS001',
                apiKey: 'kamar_cbhs_2024_key',
                baseUrl: 'https://cbhs.kamar.co.nz/api/v1',
                features: ['student_sync', 'class_sync', 'attendance_sync']
            }
        };
    }

    setupStudentSync() {
        // Sync students from KAMAR to Te Kete Ako
        document.addEventListener('click', (e) => {
            if (e.target.matches('#sync-students-btn')) {
                this.syncStudents();
            }
        });

        // Auto-sync on page load
        this.autoSyncStudents();
    }

    async syncStudents() {
        try {
            this.showLoading('Syncing students from KAMAR...');
            
            const schools = Object.keys(this.schoolConfigs);
            let totalSynced = 0;

            for (const schoolId of schools) {
                const config = this.schoolConfigs[schoolId];
                const students = await this.fetchStudentsFromKAMAR(config);
                await this.syncStudentsToSupabase(students, schoolId);
                totalSynced += students.length;
            }

            this.showSuccess(`${totalSynced} students synced successfully!`);
            
        } catch (error) {
            console.error('Student sync error:', error);
            this.showError('Failed to sync students. Please try again.');
        }
    }

    async fetchStudentsFromKAMAR(config) {
        try {
            const response = await fetch(`${config.baseUrl}/students`, {
                headers: {
                    'Authorization': `Bearer ${config.apiKey}`,
                    'Content-Type': 'application/json'
                }
            });

            if (!response.ok) {
                throw new Error(`KAMAR API error: ${response.status}`);
            }

            const data = await response.json();
            return data.students || [];
            
        } catch (error) {
            console.error('KAMAR API error:', error);
            throw error;
        }
    }

    async syncStudentsToSupabase(students, schoolId) {
        try {
            const supabase = await window.supabaseSingleton.getClient();

            for (const student of students) {
                // Check if student exists
                const { data: existingStudent } = await supabase
                    .from('students')
                    .select('*')
                    .eq('kamar_id', student.id)
                    .single();

                const studentData = {
                    kamar_id: student.id,
                    student_number: student.studentNumber,
                    first_name: student.firstName,
                    last_name: student.lastName,
                    email: student.email,
                    year_level: student.yearLevel,
                    form_class: student.formClass,
                    school_id: schoolId,
                    last_sync: new Date().toISOString()
                };

                if (existingStudent) {
                    // Update existing student
                    await supabase
                        .from('students')
                        .update(studentData)
                        .eq('kamar_id', student.id);
                } else {
                    // Create new student
                    await supabase
                        .from('students')
                        .insert(studentData);
                }
            }
            
        } catch (error) {
            console.error('Supabase sync error:', error);
            throw error;
        }
    }

    setupClassSync() {
        // Sync classes from KAMAR
        document.addEventListener('click', (e) => {
            if (e.target.matches('#sync-classes-btn')) {
                this.syncClasses();
            }
        });
    }

    async syncClasses() {
        try {
            this.showLoading('Syncing classes from KAMAR...');
            
            const schools = Object.keys(this.schoolConfigs);
            let totalSynced = 0;

            for (const schoolId of schools) {
                const config = this.schoolConfigs[schoolId];
                const classes = await this.fetchClassesFromKAMAR(config);
                await this.syncClassesToSupabase(classes, schoolId);
                totalSynced += classes.length;
            }

            this.showSuccess(`${totalSynced} classes synced successfully!`);
            
        } catch (error) {
            console.error('Class sync error:', error);
            this.showError('Failed to sync classes. Please try again.');
        }
    }

    async fetchClassesFromKAMAR(config) {
        try {
            const response = await fetch(`${config.baseUrl}/classes`, {
                headers: {
                    'Authorization': `Bearer ${config.apiKey}`,
                    'Content-Type': 'application/json'
                }
            });

            if (!response.ok) {
                throw new Error(`KAMAR API error: ${response.status}`);
            }

            const data = await response.json();
            return data.classes || [];
            
        } catch (error) {
            console.error('KAMAR API error:', error);
            throw error;
        }
    }

    async syncClassesToSupabase(classes, schoolId) {
        try {
            const supabase = await window.supabaseSingleton.getClient();

            for (const classData of classes) {
                const classInfo = {
                    kamar_id: classData.id,
                    class_code: classData.classCode,
                    class_name: classData.className,
                    subject: classData.subject,
                    year_level: classData.yearLevel,
                    teacher_id: classData.teacherId,
                    school_id: schoolId,
                    last_sync: new Date().toISOString()
                };

                // Check if class exists
                const { data: existingClass } = await supabase
                    .from('classes')
                    .select('*')
                    .eq('kamar_id', classData.id)
                    .single();

                if (existingClass) {
                    // Update existing class
                    await supabase
                        .from('classes')
                        .update(classInfo)
                        .eq('kamar_id', classData.id);
                } else {
                    // Create new class
                    await supabase
                        .from('classes')
                        .insert(classInfo);
                }
            }
            
        } catch (error) {
            console.error('Supabase sync error:', error);
            throw error;
        }
    }

    setupAssessmentSync() {
        // Sync assessments from KAMAR
        document.addEventListener('click', (e) => {
            if (e.target.matches('#sync-assessments-btn')) {
                this.syncAssessments();
            }
        });
    }

    async syncAssessments() {
        try {
            this.showLoading('Syncing assessments from KAMAR...');
            
            const schools = Object.keys(this.schoolConfigs);
            let totalSynced = 0;

            for (const schoolId of schools) {
                const config = this.schoolConfigs[schoolId];
                const assessments = await this.fetchAssessmentsFromKAMAR(config);
                await this.syncAssessmentsToSupabase(assessments, schoolId);
                totalSynced += assessments.length;
            }

            this.showSuccess(`${totalSynced} assessments synced successfully!`);
            
        } catch (error) {
            console.error('Assessment sync error:', error);
            this.showError('Failed to sync assessments. Please try again.');
        }
    }

    async fetchAssessmentsFromKAMAR(config) {
        try {
            const response = await fetch(`${config.baseUrl}/assessments`, {
                headers: {
                    'Authorization': `Bearer ${config.apiKey}`,
                    'Content-Type': 'application/json'
                }
            });

            if (!response.ok) {
                throw new Error(`KAMAR API error: ${response.status}`);
            }

            const data = await response.json();
            return data.assessments || [];
            
        } catch (error) {
            console.error('KAMAR API error:', error);
            throw error;
        }
    }

    async syncAssessmentsToSupabase(assessments, schoolId) {
        try {
            const supabase = window.supabase.createClient(
                window.ENV.SUPABASE_URL,
                window.ENV.SUPABASE_ANON_KEY
            );

            for (const assessment of assessments) {
                const assessmentData = {
                    kamar_id: assessment.id,
                    assessment_name: assessment.name,
                    subject: assessment.subject,
                    year_level: assessment.yearLevel,
                    due_date: assessment.dueDate,
                    class_id: assessment.classId,
                    school_id: schoolId,
                    last_sync: new Date().toISOString()
                };

                // Check if assessment exists
                const { data: existingAssessment } = await supabase
                    .from('assessments')
                    .select('*')
                    .eq('kamar_id', assessment.id)
                    .single();

                if (existingAssessment) {
                    // Update existing assessment
                    await supabase
                        .from('assessments')
                        .update(assessmentData)
                        .eq('kamar_id', assessment.id);
                } else {
                    // Create new assessment
                    await supabase
                        .from('assessments')
                        .insert(assessmentData);
                }
            }
            
        } catch (error) {
            console.error('Supabase sync error:', error);
            throw error;
        }
    }

    // Auto-sync functionality
    async autoSyncStudents() {
        // Auto-sync every 24 hours
        setInterval(() => {
            this.syncStudents();
        }, 24 * 60 * 60 * 1000);
    }

    // Real-time sync for specific events
    setupRealTimeSync() {
        // Listen for KAMAR webhooks
        document.addEventListener('kamar-student-updated', (e) => {
            this.syncSpecificStudent(e.detail.studentId);
        });

        document.addEventListener('kamar-class-updated', (e) => {
            this.syncSpecificClass(e.detail.classId);
        });
    }

    async syncSpecificStudent(studentId) {
        try {
            // Find which school this student belongs to
            const schools = Object.keys(this.schoolConfigs);
            
            for (const schoolId of schools) {
                const config = this.schoolConfigs[schoolId];
                const student = await this.fetchStudentFromKAMAR(config, studentId);
                
                if (student) {
                    await this.syncStudentsToSupabase([student], schoolId);
                    break;
                }
            }
            
        } catch (error) {
            console.error('Specific student sync error:', error);
        }
    }

    async fetchStudentFromKAMAR(config, studentId) {
        try {
            const response = await fetch(`${config.baseUrl}/students/${studentId}`, {
                headers: {
                    'Authorization': `Bearer ${config.apiKey}`,
                    'Content-Type': 'application/json'
                }
            });

            if (!response.ok) {
                return null;
            }

            const data = await response.json();
            return data.student;
            
        } catch (error) {
            console.error('KAMAR API error:', error);
            return null;
        }
    }

    // KAMAR data export to Te Kete Ako
    async exportKAMARData() {
        try {
            this.showLoading('Exporting KAMAR data...');
            
            const schools = Object.keys(this.schoolConfigs);
            const exportData = {};

            for (const schoolId of schools) {
                const config = this.schoolConfigs[schoolId];
                const students = await this.fetchStudentsFromKAMAR(config);
                const classes = await this.fetchClassesFromKAMAR(config);
                const assessments = await this.fetchAssessmentsFromKAMAR(config);

                exportData[schoolId] = {
                    students: students,
                    classes: classes,
                    assessments: assessments,
                    exportDate: new Date().toISOString()
                };
            }

            // Download as JSON
            const blob = new Blob([JSON.stringify(exportData, null, 2)], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `kamar-export-${new Date().toISOString().split('T')[0]}.json`;
            a.click();
            URL.revokeObjectURL(url);

            this.showSuccess('KAMAR data exported successfully!');
            
        } catch (error) {
            console.error('Export error:', error);
            this.showError('Failed to export KAMAR data. Please try again.');
        }
    }

    // Helper methods
    showLoading(message) {
        const loading = document.createElement('div');
        loading.id = 'kamar-loading';
        loading.className = 'fixed top-4 right-4 p-4 bg-blue-500 text-white rounded-lg shadow-lg z-50';
        loading.textContent = message;
        document.body.appendChild(loading);
    }

    hideLoading() {
        const loading = document.getElementById('kamar-loading');
        if (loading) {
            loading.remove();
        }
    }

    showSuccess(message) {
        this.hideLoading();
        this.showNotification(message, 'success');
    }

    showError(message) {
        this.hideLoading();
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

// Initialize KAMAR integration when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => new TeKeteKAMAR());
} else {
    new TeKeteKAMAR();
}

// Export for global access
window.TeKeteKAMAR = TeKeteKAMAR;
