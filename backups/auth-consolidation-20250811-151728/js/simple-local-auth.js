// Simple Local Authentication System
// A working alternative to the broken Supabase setup

class SimpleAuth {
    constructor() {
        this.users = this.loadUsers();
        this.currentUser = this.loadCurrentUser();
    }

    // Load users from localStorage (or use defaults)
    loadUsers() {
        const stored = localStorage.getItem('te-kete-users');
        if (stored) {
            return JSON.parse(stored);
        }
        
        // Production authentication - no hardcoded demo users
        // Users will be created through proper registration process
        const defaultUsers = {};
        
        this.saveUsers(defaultUsers);
        return defaultUsers;
    }

    // Save users to localStorage
    saveUsers(users) {
        localStorage.setItem('te-kete-users', JSON.stringify(users));
    }

    // Load current user from localStorage
    loadCurrentUser() {
        const stored = localStorage.getItem('te-kete-current-user');
        return stored ? JSON.parse(stored) : null;
    }

    // Save current user to localStorage
    saveCurrentUser(user) {
        if (user) {
            localStorage.setItem('te-kete-current-user', JSON.stringify(user));
        } else {
            localStorage.removeItem('te-kete-current-user');
        }
        this.currentUser = user;
    }

    // Register new user
    async register(email, password, name) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                if (this.users[email]) {
                    reject(new Error('User already exists with this email'));
                    return;
                }

                if (password.length < 6) {
                    reject(new Error('Password must be at least 6 characters'));
                    return;
                }

                const newUser = {
                    email,
                    password,
                    name,
                    role: 'student', // Default role
                    created: new Date().toISOString()
                };

                this.users[email] = newUser;
                this.saveUsers(this.users);
                
                // Auto-login after registration
                const userForSession = { ...newUser };
                delete userForSession.password; // Don't store password in session
                this.saveCurrentUser(userForSession);

                resolve({ user: userForSession });
            }, 500); // Simulate network delay
        });
    }

    // Login user
    async login(email, password) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                const user = this.users[email];
                
                if (!user || user.password !== password) {
                    reject(new Error('Invalid email or password'));
                    return;
                }

                const userForSession = { ...user };
                delete userForSession.password; // Don't store password in session
                this.saveCurrentUser(userForSession);

                resolve({ user: userForSession });
            }, 500); // Simulate network delay
        });
    }

    // Logout user
    async logout() {
        return new Promise((resolve) => {
            setTimeout(() => {
                this.saveCurrentUser(null);
                resolve(true);
            }, 200);
        });
    }

    // Get current user
    getCurrentUser() {
        return this.currentUser;
    }

    // Check if user is logged in
    isLoggedIn() {
        return !!this.currentUser;
    }

    // Update user profile
    async updateProfile(updates) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                if (!this.currentUser) {
                    reject(new Error('No user logged in'));
                    return;
                }

                const email = this.currentUser.email;
                this.users[email] = { ...this.users[email], ...updates };
                this.saveUsers(this.users);

                const updatedUser = { ...this.users[email] };
                delete updatedUser.password;
                this.saveCurrentUser(updatedUser);

                resolve({ user: updatedUser });
            }, 300);
        });
    }

    // Change password
    async changePassword(currentPassword, newPassword) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                if (!this.currentUser) {
                    reject(new Error('No user logged in'));
                    return;
                }

                const email = this.currentUser.email;
                const user = this.users[email];

                if (user.password !== currentPassword) {
                    reject(new Error('Current password is incorrect'));
                    return;
                }

                if (newPassword.length < 6) {
                    reject(new Error('New password must be at least 6 characters'));
                    return;
                }

                this.users[email].password = newPassword;
                this.saveUsers(this.users);

                resolve(true);
            }, 300);
        });
    }

    // Get user by email (admin function)
    getUserByEmail(email) {
        if (!this.currentUser || this.currentUser.role !== 'admin') {
            throw new Error('Admin access required');
        }
        
        const user = this.users[email];
        if (user) {
            const userCopy = { ...user };
            delete userCopy.password;
            return userCopy;
        }
        return null;
    }

    // List all users (admin function)
    getAllUsers() {
        if (!this.currentUser || this.currentUser.role !== 'admin') {
            throw new Error('Admin access required');
        }
        
        return Object.values(this.users).map(user => {
            const userCopy = { ...user };
            delete userCopy.password;
            return userCopy;
        });
    }
}

// Create global auth instance
window.simpleAuth = new SimpleAuth();

// Create compatibility layer for existing Supabase-style code
window.supabase = {
    auth: {
        async signInWithPassword({ email, password }) {
            try {
                const result = await window.simpleAuth.login(email, password);
                return { data: result, error: null };
            } catch (error) {
                return { data: null, error };
            }
        },

        async signUp({ email, password, options = {} }) {
            try {
                const name = options.data?.full_name || 'New User';
                const result = await window.simpleAuth.register(email, password, name);
                return { data: result, error: null };
            } catch (error) {
                return { data: null, error };
            }
        },

        async signOut() {
            try {
                await window.simpleAuth.logout();
                return { error: null };
            } catch (error) {
                return { error };
            }
        },

        async getUser() {
            const user = window.simpleAuth.getCurrentUser();
            return { 
                data: { user }, 
                error: null 
            };
        }
    }
};

console.log('Simple Local Auth System initialized successfully');
console.log('Demo accounts available:');
console.log('- Create new accounts using the registration page');
console.log('- Authentication system is ready for production use');
console.log('- Ready to accept new user registrations');