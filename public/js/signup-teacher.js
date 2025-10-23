/**
 * ================================================================
 * TEACHER SIGN-UP FORM - TE KETE AKO
 * NZ Education Platform - Multi-Step Professional Registration
 * ================================================================
 */

// Wait for Supabase client to be ready
let supabaseClient = null;

window.addEventListener('supabaseReady', (event) => {
    supabaseClient = event.detail.client;
});

// Multi-step form state
let currentStep = 1;
const totalSteps = 5;
const formData = {};

// DOM Elements
const form = document.getElementById('teacherSignupForm');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const submitBtn = document.getElementById('submitBtn');
const formMessage = document.getElementById('formMessage');
const schoolSelect = document.getElementById('schoolName');
const otherSchoolGroup = document.getElementById('otherSchoolGroup');

// Initialize form
document.addEventListener('DOMContentLoaded', () => {
    // Show/hide "other school" input
    if (schoolSelect) {
        schoolSelect.addEventListener('change', () => {
            if (schoolSelect.value === 'other') {
                otherSchoolGroup.style.display = 'block';
                document.getElementById('otherSchool').required = true;
            } else {
                otherSchoolGroup.style.display = 'none';
                document.getElementById('otherSchool').required = false;
            }
        });
    }
    
    // Button event listeners
    if (nextBtn) nextBtn.addEventListener('click', () => nextStep());
    if (prevBtn) prevBtn.addEventListener('click', () => previousStep());
    if (form) form.addEventListener('submit', (e) => handleSubmit(e));
    
    // Initialize step display
    showStep(currentStep);
});

/**
 * Show specific step
 */
function showStep(step) {
    // Hide all steps
    document.querySelectorAll('.form-step').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.step').forEach(s => {
        s.classList.remove('active', 'completed');
    });
    
    // Show current step
    const currentFormStep = document.querySelector(`.form-step[data-step="${step}"]`);
    if (currentFormStep) currentFormStep.classList.add('active');
    
    // Update progress indicators
    document.querySelectorAll('.step').forEach((s, index) => {
        if (index + 1 < step) {
            s.classList.add('completed');
        } else if (index + 1 === step) {
            s.classList.add('active');
        }
    });
    
    // Update buttons
    if (prevBtn) prevBtn.style.display = step === 1 ? 'none' : 'inline-block';
    if (nextBtn) nextBtn.style.display = step === totalSteps ? 'none' : 'inline-block';
    if (submitBtn) submitBtn.style.display = step === totalSteps ? 'inline-block' : 'none';
    
    // Update button text
    if (nextBtn && step === totalSteps - 1) {
        nextBtn.textContent = 'Review →';
    } else if (nextBtn) {
        nextBtn.textContent = 'Next →';
    }
}

/**
 * Next step
 */
function nextStep() {
    // Validate current step
    const currentFormStep = document.querySelector(`.form-step[data-step="${currentStep}"]`);
    const inputs = currentFormStep.querySelectorAll('input[required], select[required], textarea[required]');
    
    let valid = true;
    inputs.forEach(input => {
        if (!input.value || (input.type === 'checkbox' && !input.checked)) {
            valid = false;
            input.style.borderColor = '#dc2626';
        } else {
            input.style.borderColor = 'var(--color-neutral-300)';
        }
    });
    
    if (!valid) {
        showMessage('Please fill in all required fields', 'error');
        return;
    }
    
    // Save current step data
    saveStepData(currentStep);
    
    // Move to next step
    if (currentStep < totalSteps) {
        currentStep++;
        showStep(currentStep);
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
}

/**
 * Previous step
 */
function previousStep() {
    if (currentStep > 1) {
        currentStep--;
        showStep(currentStep);
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
}

/**
 * Save step data to formData object
 */
function saveStepData(step) {
    const stepElement = document.querySelector(`.form-step[data-step="${step}"]`);
    const inputs = stepElement.querySelectorAll('input, select, textarea');
    
    inputs.forEach(input => {
        if (input.type === 'checkbox') {
            if (input.checked) {
                if (!formData[input.name]) formData[input.name] = [];
                formData[input.name].push(input.value);
            }
        } else if (input.type === 'radio') {
            if (input.checked) {
                formData[input.name] = input.value;
            }
        } else {
            formData[input.name] = input.value;
        }
    });
}

/**
 * Handle form submission
 */
async function handleSubmit(e) {
    e.preventDefault();
    
    // Save final step data
    saveStepData(currentStep);
    
    if (!supabaseClient) {
        showMessage('Authentication system not ready. Please refresh and try again.', 'error');
        return;
    }
    
    // Show loading
    if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '⏳ Creating your account...';
    }
    
    try {
        // 1. Create auth user
        const { data: authData, error: authError } = await supabaseClient.auth.signUp({
            email: formData.email,
            password: formData.password,
            options: {
                data: {
                    first_name: formData.firstName,
                    last_name: formData.lastName,
                    role: 'teacher'
                }
            }
        });
        
        if (authError) throw authError;
        
        // 2. Create/update profile
        const { error: profileError } = await supabaseClient
            .from('profiles')
            .upsert({
                user_id: authData.user.id,
                email: formData.email,
                role: 'teacher',
                first_name: formData.firstName,
                last_name: formData.lastName,
                title: formData.title,
                display_name: `${formData.title} ${formData.firstName} ${formData.lastName}`,
                school_name: formData.schoolName === 'other' ? formData.otherSchool : formData.schoolName,
                teacher_registration_number: formData.teacherRegistration,
                teacher_role: formData.teachingRole,
                subjects_taught: formData.subjectsTaught ? JSON.parse(JSON.stringify(formData.subjectsTaught)) : null,
                year_levels_taught: formData.yearLevelsTaught ? JSON.parse(JSON.stringify(formData.yearLevelsTaught)) : null,
                kamar_school_code: formData.kamarCode || null,
                kamar_sync_enabled: formData.kamarSync === 'yes',
                personalization_settings: {
                    newsletter: formData.newsletter === 'yes',
                    professional_development: formData.professionalDev === 'yes',
                    resource_notifications: formData.resourceNotifications === 'yes'
                },
                onboarding_completed: false,
                created_at: new Date().toISOString(),
                updated_at: new Date().toISOString()
            });
        
        if (profileError) throw profileError;
        
        // 3. Success!
        showMessage('🎉 Account created successfully! Redirecting to your dashboard...', 'success');
        
        // 4. Redirect to dashboard
        setTimeout(() => {
            window.location.href = '/teachers/dashboard.html';
        }, 2000);
        
    } catch (error) {
        console.error('Signup error:', error);
        showMessage(`Error: ${error.message}. Please try again.`, 'error');
        
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerHTML = 'Create Account →';
        }
    }
}

