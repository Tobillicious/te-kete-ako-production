/**
 * Email Verification Banner
 * Shows a dismissible banner when user hasn't verified their email
 */

async function checkAndShowVerificationBanner() {
    try {
        const { data: { user } } = await supabase.auth.getUser();
        
        if (!user) return; // Not logged in
        
        // Check if email is verified
        const emailVerified = user.email_confirmed_at !== null;
        
        if (!emailVerified && !sessionStorage.getItem('verification_banner_dismissed')) {
            showVerificationBanner(user.email);
        }
    } catch (error) {
        console.error('Error checking verification status:', error);
    }
}

function showVerificationBanner(email) {
    // Check if banner already exists
    if (document.getElementById('verification-banner')) return;
    
    const banner = document.createElement('div');
    banner.id = 'verification-banner';
    banner.className = 'verification-banner';
    banner.innerHTML = `
        <div class="verification-banner-content">
            <div class="verification-banner-icon">📧</div>
            <div class="verification-banner-text">
                <strong>Please verify your email address</strong>
                <p>We sent a verification link to <strong>${escapeHtml(email)}</strong>. 
                   Check your inbox to unlock full features.</p>
            </div>
            <div class="verification-banner-actions">
                <button onclick="resendVerificationEmail()" class="btn-resend">
                    Resend Email
                </button>
                <button onclick="dismissVerificationBanner()" class="btn-dismiss" title="Dismiss">
                    ✕
                </button>
            </div>
        </div>
    `;
    
    // Insert at top of page (after header)
    const header = document.querySelector('.site-header');
    if (header) {
        header.after(banner);
    } else {
        document.body.insertBefore(banner, document.body.firstChild);
    }
}

async function resendVerificationEmail() {
    try {
        const { error } = await supabase.auth.resend({
            type: 'signup',
            email: (await supabase.auth.getUser()).data.user.email
        });
        
        if (error) throw error;
        
        // Show success message
        const banner = document.getElementById('verification-banner');
        const textDiv = banner.querySelector('.verification-banner-text');
        textDiv.innerHTML = `
            <strong>✅ Verification email sent!</strong>
            <p>Check your inbox (and spam folder) for the verification link.</p>
        `;
        
        setTimeout(() => {
            dismissVerificationBanner();
        }, 5000);
        
    } catch (error) {
        console.error('Error resending verification email:', error);
        alert('Failed to resend email. Please try again later.');
    }
}

function dismissVerificationBanner() {
    const banner = document.getElementById('verification-banner');
    if (banner) {
        banner.style.animation = 'slideUp 0.3s ease-out';
        setTimeout(() => {
            banner.remove();
            sessionStorage.setItem('verification_banner_dismissed', 'true');
        }, 300);
    }
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Add CSS styles
const style = document.createElement('style');
style.textContent = `
    .verification-banner {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        position: sticky;
        top: 0;
        z-index: 9998;
        animation: slideDown 0.3s ease-out;
    }
    
    .verification-banner-content {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        align-items: center;
        gap: 1rem;
        flex-wrap: wrap;
    }
    
    .verification-banner-icon {
        font-size: 2rem;
        flex-shrink: 0;
    }
    
    .verification-banner-text {
        flex: 1;
        min-width: 300px;
    }
    
    .verification-banner-text strong {
        display: block;
        font-size: 1.1rem;
        margin-bottom: 0.25rem;
    }
    
    .verification-banner-text p {
        margin: 0;
        opacity: 0.95;
        font-size: 0.95rem;
    }
    
    .verification-banner-actions {
        display: flex;
        gap: 0.5rem;
        align-items: center;
    }
    
    .btn-resend {
        background: white;
        color: #667eea;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    
    .btn-resend:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .btn-dismiss {
        background: rgba(255,255,255,0.2);
        color: white;
        border: none;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        font-size: 1.2rem;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    
    .btn-dismiss:hover {
        background: rgba(255,255,255,0.3);
    }
    
    @keyframes slideDown {
        from {
            transform: translateY(-100%);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
    
    @keyframes slideUp {
        from {
            transform: translateY(0);
            opacity: 1;
        }
        to {
            transform: translateY(-100%);
            opacity: 0;
        }
    }
    
    @media (max-width: 768px) {
        .verification-banner-content {
            flex-direction: column;
            text-align: center;
        }
        
        .verification-banner-actions {
            width: 100%;
            justify-content: center;
        }
    }
    
    @media print {
        .verification-banner {
            display: none !important;
        }
    }
`;
document.head.appendChild(style);

// Check on page load
if (typeof supabase !== 'undefined') {
    checkAndShowVerificationBanner();
} else {
    // Wait for Supabase to load
    setTimeout(checkAndShowVerificationBanner, 500);
}

// Export for use in other scripts
window.emailVerification = {
    checkAndShowVerificationBanner,
    dismissVerificationBanner,
    resendVerificationEmail
};

