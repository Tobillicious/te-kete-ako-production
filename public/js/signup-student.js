/**
 * ================================================================
 * STUDENT SIGN-UP FORM - TE KETE AKO
 * NZ Education Platform - Multi-Step Registration
 * ================================================================
 */

// Wait for Supabase client to be ready
let supabaseClient = null;

window.addEventListener('supabaseReady', (event) => {
    supabaseClient = event.detail.client;
});

// Multi-step form state
let currentStep = 1;
const totalSteps = 4;
const formData = {};

// DOM Elements
const form = document.getElementById('studentSignupForm');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const submitBtn = document.getElementById('submitBtn');
const formMessage = document.getElementById('formMessage');
const schoolSelect = document.getElementById('schoolName');
const otherSchoolGroup = document.getElementById('otherSchoolGroup');

// Initialize form
document.addEventListener('DOMContentLoaded', () => {
    // Show/hide "other school" input
    schoolSelect.addEventListener('change', () => {
        if (schoolSelect.value === 'other') {
            otherSchoolGroup.style.display = 'block';
            document.getElementById('otherSchool').required = true;
        } else {
            otherSchoolGroup.style.display = 'none';
            document.getElementById('otherSchool').required = false;
        }
    });
    
    // Button event listeners
    nextBtn.addEventListener('click', () => nextStep());
    prevBtn.addEventListener('click', () => previousStep());
    form.addEventListener('submit', (e) => handleSubmit(e));
    
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
    document.querySelector(`.form-step[data-step="${step}"]`).classList.add('active');
    document.querySelector(`.step[data-step="${step}"]`).classList.add('active');
    
    // Mark completed steps
    for (let i = 1; i < step; i++) {
        document.querySelector(`.step[data-step="${i}"]`).classList.add('completed');
    }
    
    // Update button visibility
    prevBtn.style.display = step === 1 ? 'none' : 'inline-block';
    nextBtn.style.display = step === totalSteps ? 'none' : 'inline-block';
    submitBtn.style.display = step === totalSteps ? 'inline-block' : 'none';
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

/**
 * Validate current step
 */
function validateStep(step) {
    const currentStepElement = document.querySelector(`.form-step[data-step="${step}"]`);
    const inputs = currentStepElement.querySelectorAll('input[required], select[required]');
    
    let isValid = true;
    let errorMessage = '';
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.style.borderColor = 'var(--color-error)';
            errorMessage = 'Please fill in all required fields';
        } else {
            input.style.borderColor = 'var(--color-neutral-300)';
        }
    });
    
    // Step-specific validation
    if (step === 1) {
        // Validate passwords match
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirmPassword').value;
        
        if (password !== confirmPassword) {
            isValid = false;
            errorMessage = 'Passwords do not match';
            document.getElementById('confirmPassword').style.borderColor = 'var(--color-error)';
        }
        
        // Validate password length
        if (password.length < 8) {
            isValid = false;
            errorMessage = 'Password must be at least 8 characters';
            document.getElementById('password').style.borderColor = 'var(--color-error)';
        }
        
        // Validate email format
        const email = document.getElementById('email').value;
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            isValid = false;
            errorMessage = 'Please enter a valid email address';
            document.getElementById('email').style.borderColor = 'var(--color-error)';
        }
    }
    
    if (step === 4) {
        // Validate terms accepted
        if (!document.getElementById('termsAccepted').checked || 
            !document.getElementById('dataConsent').checked) {
            isValid = false;
            errorMessage = 'You must accept the terms and data consent to continue';
        }
    }
    
    if (!isValid) {
        showMessage(errorMessage, 'error');
    } else {
        hideMessage();
    }
    
    return isValid;
}

/**
 * Move to next step
 */
function nextStep() {
    if (validateStep(currentStep)) {
        // Save current step data
        saveStepData(currentStep);
        
        currentStep++;
        showStep(currentStep);
    }
}

/**
 * Move to previous step
 */
function previousStep() {
    currentStep--;
    showStep(currentStep);
}

/**
 * Save step data to formData object
 */
function saveStepData(step) {
    const currentStepElement = document.querySelector(`.form-step[data-step="${step}"]`);
    const inputs = currentStepElement.querySelectorAll('input, select');
    
    inputs.forEach(input => {
        if (input.type === 'checkbox') {
            formData[input.name] = input.checked;
        } else if (input.type === 'select-multiple') {
            const selected = Array.from(input.selectedOptions).map(opt => opt.value);
            formData[input.name] = selected;
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
    
    if (!validateStep(currentStep)) {
        return;
    }
    
    // Save final step data
    saveStepData(currentStep);
    
    // Show loading
    submitBtn.disabled = true;
    submitBtn.textContent = '🔄 Creating your account...';
    
    try {
        // Check if Supabase is ready
        if (!supabaseClient) {
            throw new Error('Authentication system not ready. Please refresh the page.');
        }
        
        // Prepare user data
        const schoolName = formData.schoolName === 'other' ? 
            formData.otherSchool : formData.schoolName;
        
        // Create auth user
        const { data: authData, error: authError } = await supabaseClient.auth.signUp({
            email: formData.email,
            password: formData.password,
            options: {
                data: {
                    first_name: formData.firstName,
                    last_name: formData.lastName,
                    role: 'student'
                },
                emailRedirectTo: `${window.location.origin}/student-portal.html`
            }
        });
        
        if (authError) throw authError;
        
        // Create profile with NZ-specific data
        const { error: profileError } = await supabaseClient
            .from('profiles')
            .insert({
                user_id: authData.user.id,
                email: formData.email,
                role: 'student',
                first_name: formData.firstName,
                last_name: formData.lastName,
                display_name: `${formData.firstName} ${formData.lastName}`,
                school_name: schoolName,
                year_level: parseInt(formData.yearLevel),
                date_of_birth: formData.dateOfBirth || null,
                gender: formData.gender || null,
                cultural_identity: formData.culturalIdentity || [],
                iwi_affiliation: formData.iwiAffiliation || null,
                preferred_language: formData.preferredLanguage || 'English',
                parent_email: formData.parentEmail || null,
                consent_given: formData.dataConsent,
                terms_accepted_at: new Date().toISOString(),
                personalization_settings: {
                    email_updates: formData.emailUpdates || false
                },
                onboarding_completed: false
            });
        
        if (profileError) throw profileError;
        
        // Success!
        showMessage('🎉 Account created successfully! Please check your email to verify your account.', 'success');
        
        // Redirect after 3 seconds
        setTimeout(() => {
            window.location.href = '/login.html?registered=true';
        }, 3000);
        
    } catch (error) {
        console.error('Signup error:', error);
        showMessage(`Error: ${error.message}`, 'error');
        
        submitBtn.disabled = false;
        submitBtn.textContent = '🎉 Create Account';
    }
}

/**
 * Show message
 */
function showMessage(message, type) {
    formMessage.textContent = message;
    formMessage.className = type;
    formMessage.style.display = 'block';
}

/**
 * Hide message
 */
function hideMessage() {
    formMessage.style.display = 'none';
}

/**
 * Log form data for debugging (remove in production)
 */
window.debugFormData = () => {
};

