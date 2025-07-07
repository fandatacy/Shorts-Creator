import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_topics(niche):
    prompt = f"""Give me 5 original, trending YouTube Shorts video title ideas in both English and Hindi for the niche "{niche}". Each idea should have:
- English Title
- Hindi Title
- Clickbait hook
Only give the titles, no explanation."""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def generate_script(title):
    prompt = f"""Write a 30–60 second YouTube Shorts script (spoken format) in both Hindi and English for this title: "{title}".
It should start with a hook, then give a surprising fact, and end with a strong outro."""
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
