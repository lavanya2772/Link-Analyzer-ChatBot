# groq_api.py
import os
from groq import Groq

def query_groq(content, question):
    # Ensure the correct environment variable is used
    groq_api_key = os.environ.get("Enter Your API Key Name")
    
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables.")
    
    print(f"Using API Key: {groq_api_key[:5]}... (truncated for security)")  # Debugging
    
    client = Groq(api_key=groq_api_key)
    
    prompt = f"""You are a helpful assistant that analyzes text content from a given link and answers a question related to the content. 
    You MUST respond with ONLY a list of items, with each item on a new line. Do not include any introductory phrases, numbering, or bullet points.
    Here is the content:
    {content}

    Question: {question}

    Answer:"""
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=1024,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        answer = chat_completion.choices[0].message.content
        return answer
    except Exception as e:
        print(f"Groq API Error: {str(e)}")  # Print detailed error message
        return f"Groq API Error: {str(e)}"
