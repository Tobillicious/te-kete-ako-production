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

// Smart school search using Google Places API
let schoolSearchTimeout;
let selectedSchoolData = null;

async function initializeSchoolSearch() {
    const schoolInput = document.getElementById('school_name');
    const suggestionsDiv = document.getElementById('school_suggestions');
    
    if (!schoolInput) return;
    
    // Search as user types
    schoolInput.addEventListener('input', (e) => {
        const query = e.target.value.trim();
        
        if (query.length < 3) {
            suggestionsDiv.classList.remove('active');
            return;
        }
        
        // Debounce search
        clearTimeout(schoolSearchTimeout);
        schoolSearchTimeout = setTimeout(() => {
            searchNZSchools(query);
        }, 300);
    });
    
    // Hide suggestions when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.school-search-wrapper')) {
            suggestionsDiv.classList.remove('active');
        }
    });
}

// Search NZ schools using Google-style search
async function searchNZSchools(query) {
    const suggestionsDiv = document.getElementById('school_suggestions');
    
    // Show loading state
    suggestionsDiv.innerHTML = '<div class="school-loading">🔍 Searching NZ schools...</div>';
    suggestionsDiv.classList.add('active');
    
    try {
        // First, search our local database (fast!)
        const { data: localResults } = await supabase
            .from('nz_schools')
            .select('name, region, school_type')
            .ilike('name', `%${query}%`)
            .limit(10);
        
        // If we have results, show them
        if (localResults && localResults.length > 0) {
            displaySchoolSuggestions(localResults);
        } else {
            // No local results - show "type to add" option
            suggestionsDiv.innerHTML = `
                <div class="school-suggestion-item" onclick="selectCustomSchool('${escapeHtml(query)}')">
                    <div class="school-name">➕ "${escapeHtml(query)}"</div>
                    <div class="school-details">Add this school to our database</div>
                </div>
                <div class="school-loading" style="font-size: 0.8rem; padding: 1rem;">
                    💡 Can't find it? Just type the full name and we'll add it!
                </div>
            `;
        }
    } catch (error) {
        console.error('School search error:', error);
        suggestionsDiv.innerHTML = '<div class="school-loading">❌ Search error. Just type your school name.</div>';
    }
}

// Display school suggestions
function displaySchoolSuggestions(schools) {
    const suggestionsDiv = document.getElementById('school_suggestions');
    
    if (schools.length === 0) {
        suggestionsDiv.classList.remove('active');
        return;
    }
    
    suggestionsDiv.innerHTML = schools.map(school => `
        <div class="school-suggestion-item" onclick='selectSchool(${JSON.stringify(school)})'>
            <div class="school-name">${escapeHtml(school.name)}</div>
            <div class="school-details">${escapeHtml(school.region || 'Region unknown')} • ${escapeHtml(school.school_type || 'Secondary')}</div>
        </div>
    `).join('');
    
    // Add "or type to add new" option at bottom
    const inputValue = document.getElementById('school_name').value;
    suggestionsDiv.innerHTML += `
        <div class="school-suggestion-item" onclick="selectCustomSchool('${escapeHtml(inputValue)}')" style="border-top: 2px solid var(--color-border);">
            <div class="school-name">➕ Add "${escapeHtml(inputValue)}" as new school</div>
            <div class="school-details">If your school isn't listed above</div>
        </div>
    `;
    
    suggestionsDiv.classList.add('active');
}

// Select school from suggestions
function selectSchool(schoolData) {
    document.getElementById('school_name').value = schoolData.name;
    document.getElementById('school_region').value = schoolData.region || '';
    document.getElementById('school_type').value = schoolData.school_type || '';
    document.getElementById('school_suggestions').classList.remove('active');
    
    selectedSchoolData = schoolData;
}

// Select custom school (not in database)
function selectCustomSchool(schoolName) {
    document.getElementById('school_name').value = schoolName;
    document.getElementById('school_region').value = 'To be confirmed';
    document.getElementById('school_type').value = 'To be confirmed';
    document.getElementById('school_suggestions').classList.remove('active');
    
    selectedSchoolData = { name: schoolName, region: 'To be confirmed', school_type: 'To be confirmed' };
}

