#!/bin/bash

NAV_HEADER='                        <header class="site-header no-print">
        <div class="nav-container">
            <a href="/index.html" class="nav-brand">Te Kete Ako</a>
            <nav class="main-nav">
                <ul>
                    <li><a href="/unit-plans.html" class="nav-link"><span class="nav-icon">📚</span><span class="nav-text-en">Unit Plans</span><span class="nav-text-mi" lang="mi">Ngā Waehere</span></a></li>
                    <li><a href="/lessons.html" class="nav-link"><span class="nav-icon">🎓</span><span class="nav-text-en">Lessons</span><span class="nav-text-mi" lang="mi">Ngā Akoranga</span></a></li>
                    <li><a href="/handouts.html" class="nav-link"><span class="nav-icon">📄</span><span class="nav-text-en">Handouts</span><span class="nav-text-mi" lang="mi">Ngā Rauemi</span></a></li>
                    <li><a href="/teachers/index.html" class="nav-link"><span class="nav-icon">🧑‍🏫</span><span class="nav-text-en">Teachers</span><span class="nav-text-mi" lang="mi">Ngā Kaiako</span></a></li>
                    <li class="auth-nav"><a href="/login.html" class="nav-link login-btn"><span class="nav-icon">👤</span>Login</a></li>
                </ul>
            </nav>
            <nav class="breadcrumbs no-print" aria-label="Breadcrumb"><ol id="breadcrumbs" class="breadcrumbs-list"></ol></nav>
        </div>
    </header>

'

for file in public/units/unit-1-te-ao-maori/lessons/*.html; do
  if [[ ! "$file" =~ (backup|master|FIXED) ]] && ! grep -q "site-header" "$file"; then
    # Add nav after <body> tag
    sed -i '' "/<body>/a\\
$NAV_HEADER
" "$file"
    echo "✅ Added nav: $(basename $file)"
  fi
done
