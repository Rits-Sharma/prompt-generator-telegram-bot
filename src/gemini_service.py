import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def get_api_key():
    return os.getenv("GEMINI_API_KEY")

def init_client():
    api_key = get_api_key()
    if not api_key:
        return None
    return genai.Client()

def generate_professional_prompt(client, model, level, category, tone, user_input):
    system_instruction = (
        "You are a world-class Prompt Engineer. Convert user's idea into a "
        "structured professional prompt (Role, Objective, Context, Constraints, Expected Output). "
        "Optimize for ChatGPT/Gemini/Claude. Return ONLY the final prompt."
    )
    
    contents = (
        f"User Level: {level}\n"
        f"Category: {category}\n"
        f"Tone: {tone}\n"
        f"User Requirement: {user_input}"
    )
    
    response = client.models.generate_content(
        model=model,
        contents=contents,
        config={
            "system_instruction": system_instruction
        }
    )
    return response.text