/**
 * Show message to user
 */
function showMessage(message, type = 'info') {
    if (!formMessage) return;
    
    formMessage.textContent = message;
    formMessage.style.display = 'block';
    
    if (type === 'error') {
        formMessage.style.background = '#fee2e2';
        formMessage.style.color = '#991b1b';
        formMessage.style.border = '1px solid #fca5a5';
    } else if (type === 'success') {
        formMessage.style.background = '#d1fae5';
        formMessage.style.color = '#065f46';
        formMessage.style.border = '1px solid #6ee7b7';
    } else {
        formMessage.style.background = '#dbeafe';
        formMessage.style.color = '#1e40af';
        formMessage.style.border = '1px solid #93c5fd';
    }
    
    // Auto-hide after 5 seconds for non-errors
    if (type !== 'error') {
        setTimeout(() => {
            formMessage.style.display = 'none';
        }, 5000);
    }
}

/**
 * Validate email format
 */
function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

/**
 * Validate password strength
 */
function isStrongPassword(password) {
    // At least 8 characters, 1 uppercase, 1 lowercase, 1 number
    return password.length >= 8 &&
           /[A-Z]/.test(password) &&
           /[a-z]/.test(password) &&
           /[0-9]/.test(password);
}

/**
 * Auto-save form data to localStorage (recovery feature)
 */
function autoSave() {
    localStorage.setItem('teacherSignupDraft', JSON.stringify(formData));
}

/**
 * Load saved draft
 */
function loadDraft() {
    const draft = localStorage.getItem('teacherSignupDraft');
    if (draft) {
        const confirmed = confirm('We found a saved draft of your registration. Would you like to continue where you left off?');
        if (confirmed) {
            Object.assign(formData, JSON.parse(draft));
            // TODO: Populate form fields with saved data
        }
    }
}

// Initialize draft loading
setTimeout(loadDraft, 500);

/**
 * Clear draft after successful submission
 */
function clearDraft() {
    localStorage.removeItem('teacherSignupDraft');
}

/**
 * Handle step validation specific to teacher fields
 */
function validateTeacherStep(step) {
    switch(step) {
        case 1: // Basic Info
            if (!formData.email || !isValidEmail(formData.email)) {
                showMessage('Please enter a valid email address', 'error');
                return false;
            }
            if (!formData.password || !isStrongPassword(formData.password)) {
                showMessage('Password must be at least 8 characters with uppercase, lowercase, and number', 'error');
                return false;
            }
            if (formData.password !== document.getElementById('confirmPassword')?.value) {
                showMessage('Passwords do not match', 'error');
                return false;
            }
            break;
            
        case 2: // Professional Info
            if (!formData.teacherRegistration || formData.teacherRegistration.length < 5) {
                showMessage('Please enter a valid teacher registration number', 'error');
                return false;
            }
            break;
            
        case 3: // Teaching Details
            if (!formData.subjectsTaught || formData.subjectsTaught.length === 0) {
                showMessage('Please select at least one subject you teach', 'error');
                return false;
            }
            if (!formData.yearLevelsTaught || formData.yearLevelsTaught.length === 0) {
                showMessage('Please select at least one year level you teach', 'error');
                return false;
            }
            break;
    }
    
    return true;
}

// Console log for debugging
