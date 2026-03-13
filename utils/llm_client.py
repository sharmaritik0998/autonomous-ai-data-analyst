import os
from groq import Groq
from dotenv import load_dotenv

# .env file load karega
load_dotenv()

# API key environment variable se lega
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_text(prompt):

    try:

        chat = client.chat.completions.create(

            messages=[
                {"role": "system", "content": "You are a professional data analyst."},
                {"role": "user", "content": prompt}
            ],

            model="llama-3.1-8b-instant",
            temperature=0.3

        )

        return chat.choices[0].message.content

    except Exception as e:
        return f"Error calling Groq API: {e}"