#!/usr/bin/env python3
"""
Test script for Gemini and GLM API keys.
"""

import os
import google.generativeai as genai
from zhipuai import ZhipuAI
from dotenv import load_dotenv

def test_gemini():
    """Tests the Gemini API key."""
    print("Testing Gemini API key...")
    try:
        load_dotenv()
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not gemini_api_key:
            print("❌ GEMINI_API_KEY not found in .env file.")
            return

        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("Test connection")
        
        if response.text:
            print("✅ Gemini API connection successful.")
        else:
            print("❌ Gemini API connection failed.")
            
    except Exception as e:
        print(f"❌ Gemini API error: {e}")

def test_glm():
    """Tests the GLM API key."""
    print("\nTesting GLM API key...")
    try:
        load_dotenv()
        glm_api_key = os.getenv("GLM_API_KEY")
        if not glm_api_key:
            print("❌ GLM_API_KEY not found in .env file.")
            return

        client = ZhipuAI(api_key=glm_api_key)
        response = client.chat.completions.create(
            model="glm-4",
            messages=[
                {"role": "user", "content": "Test connection"}
            ],
        )
        
        if response.choices[0].message:
            print("✅ GLM API connection successful.")
        else:
            print("❌ GLM API connection failed.")

    except Exception as e:
        print(f"❌ GLM API error: {e}")

if __name__ == "__main__":
    test_gemini()
    test_glm()
