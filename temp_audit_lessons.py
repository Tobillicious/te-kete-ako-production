
import sys
from supabase_graphrag_connector import SupabaseGraphRAGConnector

def audit_lessons():
    """
    Connects to Supabase and performs a read-only audit of lesson content.
    """
    print("Connecting to GraphRAG to audit lesson content...")
    try:
        connector = SupabaseGraphRAGConnector()
    except Exception as e:
        print(f"Error instantiating connector: {e}")
        return

    try:
        # 1. Get the total count of lessons
        count_result = connector.client.table('resources').select('*', count='exact').eq('type', 'lesson').execute()
        total_lessons = count_result.count
        print(f"\n--- Audit Results ---")
        print(f"Total number of 'lesson' type resources found: {total_lessons}")

        # 2. Fetch a sample of lesson records
        print("\nFetching a sample of 15 lessons for analysis...")
        sample_result = connector.client.table('resources').select('title, path, subject, author, description, tags').eq('type', 'lesson').limit(15).execute()
        
        if not sample_result.data:
            print("No lesson samples found.")
            return

        print("\n--- Sample Lesson Analysis ---")
        for i, lesson in enumerate(sample_result.data):
            print(f"\nSample #{i+1}:")
            print(f"  Title: {lesson.get('title', 'N/A')}")
            print(f"  Path: {lesson.get('path', 'N/A')}")
            print(f"  Subject: {lesson.get('subject', 'N/A')}")
            print(f"  Author: {lesson.get('author', 'N/A')}")
            print(f"  Description: {str(lesson.get('description', 'N/A'))[:100]}...")
            print(f"  Tags: {lesson.get('tags', [])}")

    except Exception as e:
        print(f"\nAn error occurred while querying the database: {e}")
        print("Please ensure the credentials in 'supabase_graphrag_connector.py' are correct and the database is accessible.")

if __name__ == "__main__":
    audit_lessons()