// HTML escape utility
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Legacy function - keep for backwards compatibility
async function loadNZSchools() {
    // Initialize school search instead
    initializeSchoolSearch();
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
            
            // Validate password strength (Supabase requirements)
            if (password.length < 8) {
                showStepMessage('Password must be at least 8 characters', 'error', 1);
                return false;
            }
            
            if (!/[a-z]/.test(password)) {
                showStepMessage('Password must contain at least one lowercase letter', 'error', 1);
                return false;
            }
            
            if (!/[A-Z]/.test(password)) {
                showStepMessage('Password must contain at least one uppercase letter', 'error', 1);
                return false;
            }
            
            if (!/[0-9]/.test(password)) {
                showStepMessage('Password must contain at least one number', 'error', 1);
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
                
                if (subjects.length === 0 || yearLevels.length === 0) {
                    showStepMessage('Please select at least one subject and one year level', 'error', 3);
                    return false;
                }
                
                formData.schoolName = school || 'Not specified';
                formData.subjects = subjects;
                formData.yearLevels = yearLevels;
                formData.teacherRole = document.getElementById('teacher_role').value;
                
                // Save school data for profile
                formData.schoolRegion = document.getElementById('school_region').value || '';
                formData.schoolType = document.getElementById('school_type').value || '';
                
                // Add new school to database if it's not in our list
                if (school && school.trim() !== '') {
                    addSchoolIfNew(
                        school.trim(),
                        formData.schoolRegion || 'To be confirmed',
                        formData.schoolType || 'To be confirmed'
                    );
                }
                
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
        // Use the fixed registration function if available
        if (window.authFixes && window.authFixes.fixedRegistrationSubmit) {
            console.log('Using fixed registration method...');
            const result = await window.authFixes.fixedRegistrationSubmit(formData);
            
            if (result.success) {
                if (result.requiresEmailVerification) {
                    showStepMessage(
                        '📧 Account created! Redirecting to email verification...',
                        'success',
                        5
                    );
                    
                    setTimeout(() => {
                        window.location.href = `/verify-email.html?email=${encodeURIComponent(formData.email)}`;
                    }, 2000);
                } else {
                    showStepMessage('Account created successfully! Redirecting to your kete...', 'success', 5);
                    
                    setTimeout(() => {
                        window.location.href = '/my-kete.html';
                    }, 2000);
                }
                return;
            }
        }
        
        // Fallback to original method
        console.log('Using original registration method...');
        
        // 1. Ensure role is valid
        if (!formData.role || !['teacher', 'student', 'admin'].includes(formData.role)) {
            throw new Error('Invalid role specified. Must be teacher, student, or admin.');
        }
        
        // 2. Create Supabase auth user
        const { data: authData, error: authError } = await supabase.auth.signUp({
            email: formData.email,
            password: formData.password,
            options: {
                data: {
                    full_name: formData.fullName,
                    role: formData.role,
                    school_name: formData.schoolName || 'Mangakōtukutuku College'
                }
            }
        });
        
        if (authError) {
            console.error('Auth signup error:', authError);
            throw authError;
        }
        
        if (!authData.user) {
            throw new Error('Registration failed - no user created');
        }
        
        console.log('User created successfully:', authData.user.id);
        
        // 3. Wait a moment for any potential triggers to run
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        // 4. Check if profile already exists (in case trigger worked)
        const { data: existingProfile } = await supabase
            .from('profiles')
            .select('*')
            .eq('user_id', authData.user.id)
            .single();
            
        if (existingProfile) {
            console.log('Profile already exists from trigger:', existingProfile);
            
            if (authData.session) {
                showStepMessage('Account created successfully! Redirecting to your kete...', 'success', 5);
                setTimeout(() => {
                    window.location.href = '/my-kete.html';
                }, 2000);
            } else {
                showStepMessage(
                    '📧 Account created! Redirecting to email verification...',
                    'success',
                    5
                );
                setTimeout(() => {
                    window.location.href = `/verify-email.html?email=${encodeURIComponent(formData.email)}`;
                }, 2000);
            }
            return;
        }
        
        // 5. No profile exists, create it manually
        console.log('Creating profile manually...');
        
        // Set session first so RLS policies work
        if (authData.session) {
            await supabase.auth.setSession({
                access_token: authData.session.access_token,
                refresh_token: authData.session.refresh_token
            });
        } else {
            // No session - likely email confirmation required
            showStepMessage(
                '📧 Account created! Redirecting to email verification...',
                'success',
                5
            );
            
            // Redirect to verify-email page with email param
            setTimeout(() => {
                window.location.href = `/verify-email.html?email=${encodeURIComponent(formData.email)}`;
            }, 2000);
            return; // Stop here - can't create profile without session
        }
        
        // 6. Create comprehensive profile
        const profileData = {
            user_id: authData.user.id,
            email: formData.email,
            role: formData.role,  // Ensure this is exactly 'teacher', 'student', or 'admin'
            display_name: formData.fullName,
            school_name: formData.schoolName || formData.studentSchool || 'Mangakōtukutuku College',
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
        
        console.log('Attempting to create profile with data:', profileData);
        
        // 7. Insert profile into database
        const { data: profileResult, error: profileError } = await supabase
            .from('profiles')
            .insert(profileData)
            .select()
            .single();
            
        if (profileError) {
            console.error('Profile creation error:', profileError);
            
            // If profile creation fails, clean up the auth user
            await supabase.auth.signOut();
            
            throw new Error(`Profile creation failed: ${profileError.message}`);
        }
        
        console.log('Profile created successfully:', profileResult);
        
        // 8. Success! Show message and redirect
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

// Add new school to database if not already there
async function addSchoolIfNew(schoolName, region = 'To be confirmed', schoolType = 'To be confirmed') {
    try {
        // Check if school exists
        const { data: existing } = await supabase
            .from('nz_schools')
            .select('name')
            .eq('name', schoolName)
            .single();
        
        if (!existing) {
            // Add new school (crowd-sourced!)
            await supabase
                .from('nz_schools')
                .insert([{
                    name: schoolName,
                    region: region,
                    school_type: schoolType
                }]);
        }
    } catch (error) {
        // Silently fail - not critical for registration
        console.error('Could not add school:', error);
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

