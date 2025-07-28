# 🗃️ SUPABASE RESOURCE INTEGRATION EXECUTION GUIDE

## 📋 OVERVIEW

This guide will help you execute the SQL statements to add the 14 critical discovered resources from the comprehensive site audit to your Supabase database. These resources include the 4 major standalone platforms and 10 other critical educational tools that were "hidden" in the platform.

## 🎯 RESOURCES TO BE ADDED

### TIER 1: Critical Standalone Platforms
1. **Classroom Leaderboard System** - Gamification & progress tracking
2. **Digital Pūrākau Interactive Storytelling** - Cultural narrative platform  
3. **Living Whakapapa Project** - Genealogical learning system
4. **Virtual Marae Training Protocol** - VR/AR cultural education

### TIER 2: Y8 Systems Society Design Resources  
5. **Society Design Collaboration Framework** - Group work management
6. **Society Design Assessment Rubric** - Evaluation criteria
7. **Decolonized Design Template** - Cultural design framework
8. **Design-a-System Template** - Systems thinking scaffolding

### TIER 3: Professional Development Resources
9. **Decolonized Assessment Framework** - Cultural assessment philosophy
10. **Professional Lesson Template** - Standardized planning format

### TIER 4: Interactive Tools & Games
11. **Interactive Society Design Tool** - Digital society creation
12. **Guided Inquiry: Society Design Project** - 5-week collaborative framework

### TIER 5: Complete Units
13. **Year 8 Systems Unit: Decolonizing Power Structures** - Complete 5-week unit
14. **Complete Design Your Society Unit** - Comprehensive systems thinking unit

## 🔧 EXECUTION METHODS

### METHOD 1: Supabase Dashboard SQL Editor (RECOMMENDED)

1. **Access Your Supabase Dashboard**
   - Go to https://supabase.com
   - Sign in to your account
   - Select your Te Kete Ako project

2. **Open SQL Editor**
   - Click on "SQL Editor" in the left sidebar
   - Click "New Query" to create a new SQL query

3. **Execute the SQL**
   - Copy the contents of `CORRECTED_SUPABASE_RESOURCE_INTEGRATION.sql`
   - Paste into the SQL Editor
   - Click "Run" to execute

4. **Verify Success**
   - Check that you see success messages for all INSERT statements
   - Go to "Table Editor" → "resources" to verify the new entries

### METHOD 2: Using Supabase CLI (If Available)

```bash
# Install Supabase CLI
npm install -g supabase

# Login to your account
supabase login

# Link to your project
supabase link --project-ref your-project-ref

# Execute the SQL file
supabase db execute -f CORRECTED_SUPABASE_RESOURCE_INTEGRATION.sql
```

### METHOD 3: Using psql (Direct PostgreSQL Connection)

If you have the direct database connection string:

```bash
psql "your-connection-string" -f CORRECTED_SUPABASE_RESOURCE_INTEGRATION.sql
```

## 📝 SQL FILE DETAILS

**File:** `CORRECTED_SUPABASE_RESOURCE_INTEGRATION.sql`

This file contains:
- ✅ **14 INSERT statements** for the critical discovered resources
- ✅ **Proper schema matching** the existing resources table structure
- ✅ **Cultural integration metadata** with Te Ao Māori concepts
- ✅ **Curriculum alignment** with NZ Achievement Objectives
- ✅ **Performance indexes** for optimal database performance
- ✅ **Updated featured resources view** for homepage display

## 🔍 VERIFICATION STEPS

After executing the SQL, verify the integration:

1. **Check Resource Count**
   ```sql
   SELECT COUNT(*) FROM resources WHERE author = 'Te Kete Ako Team';
   ```
   *Should return significantly more resources than before*

2. **Verify Featured Resources**
   ```sql
   SELECT title, type, path FROM resources WHERE featured = true ORDER BY created_at DESC;
   ```
   *Should include the new high-priority resources*

3. **Check Cultural Integration**
   ```sql
   SELECT title, cultural_elements->'cultural_integration' as cultural_level 
   FROM resources 
   WHERE cultural_elements->'cultural_integration' = '"essential"';
   ```
   *Should show the culturally significant resources*

## 🚨 TROUBLESHOOTING

### Common Issues & Solutions

**Issue: "relation 'resources' does not exist"**
- **Solution:** First execute the `deploy-resources-table.sql` to create the table

**Issue: "column does not exist"**  
- **Solution:** The existing table schema might be different. Check table structure with:
  ```sql
  \d resources
  ```

**Issue: "duplicate key value violates unique constraint"**
- **Solution:** Some resources might already exist. Use `INSERT ... ON CONFLICT DO NOTHING` or check existing data first

**Issue: "permission denied"**
- **Solution:** Ensure you have the necessary permissions or use the service role key

## 🎉 EXPECTED OUTCOME

After successful execution, you should see:

- ✅ **14 new resources** in your resources table
- ✅ **Enhanced featured resources** on your homepage
- ✅ **Improved cultural content** discovery
- ✅ **Better resource categorization** with proper tags and metadata
- ✅ **Curriculum-aligned content** for educational planning

## 📊 INTEGRATION IMPACT

This integration will:

1. **Unlock Hidden Value** - Make 14 critical educational tools discoverable
2. **Enhance Cultural Learning** - Showcase Te Ao Māori resources properly  
3. **Improve User Experience** - Students and teachers can find powerful tools
4. **Support Assessment** - Provide frameworks for culturally responsive evaluation
5. **Enable Collaboration** - Offer group work and project management tools

## 🔄 NEXT STEPS

After successful integration:

1. **Update Navigation** - Add links to new resources in main menu
2. **Test Functionality** - Verify all new resource links work correctly
3. **Cultural Validation** - Ensure cultural content is appropriate and accurate
4. **User Training** - Inform teachers about newly available tools
5. **Analytics Setup** - Track usage of integrated resources

---

**🌟 This integration represents a major enhancement to Te Kete Ako, transforming it from a collection of resources into a comprehensive, culturally-grounded educational platform.**