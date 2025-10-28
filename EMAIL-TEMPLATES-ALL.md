# 📧 ALL SUPABASE EMAIL TEMPLATES - Te Kete Ako

Beautiful, branded email templates for all Supabase authentication emails.

**Design:** Teal-to-gold gradient header, culturally grounded whakataukī, professional footer

---

## 1️⃣ CONFIRM SIGNUP (Already done yesterday!)

Template name in Supabase: **"Confirm signup"**

```html
[The template you provided - already in Supabase]
```

---

## 2️⃣ RESET PASSWORD

Template name in Supabase: **"Reset Password"**

See: `EMAIL-TEMPLATE-PASSWORD-RESET.html`

---

## 3️⃣ INVITE USER

Template name in Supabase: **"Invite user"**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Merriweather:ital,wght@0,300;0,400&display=swap');
        
        body {
            margin: 0;
            padding: 0;
            font-family: 'Lato', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background-color: #f8f9fa;
            color: #2c3e50;
            line-height: 1.6;
        }
        .email-container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
        }
        .header {
            background: linear-gradient(135deg, #1e6b7a 0%, #2d8a99 50%, #d4af37 100%);
            padding: 2rem;
            text-align: center;
        }
        .logo {
            font-size: 3rem;
            margin-bottom: 0.5rem;
        }
        .brand {
            color: white;
            font-size: 1.5rem;
            font-weight: 700;
            margin: 0;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        .content {
            padding: 2rem;
        }
        .greeting {
            font-size: 1.3rem;
            color: #1e6b7a;
            margin: 0 0 1rem 0;
            font-weight: 700;
        }
        .message {
            font-size: 1rem;
            color: #2c3e50;
            margin-bottom: 1.5rem;
        }
        .button-container {
            text-align: center;
            margin: 2rem 0;
        }
        .confirm-button {
            background: linear-gradient(135deg, #1e6b7a 0%, #2d8a99 50%, #d4af37 100%);
            color: white !important;
            padding: 14px 36px;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 700;
            font-size: 1rem;
            display: inline-block;
            box-shadow: 0 4px 6px rgba(30, 107, 122, 0.3);
        }
        .link-fallback {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #2d8a99;
            margin: 1.5rem 0;
            font-size: 0.9rem;
            color: #6c757d;
        }
        .link-fallback a {
            color: #1e6b7a;
            word-break: break-all;
        }
        .whakatauki {
            background: linear-gradient(135deg, #e8f4f8 0%, #fff9e6 100%);
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid #d4af37;
            margin: 2rem 0;
            text-align: center;
        }
        .whakatauki-text {
            font-family: 'Merriweather', serif;
            font-style: italic;
            color: #1e6b7a;
            font-size: 1.1rem;
            margin: 0 0 0.5rem 0;
        }
        .whakatauki-translation {
            color: #2d8a99;
            font-size: 0.95rem;
            margin: 0;
        }
        .footer {
            background: #2c3e50;
            color: white;
            padding: 2rem;
            text-align: center;
        }
        .footer-brand {
            font-size: 1.2rem;
            font-weight: 700;
            margin: 0 0 0.5rem 0;
        }
        .footer-tagline {
            font-size: 0.9rem;
            color: #95a5a6;
            margin: 0 0 1rem 0;
        }
        .footer-link {
            color: #d4af37;
            text-decoration: none;
            font-weight: 600;
        }
        .disclaimer {
            color: #95a5a6;
            font-size: 0.8rem;
            margin-top: 1.5rem;
            padding-top: 1rem;
            border-top: 1px solid #34495e;
        }
    </style>
</head>
<body>
    <div class="email-container">
        <!-- Header -->
        <div class="header">
            <div class="logo">🎉</div>
            <h1 class="brand">You're Invited!</h1>
        </div>

        <!-- Main Content -->
        <div class="content">
            <h2 class="greeting">Kia ora!</h2>
            
            <p class="message">
                You've been invited to join <strong>Te Kete Ako</strong> - your basket of teaching resources for Aotearoa New Zealand!
            </p>
            
            <p class="message">
                Access 140+ culturally-grounded teaching resources designed by educators, for educators.
            </p>

            <div class="button-container">
                <a href="{{ .ConfirmationURL }}" class="confirm-button">
                    ✅ Accept Invitation
                </a>
            </div>

            <div class="link-fallback">
                <strong>Button not working?</strong><br>
                Copy and paste this link into your browser:<br>
                <a href="{{ .ConfirmationURL }}">{{ .ConfirmationURL }}</a>
            </div>

            <!-- Whakataukī -->
            <div class="whakatauki">
                <p class="whakatauki-text">"Whaowhia te kete mātauranga"</p>
                <p class="whakatauki-translation">Fill the basket of knowledge</p>
            </div>
        </div>

        <!-- Footer -->
        <div class="footer">
            <p class="footer-brand">🧺 Te Kete Ako</p>
            <p class="footer-tagline">Aotearoa New Zealand</p>
            <a href="https://tekete.co.nz" class="footer-link">tekete.co.nz</a>
            
            <p class="disclaimer">
                If you didn't expect this invitation, you can safely ignore this email.
            </p>
        </div>
    </div>
</body>
</html>
```

---

## 4️⃣ MAGIC LINK

Template name in Supabase: **"Magic Link"**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Merriweather:ital,wght@0,300;0,400&display=swap');
        
        body {
            margin: 0;
            padding: 0;
            font-family: 'Lato', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background-color: #f8f9fa;
            color: #2c3e50;
            line-height: 1.6;
        }
        .email-container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
        }
        .header {
            background: linear-gradient(135deg, #1e6b7a 0%, #2d8a99 50%, #d4af37 100%);
            padding: 2rem;
            text-align: center;
        }
        .logo {
            font-size: 3rem;
            margin-bottom: 0.5rem;
        }
        .brand {
            color: white;
            font-size: 1.5rem;
            font-weight: 700;
            margin: 0;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        .content {
            padding: 2rem;
        }
        .greeting {
            font-size: 1.3rem;
            color: #1e6b7a;
            margin: 0 0 1rem 0;
            font-weight: 700;
        }
        .message {
            font-size: 1rem;
            color: #2c3e50;
            margin-bottom: 1.5rem;
        }
        .security-warning {
            background: #fff3cd;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #d4af37;
            margin: 1.5rem 0;
        }
        .security-warning strong {
            color: #856404;
        }
        .button-container {
            text-align: center;
            margin: 2rem 0;
        }
        .confirm-button {
            background: linear-gradient(135deg, #1e6b7a 0%, #2d8a99 50%, #d4af37 100%);
            color: white !important;
            padding: 14px 36px;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 700;
            font-size: 1rem;
            display: inline-block;
            box-shadow: 0 4px 6px rgba(30, 107, 122, 0.3);
        }
        .link-fallback {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #2d8a99;
            margin: 1.5rem 0;
            font-size: 0.9rem;
            color: #6c757d;
        }
        .link-fallback a {
            color: #1e6b7a;
            word-break: break-all;
        }
        .whakatauki {
            background: linear-gradient(135deg, #e8f4f8 0%, #fff9e6 100%);
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid #d4af37;
            margin: 2rem 0;
            text-align: center;
        }
        .whakatauki-text {
            font-family: 'Merriweather', serif;
            font-style: italic;
            color: #1e6b7a;
            font-size: 1.1rem;
            margin: 0 0 0.5rem 0;
        }
        .whakatauki-translation {
            color: #2d8a99;
            font-size: 0.95rem;
            margin: 0;
        }
        .footer {
            background: #2c3e50;
            color: white;
            padding: 2rem;
            text-align: center;
        }
        .footer-brand {
            font-size: 1.2rem;
            font-weight: 700;
            margin: 0 0 0.5rem 0;
        }
        .footer-tagline {
            font-size: 0.9rem;
            color: #95a5a6;
            margin: 0 0 1rem 0;
        }
        .footer-link {
            color: #d4af37;
            text-decoration: none;
            font-weight: 600;
        }
        .disclaimer {
            color: #95a5a6;
            font-size: 0.8rem;
            margin-top: 1.5rem;
            padding-top: 1rem;
            border-top: 1px solid #34495e;
        }
    </style>
</head>
<body>
    <div class="email-container">
        <!-- Header -->
        <div class="header">
            <div class="logo">✨</div>
            <h1 class="brand">Your Magic Link</h1>
        </div>

        <!-- Main Content -->
        <div class="content">
            <h2 class="greeting">Kia ora {{ .Email }}!</h2>
            
            <p class="message">
                Click the link below to sign in to <strong>Te Kete Ako</strong> without a password!
            </p>

            <div class="security-warning">
                <strong>⚠️ Security Notice:</strong><br>
                This magic link expires in <strong>1 hour</strong>. If you didn't request this, you can safely ignore this email.
            </div>

            <div class="button-container">
                <a href="{{ .ConfirmationURL }}" class="confirm-button">
                    🔐 Sign In to Te Kete Ako
                </a>
            </div>

            <div class="link-fallback">
                <strong>Button not working?</strong><br>
                Copy and paste this link into your browser:<br>
                <a href="{{ .ConfirmationURL }}">{{ .ConfirmationURL }}</a>
            </div>

            <!-- Whakataukī -->
            <div class="whakatauki">
                <p class="whakatauki-text">"He aha te mea nui o te ao? He tangata, he tangata, he tangata"</p>
                <p class="whakatauki-translation">What is the most important thing in the world? It is people, it is people, it is people</p>
            </div>
        </div>

        <!-- Footer -->
        <div class="footer">
            <p class="footer-brand">🧺 Te Kete Ako</p>
            <p class="footer-tagline">Aotearoa New Zealand</p>
            <a href="https://tekete.co.nz" class="footer-link">tekete.co.nz</a>
            
            <p class="disclaimer">
                This is an automated security email for passwordless authentication.
            </p>
        </div>
    </div>
</body>
</html>
```

---

## 5️⃣ CHANGE EMAIL ADDRESS

Template name in Supabase: **"Change Email Address"**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Merriweather:ital,wght@0,300;0,400&display=swap');
        
        body {
            margin: 0;
            padding: 0;
            font-family: 'Lato', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background-color: #f8f9fa;
            color: #2c3e50;
            line-height: 1.6;
        }
        .email-container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
        }
        .header {
            background: linear-gradient(135deg, #1e6b7a 0%, #2d8a99 50%, #d4af37 100%);
            padding: 2rem;
            text-align: center;
        }
        .logo {
            font-size: 3rem;
            margin-bottom: 0.5rem;
        }
        .brand {
            color: white;
            font-size: 1.5rem;
            font-weight: 700;
            margin: 0;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        .content {
            padding: 2rem;
        }
        .greeting {
            font-size: 1.3rem;
            color: #1e6b7a;
            margin: 0 0 1rem 0;
            font-weight: 700;
        }
        .message {
            font-size: 1rem;
            color: #2c3e50;
            margin-bottom: 1.5rem;
        }
        .security-warning {
            background: #fff3cd;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #d4af37;
            margin: 1.5rem 0;
        }
        .security-warning strong {
            color: #856404;
        }
        .button-container {
            text-align: center;
            margin: 2rem 0;
        }
        .confirm-button {
            background: linear-gradient(135deg, #1e6b7a 0%, #2d8a99 50%, #d4af37 100%);
            color: white !important;
            padding: 14px 36px;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 700;
            font-size: 1rem;
            display: inline-block;
            box-shadow: 0 4px 6px rgba(30, 107, 122, 0.3);
        }
        .link-fallback {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #2d8a99;
            margin: 1.5rem 0;
            font-size: 0.9rem;
            color: #6c757d;
        }
        .link-fallback a {
            color: #1e6b7a;
            word-break: break-all;
        }
        .whakatauki {
            background: linear-gradient(135deg, #e8f4f8 0%, #fff9e6 100%);
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid #d4af37;
            margin: 2rem 0;
            text-align: center;
        }
        .whakatauki-text {
            font-family: 'Merriweather', serif;
            font-style: italic;
            color: #1e6b7a;
            font-size: 1.1rem;
            margin: 0 0 0.5rem 0;
        }
        .whakatauki-translation {
            color: #2d8a99;
            font-size: 0.95rem;
            margin: 0;
        }
        .footer {
            background: #2c3e50;
            color: white;
            padding: 2rem;
            text-align: center;
        }
        .footer-brand {
            font-size: 1.2rem;
            font-weight: 700;
            margin: 0 0 0.5rem 0;
        }
        .footer-tagline {
            font-size: 0.9rem;
            color: #95a5a6;
            margin: 0 0 1rem 0;
        }
        .footer-link {
            color: #d4af37;
            text-decoration: none;
            font-weight: 600;
        }
        .disclaimer {
            color: #95a5a6;
            font-size: 0.8rem;
            margin-top: 1.5rem;
            padding-top: 1rem;
            border-top: 1px solid #34495e;
        }
    </style>
</head>
<body>
    <div class="email-container">
        <!-- Header -->
        <div class="header">
            <div class="logo">📧</div>
            <h1 class="brand">Confirm Email Change</h1>
        </div>

        <!-- Main Content -->
        <div class="content">
            <h2 class="greeting">Kia ora!</h2>
            
            <p class="message">
                You requested to change your email address for your <strong>Te Kete Ako</strong> account.
            </p>

            <div class="security-warning">
                <strong>⚠️ Security Notice:</strong><br>
                To complete this change, please confirm your new email address. If you didn't request this change, contact us immediately.
            </div>

            <div class="button-container">
                <a href="{{ .ConfirmationURL }}" class="confirm-button">
                    ✅ Confirm New Email
                </a>
            </div>

            <div class="link-fallback">
                <strong>Button not working?</strong><br>
                Copy and paste this link into your browser:<br>
                <a href="{{ .ConfirmationURL }}">{{ .ConfirmationURL }}</a>
            </div>

            <!-- Whakataukī -->
            <div class="whakatauki">
                <p class="whakatauki-text">"Kia tūpato"</p>
                <p class="whakatauki-translation">Be cautious - your account security matters</p>
            </div>
        </div>

        <!-- Footer -->
        <div class="footer">
            <p class="footer-brand">🧺 Te Kete Ako</p>
            <p class="footer-tagline">Aotearoa New Zealand</p>
            <a href="https://tekete.co.nz" class="footer-link">tekete.co.nz</a>
            
            <p class="disclaimer">
                If you didn't request this email change, contact support@tekete.co.nz immediately.
            </p>
        </div>
    </div>
</body>
</html>
```

---

## 6️⃣ REAUTHENTICATION

Template name in Supabase: **"Reauthenticate" or "Confirm Action"**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Merriweather:ital,wght@0,300;0,400&display=swap');
        
        body {
            margin: 0;
            padding: 0;
            font-family: 'Lato', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background-color: #f8f9fa;
            color: #2c3e50;
            line-height: 1.6;
        }
        .email-container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
        }
        .header {
            background: linear-gradient(135deg, #1e6b7a 0%, #2d8a99 50%, #d4af37 100%);
            padding: 2rem;
            text-align: center;
        }
        .logo {
            font-size: 3rem;
            margin-bottom: 0.5rem;
        }
        .brand {
            color: white;
            font-size: 1.5rem;
            font-weight: 700;
            margin: 0;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        .content {
            padding: 2rem;
        }
        .greeting {
            font-size: 1.3rem;
            color: #1e6b7a;
            margin: 0 0 1rem 0;
            font-weight: 700;
        }
        .message {
            font-size: 1rem;
            color: #2c3e50;
            margin-bottom: 1.5rem;
        }
        .security-warning {
            background: #f8d7da;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #dc3545;
            margin: 1.5rem 0;
        }
        .security-warning strong {
            color: #721c24;
        }
        .button-container {
            text-align: center;
            margin: 2rem 0;
        }
        .confirm-button {
            background: linear-gradient(135deg, #1e6b7a 0%, #2d8a99 50%, #d4af37 100%);
            color: white !important;
            padding: 14px 36px;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 700;
            font-size: 1rem;
            display: inline-block;
            box-shadow: 0 4px 6px rgba(30, 107, 122, 0.3);
        }
        .link-fallback {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #2d8a99;
            margin: 1.5rem 0;
            font-size: 0.9rem;
            color: #6c757d;
        }
        .link-fallback a {
            color: #1e6b7a;
            word-break: break-all;
        }
        .whakatauki {
            background: linear-gradient(135deg, #e8f4f8 0%, #fff9e6 100%);
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid #d4af37;
            margin: 2rem 0;
            text-align: center;
        }
        .whakatauki-text {
            font-family: 'Merriweather', serif;
            font-style: italic;
            color: #1e6b7a;
            font-size: 1.1rem;
            margin: 0 0 0.5rem 0;
        }
        .whakatauki-translation {
            color: #2d8a99;
            font-size: 0.95rem;
            margin: 0;
        }
        .footer {
            background: #2c3e50;
            color: white;
            padding: 2rem;
            text-align: center;
        }
        .footer-brand {
            font-size: 1.2rem;
            font-weight: 700;
            margin: 0 0 0.5rem 0;
        }
        .footer-tagline {
            font-size: 0.9rem;
            color: #95a5a6;
            margin: 0 0 1rem 0;
        }
        .footer-link {
            color: #d4af37;
            text-decoration: none;
            font-weight: 600;
        }
        .disclaimer {
            color: #95a5a6;
            font-size: 0.8rem;
            margin-top: 1.5rem;
            padding-top: 1rem;
            border-top: 1px solid #34495e;
        }
    </style>
</head>
<body>
    <div class="email-container">
        <!-- Header -->
        <div class="header">
            <div class="logo">🛡️</div>
            <h1 class="brand">Security Verification</h1>
        </div>

        <!-- Main Content -->
        <div class="content">
            <h2 class="greeting">Kia ora {{ .Email }}!</h2>
            
            <p class="message">
                For your security, we need to verify it's really you before you can proceed.
            </p>

            <div class="security-warning">
                <strong>🔐 Security Action Required:</strong><br>
                This verification link expires in <strong>5 minutes</strong>. If you didn't attempt this action, contact us immediately.
            </div>

            <div class="button-container">
                <a href="{{ .ConfirmationURL }}" class="confirm-button">
                    ✅ Verify It's Me
                </a>
            </div>

            <div class="link-fallback">
                <strong>Button not working?</strong><br>
                Copy and paste this link into your browser:<br>
                <a href="{{ .ConfirmationURL }}">{{ .ConfirmationURL }}</a>
            </div>

            <!-- Whakataukī -->
            <div class="whakatauki">
                <p class="whakatauki-text">"Kia tūpato, kia kaha"</p>
                <p class="whakatauki-translation">Be cautious, be strong</p>
            </div>
        </div>

        <!-- Footer -->
        <div class="footer">
            <p class="footer-brand">🧺 Te Kete Ako</p>
            <p class="footer-tagline">Aotearoa New Zealand</p>
            <a href="https://tekete.co.nz" class="footer-link">tekete.co.nz</a>
            
            <p class="disclaimer">
                This is a critical security verification. If this wasn't you, contact support@tekete.co.nz immediately.
            </p>
        </div>
    </div>
</body>
</html>
```

---

## ✅ ALL TEMPLATES COMPLETE!

**What to do:**
1. Go to Supabase Dashboard > Authentication > Email Templates
2. Copy each template above into the corresponding template type
3. Save each one
4. Test by triggering each email type

**Design Consistency:**
- ✅ Teal-to-gold gradient header (brand colors)
- ✅ Different emojis for each type (visual differentiation)
- ✅ Culturally appropriate whakataukī for each context
- ✅ Professional footer with tekete.co.nz branding
- ✅ Security notices where appropriate
- ✅ Button + link fallback for accessibility

All emails are beautiful, on-brand, and culturally grounded! 🧺✨

