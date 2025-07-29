// Firebase Configuration for Te Kete Ako
// This handles authentication while keeping Supabase for data storage

// Firebase configuration object - using TuiTrader project credentials
const firebaseConfig = {
  apiKey: "AIzaSyBVxci5nqv6DJG7-d49PrRkCRM0ilypmI8",
  authDomain: "tuitrader.firebaseapp.com", 
  projectId: "tuitrader",
  storageBucket: "tuitrader.appspot.com",
  messagingSenderId: "103397323487",
  appId: "1:103397323487:web:MzMyMjg0YjYtNzI1ZC00MWM3LWJiMmEtZWM3YWE2ZjVkZTY5"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Get Firebase Auth instance
const auth = firebase.auth();

// Export auth for global use
window.firebaseAuth = auth;

// Global Firebase authentication helper functions
window.firebaseAuthHelpers = {
  async signInWithEmail(email, password) {
    try {
      const userCredential = await auth.signInWithEmailAndPassword(email, password);
      return { user: userCredential.user, error: null };
    } catch (error) {
      return { user: null, error: error.message };
    }
  },

  async signUpWithEmail(email, password) {
    try {
      const userCredential = await auth.createUserWithEmailAndPassword(email, password);
      return { user: userCredential.user, error: null };
    } catch (error) {
      return { user: null, error: error.message };
    }
  },

  async signOut() {
    try {
      await auth.signOut();
      return { error: null };
    } catch (error) {
      return { error: error.message };
    }
  },

  getCurrentUser() {
    return auth.currentUser;
  },

  isLoggedIn() {
    return !!auth.currentUser;
  },

  onAuthStateChanged(callback) {
    return auth.onAuthStateChanged(callback);
  }
};

console.log('Firebase Auth initialized successfully');