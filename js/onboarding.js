// onboarding.js
// Multi-step registration flow for Te Kete Ako

let currentStep = 1;
let selectedRole = null;
let formData = {};
let nzSchools = [];

// Initialize onboarding
document.addEventListener('DOMContentLoaded', async () => {
    await loadNZSchools();
    initializeForm();
});

// Load NZ schools from Supabase
async function loadNZSchools() {
    try {
        const { data, error } = await supabase
            .from('nz_schools')
            .select('name, region, school_type')
            .order('name');
        
        if (!error && data) {
            nzSchools = data;
            populateSchoolsList();
        }
    } catch (error) {
        console.error('Error loading schools:', error);
    }
}

// Populate schools datalist
function populateSchoolsList() {
    const datalist = document.getElementById('schools-list');
    if (!datalist) return;
    
    nzSchools.forEach(school => {
        const option = document.createElement('option');
        option.value = school.name;
        option.textContent = `${school.name} (${school.region})`;
        datalist.appendChild(option);
    });
}

// Initialize form event listeners
function initializeForm() {
    const form = document.getElementById('onboarding-form');
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        await submitRegistration();
    });
    
    // Password confirmation validation
    const password = document.getElementById('password');
    const passwordConfirm = document.getElementById('password_confirm');
    
    passwordConfirm.addEventListener('input', () => {
        if (password.value !== passwordConfirm.value) {
            passwordConfirm.setCustomValidity('Passwords do not match');
        } else {
            passwordConfirm.setCustomValidity('');
        }
    });
}

