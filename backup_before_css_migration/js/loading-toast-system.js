/**
 * Loading & Toast System - Te Kete Ako
 * Professional feedback for user actions
 * Agent-9 - October 15, 2025
 */

(function() {
    'use strict';

    // =================================================================
    // LOADING OVERLAY
    // =================================================================
    window.showLoading = function(message = 'Loading...') {
        let overlay = document.querySelector('.loading-overlay');
        
        if (!overlay) {
            overlay = document.createElement('div');
            overlay.className = 'loading-overlay';
            overlay.innerHTML = `
                <div class="loading-content">
                    <div class="loading-spinner loading-spinner-large"></div>
                    <p class="loading-text">${message}</p>
                </div>
            `;
            document.body.appendChild(overlay);
        } else {
            overlay.querySelector('.loading-text').textContent = message;
        }
        
        overlay.classList.add('active');
    };

    window.hideLoading = function() {
        const overlay = document.querySelector('.loading-overlay');
        if (overlay) {
            overlay.classList.remove('active');
        }
    };

    // =================================================================
    // TOAST NOTIFICATIONS
    // =================================================================
    window.showToast = function(message, type = 'success', duration = 4000) {
        let container = document.querySelector('.toast-container');
        
        if (!container) {
            container = document.createElement('div');
            container.className = 'toast-container';
            document.body.appendChild(container);
        }

        const icons = {
            success: '✅',
            error: '❌',
            warning: '⚠️',
            info: 'ℹ️'
        };

        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        toast.innerHTML = `
            <span class="toast-icon">${icons[type] || icons.info}</span>
            <span class="toast-message">${message}</span>
            <button class="toast-close" aria-label="Close notification">✕</button>
        `;

        container.appendChild(toast);

        // Close button
        toast.querySelector('.toast-close').addEventListener('click', function() {
            removeToast(toast);
        });

        // Auto-remove after duration
        if (duration > 0) {
            setTimeout(() => {
                removeToast(toast);
            }, duration);
        }
    };

    function removeToast(toast) {
        toast.style.animation = 'slideOutRight 0.4s ease';
        setTimeout(() => toast.remove(), 400);
    }

    // =================================================================
    // PROGRESS BAR
    // =================================================================
    window.createProgressBar = function(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return null;

        const progressBar = document.createElement('div');
        progressBar.className = 'progress-bar';
        progressBar.innerHTML = '<div class="progress-fill" style="width: 0%"></div>';
        container.appendChild(progressBar);

        return {
            element: progressBar,
            setProgress: function(percent) {
                const fill = progressBar.querySelector('.progress-fill');
                fill.style.width = Math.min(100, Math.max(0, percent)) + '%';
            }
        };
    };

    // =================================================================
    // DEMO: TEST NOTIFICATIONS
    // =================================================================
    window.testLoadingSystem = function() {
        // Test loading
        showLoading('Processing your request...');
        
        setTimeout(() => {
            hideLoading();
            showToast('Operation completed successfully!', 'success');
        }, 2000);
        
        // Test different toast types
        setTimeout(() => showToast('This is an info message', 'info'), 2500);
        setTimeout(() => showToast('Warning: Check your inputs', 'warning'), 3000);
        setTimeout(() => showToast('Error occurred, please try again', 'error', 6000), 3500);
    };

    // Expose globally
    window.LoadingSystem = {
        showLoading,
        hideLoading,
        showToast,
        createProgressBar,
        test: testLoadingSystem
    };

    console.log('✅ Loading & Toast System initialized');
    console.log('   Test with: LoadingSystem.test()');

})();

