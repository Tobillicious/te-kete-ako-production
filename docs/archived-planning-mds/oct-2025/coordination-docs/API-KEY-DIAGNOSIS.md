# 🔍 API Key & RLS Diagnosis

**Issue:** "Invalid API key" errors despite key being correct  
**Date:** October 24, 2025

---

## ✅ **API KEY IS CORRECT**

**Actual Anon Key from Supabase:**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM
```

**Key in Code:**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM
```

**Match:** ✅ IDENTICAL

**Conclusion:** API key is NOT the problem!

---

## 🚨 **REAL ISSUE: RLS BLOCKING ACCESS**

**Error Message:**
```
GraphRAG query error: {
  message: 'Invalid API key',
  hint: 'Double check your Supabase `anon` or `service_role` API key.'
}
```

**Misleading!** This is Supabase's generic error when RLS denies access.

**Real Problem:** Row Level Security is blocking anonymous reads

---

## 🔧 **FIX NEEDED**

The graphrag_relationships table needs proper RLS policy for anonymous SELECT.

**Current Status:** Investigating policies...