// Navigate to next step
function nextStep(stepNumber) {
    // Validate current step
    if (!validateCurrentStep()) {
        return;
    }
    
    // Update progress
    updateProgress(currentStep, stepNumber);
    
    // Show new step
    document.querySelectorAll('.onboarding-step').forEach(step => {
        step.classList.remove('active');
    });
    
    const nextStepEl = document.querySelector(`.onboarding-step[data-step="${stepNumber}"]`);
    if (nextStepEl) {
        nextStepEl.classList.add('active');
    }
    
    currentStep = stepNumber;
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Navigate to previous step
function prevStep(stepNumber) {
    updateProgress(currentStep, stepNumber);
    
    document.querySelectorAll('.onboarding-step').forEach(step => {
        step.classList.remove('active');
    });
    
    const prevStepEl = document.querySelector(`.onboarding-step[data-step="${stepNumber}"]`);
    if (prevStepEl) {
        prevStepEl.classList.add('active');
    }
    
    currentStep = stepNumber;
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Update progress indicator
function updateProgress(fromStep, toStep) {
    // Mark completed steps
    document.querySelectorAll('.progress-step').forEach((step, index) => {
        const stepNum = index + 1;
        
        if (stepNum < toStep) {
            step.classList.add('completed');
            step.classList.remove('active');
        } else if (stepNum === toStep) {
            step.classList.add('active');
            step.classList.remove('completed');
        } else {
            step.classList.remove('active', 'completed');
        }
    });
}

// Validate current step
function validateCurrentStep() {
    const messageDiv = document.getElementById(`step${currentStep}-message`);
    
    switch (currentStep) {
        case 1:
            const fullName = document.getElementById('full_name').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const passwordConfirm = document.getElementById('password_confirm').value;
            
            if (!fullName || !email || !password) {
                showStepMessage('Please fill in all required fields', 'error', 1);
                return false;
            }
            
            if (password.length < 6) {
                showStepMessage('Password must be at least 6 characters', 'error', 1);
                return false;
            }
            
            if (password !== passwordConfirm) {
                showStepMessage('Passwords do not match', 'error', 1);
                return false;
            }
            
            // Save to formData
            formData.fullName = fullName;
            formData.email = email;
            formData.password = password;
            return true;
            
        case 2:
            if (!selectedRole) {
                showStepMessage('Please select your role', 'error', 2);
                return false;
            }
            formData.role = selectedRole;
            return true;
            
        case 3:
            if (selectedRole === 'teacher') {
                const school = document.getElementById('school_name').value;
                const subjects = Array.from(document.querySelectorAll('input[name="subjects"]:checked'))
                    .map(cb => cb.value);
                const yearLevels = Array.from(document.querySelectorAll('input[name="year_levels"]:checked'))
                    .map(cb => parseInt(cb.value));
                
                if (!school || subjects.length === 0 || yearLevels.length === 0) {
                    showStepMessage('Please complete all required fields (school, subjects, year levels)', 'error', 3);
                    return false;
                }
                
                formData.schoolName = school;
                formData.subjects = subjects;
                formData.yearLevels = yearLevels;
                formData.teacherRole = document.getElementById('teacher_role').value;
                
            } else if (selectedRole === 'student') {
                const yearLevel = document.getElementById('student_year_level').value;
                
                if (!yearLevel) {
                    showStepMessage('Please select your year level', 'error', 3);
                    return false;
                }
                
                formData.yearLevel = parseInt(yearLevel);
                formData.studentSchool = document.getElementById('student_school').value;
                formData.parentEmail = document.getElementById('parent_email').value;
            }
            return true;
            
        case 4:
            // Step 4 is optional, collect data if provided
            formData.culturalIdentity = document.getElementById('cultural_identity').value;
            formData.iwiAffiliation = document.getElementById('iwi_affiliation').value;
            formData.preferredLanguage = document.getElementById('preferred_language').value || 'English';
            return true;
            
        case 5:
            const termsAccepted = document.getElementById('terms_accepted').checked;
            const privacyAccepted = document.getElementById('privacy_accepted').checked;
            
            if (!termsAccepted || !privacyAccepted) {
                showStepMessage('You must accept the Terms and Privacy Policy to continue', 'error', 5);
                return false;
            }
            
            formData.marketingConsent = document.getElementById('marketing_consent').checked;
            return true;
            
        default:
            return true;
    }
}

// Show step-specific message
function showStepMessage(message, type, step) {
    const messageDiv = document.getElementById(`step${step}-message`);
    if (!messageDiv) return;
    
    messageDiv.textContent = message;
    messageDiv.className = `message ${type}`;
    messageDiv.style.display = 'block';
    
    // Auto-hide after 5 seconds
    setTimeout(() => {
        messageDiv.style.display = 'none';
    }, 5000);
}

// Select role (teacher/student)
function selectRole(role) {
    selectedRole = role;
    
    // Update UI
    document.querySelectorAll('.role-card').forEach(card => {
        card.classList.remove('selected');
    });
    document.querySelector(`.role-card[data-role="${role}"]`).classList.add('selected');
    
    // Set hidden input
    document.getElementById('role').value = role;
    
    // Enable next button
    document.getElementById('role-next-btn').disabled = false;
    
    // Show/hide appropriate profile steps
    document.querySelectorAll('.onboarding-step[data-step="3"]').forEach(step => {
        if (step.dataset.role === role) {
            step.style.display = 'block';
        } else {
            step.style.display = 'none';
        }
    });
}

// Next step from role selection
function nextStepFromRole() {
    if (!selectedRole) {
        showStepMessage('Please select your role', 'error', 2);
        return;
    }
    nextStep(3);
}

// Submit registration to Supabase
async function submitRegistration() {
    const submitBtn = document.getElementById('submit-btn');
    const submitSpinner = document.getElementById('submit-spinner');
    const submitText = document.getElementById('submit-text');
    
    // Show loading state
    submitBtn.disabled = true;
    submitSpinner.style.display = 'inline-block';
    submitText.textContent = 'Creating your account...';
    
    try {
        // 1. Create Supabase auth user
        const { data: authData, error: authError } = await supabase.auth.signUp({
            email: formData.email,
            password: formData.password,
            options: {
                data: {
                    full_name: formData.fullName,
                    role: formData.role
                }
            }
        });
        
        if (authError) throw authError;
        
        const userId = authData.user.id;
        
        // 2. Create comprehensive profile
        const profileData = {
            user_id: userId,
            email: formData.email,
            role: formData.role,
            display_name: formData.fullName,
            school_name: formData.schoolName || formData.studentSchool || null,
            preferred_language: formData.preferredLanguage || 'English',
            onboarding_completed: true,
            terms_accepted_at: new Date().toISOString()
        };
        
        // Add role-specific fields
        if (formData.role === 'teacher') {
            profileData.teacher_role = formData.teacherRole || null;
            profileData.subjects_taught = formData.subjects || [];
            profileData.year_levels_taught = formData.yearLevels || [];
        } else if (formData.role === 'student') {
            profileData.year_level = formData.yearLevel;
            profileData.parent_email = formData.parentEmail || null;
        }
        
        // Add cultural fields (if provided)
        if (formData.culturalIdentity) {
            // Split by comma and trim
            const identities = formData.culturalIdentity
                .split(',')
                .map(i => i.trim())
                .filter(i => i.length > 0);
            profileData.cultural_identity = identities;
        }
        
        if (formData.iwiAffiliation) {
            profileData.iwi_affiliation = formData.iwiAffiliation;
        }
        
        // 3. Insert profile into database
        const { error: profileError } = await supabase
            .from('profiles')
            .insert([profileData]);
        
        if (profileError) {
            console.error('Profile creation error:', profileError);
            throw new Error('Account created but profile setup failed. Please contact support.');
        }
        
        // 4. Success! Show message and redirect
        showStepMessage('Account created successfully! Redirecting to your kete...', 'success', 5);
        
        setTimeout(() => {
            window.location.href = '/my-kete.html';
        }, 2000);
        
    } catch (error) {
        console.error('Registration error:', error);
        showStepMessage(error.message || 'Registration failed. Please try again.', 'error', 5);
        
        // Reset button
        submitBtn.disabled = false;
        submitSpinner.style.display = 'none';
        submitText.textContent = '🧺 Create My Account';
    }
}

// Check if user is already logged in
window.addEventListener('load', async () => {
    const { data: { user } } = await supabase.auth.getUser();
    if (user) {
        // User is already logged in, redirect
        window.location.href = '/index.html';
    }
});

