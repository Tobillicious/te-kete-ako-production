/**
 * ================================================================
 * FIREBASE AUTHENTICATION - TE KETE AKO
 * ================================================================
 * 
 * Unified Firebase auth system replacing all legacy auth scripts
 * Features: Login, Signup, Email Verification, Password Reset
 * Integrates with Supabase GRAPHRAG via Netlify functions
 * 
 * ================================================================
 */

import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-app.js";
import { 
    getAuth, 
    createUserWithEmailAndPassword,
    signInWithEmailAndPassword,
    signOut,
    sendEmailVerification,
    sendPasswordResetEmail,
    onAuthStateChanged,
    updateProfile
} from "https://www.gstatic.com/firebasejs/11.0.1/firebase-auth.js";

// Firebase configuration - replace with your actual project settings
// Get these from Firebase Console > Project Settings > General
const firebaseConfig = {
    apiKey: "YOUR_API_KEY", // Safe to expose publicly
    authDomain: "te-kete-ako.firebaseapp.com",
    projectId: "te-kete-ako",
    storageBucket: "te-kete-ako.appspot.com", 
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Global auth state
let currentUser = null;

/**
 * Display error messages inline
 */
function showError(message, elementId = 'error-message') {
    const errorElement = document.getElementById(elementId);
    if (errorElement) {
        errorElement.textContent = message;
        errorElement.style.display = 'block';
        errorElement.className = 'error-message show';
    } else {
        console.error(message);
        alert(message); // Fallback
    }
}

/**
 * Display success messages
 */
function showSuccess(message, elementId = 'success-message') {
    const successElement = document.getElementById(elementId);
    if (successElement) {
        successElement.textContent = message;
        successElement.style.display = 'block';
        successElement.className = 'success-message show';
    } else {
        alert(message); // Fallback
    }
}

/**
 * Clear all messages
 */
function clearMessages() {
    const errorElement = document.getElementById('error-message');
    const successElement = document.getElementById('success-message');
    
    if (errorElement) {
        errorElement.style.display = 'none';
        errorElement.textContent = '';
    }
    if (successElement) {
        successElement.style.display = 'none';
        successElement.textContent = '';
    }
}

/**
 * Show loading state for buttons
 */
function setLoadingState(buttonId, isLoading) {
    const button = document.getElementById(buttonId);
    if (button) {
        if (isLoading) {
            button.disabled = true;
            button.dataset.originalText = button.textContent;
            button.textContent = 'Loading...';
        } else {
            button.disabled = false;
            button.textContent = button.dataset.originalText || button.textContent;
        }
    }
}

/**
 * Register new user with email and password
 */
async function handleSignup(email, password, confirmPassword, displayName, role = 'student') {
    clearMessages();
    
    // Validation
    if (!email || !password || !displayName) {
        showError('Please fill in all required fields.');
        return;
    }
    
    if (password !== confirmPassword) {
        showError('Passwords do not match.');
        return;
    }
    
    if (password.length < 6) {
        showError('Password must be at least 6 characters long.');
        return;
    }
    
    setLoadingState('signup-btn', true);
    
    try {
        // Create user account
        const userCredential = await createUserWithEmailAndPassword(auth, email, password);
        const user = userCredential.user;
        
        // Update user profile with display name and role
        await updateProfile(user, {
            displayName: displayName,
        });
        
        // Send email verification
        await sendEmailVerification(user);
        
        // Store role in custom claims (would need Firebase Admin SDK for production)
        // For now, we'll handle role in Netlify function
        
        showSuccess('Account created successfully! Please check your email to verify your account.');
        
        // Redirect to verification page after short delay
        setTimeout(() => {
            window.location.href = '/verify-email.html';
        }, 2000);
        
    } catch (error) {
        console.error('Signup error:', error);
        let errorMessage = 'Failed to create account. ';
        
        switch (error.code) {
            case 'auth/email-already-in-use':
                errorMessage += 'This email is already registered.';
                break;
            case 'auth/invalid-email':
                errorMessage += 'Please enter a valid email address.';
                break;
            case 'auth/weak-password':
                errorMessage += 'Password is too weak. Please choose a stronger password.';
                break;
            default:
                errorMessage += error.message;
        }
        
        showError(errorMessage);
    } finally {
        setLoadingState('signup-btn', false);
    }
}

/**
 * Sign in existing user
 */
async function handleLogin(email, password) {
    clearMessages();
    
    if (!email || !password) {
        showError('Please enter both email and password.');
        return;
    }
    
    setLoadingState('login-btn', true);
    
    try {
        const userCredential = await signInWithEmailAndPassword(auth, email, password);
        const user = userCredential.user;
        
        // Check if email is verified
        if (!user.emailVerified) {
            showError('Please verify your email before signing in. Check your inbox for the verification link.');
            await signOut(auth);
            return;
        }
        
        // Successful login - redirect based on user role
        // You could store role in custom claims or fetch from Supabase
        window.location.href = '/my-kete.html';
        
    } catch (error) {
        console.error('Login error:', error);
        let errorMessage = 'Failed to sign in. ';
        
        switch (error.code) {
            case 'auth/user-not-found':
            case 'auth/wrong-password':
                errorMessage += 'Invalid email or password.';
                break;
            case 'auth/invalid-email':
                errorMessage += 'Please enter a valid email address.';
                break;
            case 'auth/too-many-requests':
                errorMessage += 'Too many failed attempts. Please try again later.';
                break;
            default:
                errorMessage += error.message;
        }
        
        showError(errorMessage);
    } finally {
        setLoadingState('login-btn', false);
    }
}

/**
 * Sign out current user
 */
async function handleLogout() {
    try {
        await signOut(auth);
        window.location.href = '/login.html';
    } catch (error) {
        console.error('Logout error:', error);
        showError('Failed to sign out. Please try again.');
    }
}

/**
 * Send password reset email
 */
async function handlePasswordReset(email) {
    clearMessages();
    
    if (!email) {
        showError('Please enter your email address.');
        return;
    }
    
    setLoadingState('reset-btn', true);
    
    try {
        await sendPasswordResetEmail(auth, email);
        showSuccess('Password reset email sent! Check your inbox for further instructions.');
        
    } catch (error) {
        console.error('Password reset error:', error);
        let errorMessage = 'Failed to send password reset email. ';
        
        switch (error.code) {
            case 'auth/user-not-found':
                errorMessage += 'No account found with this email address.';
                break;
            case 'auth/invalid-email':
                errorMessage += 'Please enter a valid email address.';
                break;
            default:
                errorMessage += error.message;
        }
        
        showError(errorMessage);
    } finally {
        setLoadingState('reset-btn', false);
    }
}

/**
 * Get current user ID token for API calls
 */
async function getCurrentUserToken() {
    if (currentUser) {
        return await currentUser.getIdToken();
    }
    return null;
}

/**
 * Fetch data from Netlify function with auth token
 */
async function fetchWithAuth(url, options = {}) {
    const token = await getCurrentUserToken();
    if (!token) {
        throw new Error('User not authenticated');
    }
    
    const headers = {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
        ...options.headers
    };
    
    return fetch(url, {
        ...options,
        headers
    });
}

/**
 * Auth state listener
 */
onAuthStateChanged(auth, (user) => {
    currentUser = user;
    
    if (user) {
        console.log('User signed in:', user.email);
        document.body.classList.add('logged-in');
        document.body.classList.remove('logged-out');
        
        // Update UI elements
        updateAuthUI(user);
        
    } else {
        console.log('User signed out');
        document.body.classList.add('logged-out');
        document.body.classList.remove('logged-in');
        
        // Clear UI
        updateAuthUI(null);
    }
});

/**
 * Update UI based on auth state
 */
function updateAuthUI(user) {
    // Update navigation
    const loginLinks = document.querySelectorAll('.login-link');
    const logoutLinks = document.querySelectorAll('.logout-link');
    const userDisplays = document.querySelectorAll('.user-display');
    
    if (user) {
        // Show logout, hide login
        loginLinks.forEach(link => link.style.display = 'none');
        logoutLinks.forEach(link => link.style.display = 'block');
        
        // Show user info
        userDisplays.forEach(display => {
            display.textContent = user.displayName || user.email;
            display.style.display = 'block';
        });
        
    } else {
        // Show login, hide logout
        loginLinks.forEach(link => link.style.display = 'block');
        logoutLinks.forEach(link => link.style.display = 'none');
        
        // Hide user info
        userDisplays.forEach(display => {
            display.style.display = 'none';
        });
    }
}

/**
 * Initialize event listeners
 */
document.addEventListener('DOMContentLoaded', () => {
    // Login form
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            handleLogin(email, password);
        });
    }
    
    // Signup form
    const signupForm = document.getElementById('signup-form');
    if (signupForm) {
        signupForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirm-password').value;
            const displayName = document.getElementById('display-name').value;
            const role = document.getElementById('role')?.value || 'student';
            handleSignup(email, password, confirmPassword, displayName, role);
        });
    }
    
    // Password reset form
    const resetForm = document.getElementById('reset-form');
    if (resetForm) {
        resetForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            handlePasswordReset(email);
        });
    }
    
    // Logout buttons
    const logoutButtons = document.querySelectorAll('.logout-btn');
    logoutButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            handleLogout();
        });
    });
});

// Export functions for global use
window.TeKeteAuth = {
    handleLogin,
    handleSignup,
    handleLogout,
    handlePasswordReset,
    getCurrentUserToken,
    fetchWithAuth,
    auth,
    currentUser: () => currentUser
};

console.log('🔥 Firebase Auth initialized for Te Kete Ako');