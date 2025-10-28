-- Automatic Content Indexer for GraphRAG
-- Scans filesystem and indexes ALL teaching content
-- Can be run repeatedly to add new content

-- This script is meant to be called with file lists from terminal
-- Example: Run scan-and-index.sh which calls this SQL

-- For now, let's create the helper functions for automatic indexing

-- 1. Function: Extract year level from path/filename
CREATE OR REPLACE FUNCTION extract_year_level(file_path text)
RETURNS text AS $$
BEGIN
  -- Match patterns like "y8-", "year-8-", "Y8", etc.
  IF file_path ~ 'y8-|year-?8|Y8' THEN RETURN '8';
  ELSIF file_path ~ 'y9-|year-?9|Y9' THEN RETURN '9';
  ELSIF file_path ~ 'y10-|year-?10|Y10' THEN RETURN '10';
  ELSIF file_path ~ 'y11-|year-?11|Y11' THEN RETURN '11';
  ELSIF file_path ~ 'y12-|year-?12|Y12' THEN RETURN '12';
  ELSIF file_path ~ 'y13-|year-?13|Y13' THEN RETURN '13';
  
  -- Check for ranges in filename
  ELSIF file_path ~ '7-10|7-13|8-10|8-12' THEN 
    RETURN SUBSTRING(file_path FROM '(\d+-\d+)');
  
  -- Default: guess from location
  ELSIF file_path LIKE '%units%' THEN RETURN '7-13';
  ELSIF file_path LIKE '%handouts%' THEN RETURN '8-12';
  ELSE RETURN '7-13';  -- Generic default
  END IF;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- 2. Function: Extract subject from filename/path
CREATE OR REPLACE FUNCTION extract_subject(file_path text, title text)
RETURNS text AS $$
DECLARE
  path_lower text := LOWER(file_path || ' ' || COALESCE(title, ''));
BEGIN
  -- Te Reo / Te Ao Māori (check first - most specific)
  IF path_lower ~ 'te-reo|maori-greetings|wordle.*maori|te-ao-maori|whakapapa|tikanga|mātauranga|matauranga|kaitiakitanga|rangatiratanga' THEN
    RETURN 'te-reo';
  
  -- Math
  ELSIF path_lower ~ 'math|probability|statistics|graph|geometric|algebra' THEN
    RETURN 'mathematics';
  
  -- Science
  ELSIF path_lower ~ 'science|climate|microplastic|genetic|sleep|tectonic|stem|ecological' THEN
    RETURN 'science';
  
  -- Social Studies
  ELSIF path_lower ~ 'treaty|waitangi|history|decoloni|economic|justice|raids|battalion|wars|tino|bastion|global|system' THEN
    RETURN 'social-studies';
  
  -- English
  ELSIF path_lower ~ 'english|writer|author|rhetoric|persuade|entertain|literacy|media|peel|diction|tone|hook|conclusion|speech|soliloquy|shakespeare' THEN
    RETURN 'english';
  
  -- Technology
  ELSIF path_lower ~ 'technology|digital|ai-|llm|prompt|design-thinking|citizenship|sovereignty.*data|ethics.*ai' THEN
    RETURN 'technology';
  
  -- Arts
  ELSIF path_lower ~ 'arts|elements-of-art|film.*scene' THEN
    RETURN 'arts';
  
  -- Health/PE
  ELSIF path_lower ~ 'health|vaping|pe-' THEN
    RETURN 'health-pe';
  
  -- Cross-curricular
  ELSIF path_lower ~ 'cross-curricular|future.*rangatiratanga|design.*society' THEN
    RETURN 'cross-curricular';
  
  ELSE
    RETURN 'general';
  END IF;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- 3. Function: Detect resource type from path
CREATE OR REPLACE FUNCTION detect_resource_type(file_path text)
RETURNS text AS $$
BEGIN
  IF file_path LIKE '%/handouts/%' THEN RETURN 'handout';
  ELSIF file_path LIKE '%/lessons/%' THEN RETURN 'lesson';
  ELSIF file_path LIKE '%unit%' AND file_path NOT LIKE '%lesson%' THEN RETURN 'unit-plan';
  ELSIF file_path LIKE '%/games/%' THEN RETURN 'game';
  ELSIF file_path LIKE '%video-activit%' THEN RETURN 'video';
  ELSIF file_path LIKE '%/activities/%' THEN RETURN 'activity';
  ELSIF file_path LIKE '%do-now%' THEN RETURN 'activity';
  ELSIF file_path LIKE '%/templates/%' THEN RETURN 'template';
  ELSE RETURN 'other';
  END IF;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- 4. Function: Extract title from filename
CREATE OR REPLACE FUNCTION extract_title_from_path(file_path text)
RETURNS text AS $$
DECLARE
  filename text;
  title text;
BEGIN
  -- Get filename without extension
  filename := REGEXP_REPLACE(file_path, '^.*/([^/]+)\.html$', '\1');
  
  -- Clean up: replace hyphens/underscores with spaces, title case
  title := REGEXP_REPLACE(filename, '[-_]', ' ', 'g');
  title := INITCAP(title);
  
  -- Clean common patterns
  title := REPLACE(title, 'Handout', '');
  title := REPLACE(title, 'Lesson', '');
  title := REPLACE(title, 'Unit', 'Unit');
  title := REGEXP_REPLACE(title, '\s+', ' ', 'g');
  title := TRIM(title);
  
  RETURN title;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- 5. Function: Check if file has whakataukī (heuristic)
CREATE OR REPLACE FUNCTION likely_has_whakataukī(file_path text, title text)
RETURNS boolean AS $$
BEGIN
  -- Enhanced/cultural files likely have whakataukī
  IF file_path ~ 'enhanced/|maori|cultural|te-ao|decoloni|tikanga' THEN
    RETURN true;
  -- Units typically have whakataukī
  ELSIF file_path ~ 'units/unit-' THEN
    RETURN true;
  ELSE
    RETURN false;
  END IF;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- Test the functions
SELECT 
  'handouts/media-literacy-comprehension-handout.html' as path,
  extract_title_from_path('handouts/media-literacy-comprehension-handout.html') as title,
  detect_resource_type('handouts/media-literacy-comprehension-handout.html') as type,
  extract_subject('handouts/media-literacy-comprehension-handout.html', 'Media Literacy') as subject,
  extract_year_level('handouts/media-literacy-comprehension-handout.html') as year_level,
  likely_has_whakataukī('handouts/media-literacy-comprehension-handout.html', 'Media Literacy') as has_whakataukī;
