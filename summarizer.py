# summarizer.py
import requests

def summarize_text(text):
    prompt = f"""
Summarize the following text for a curious reader:
1. Write a short and friendly introduction.
2. Highlight the main ideas using bullet points.
3. Add a final 'Key Takeaways' section.

Text:
{text}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",   # You can change to 'llama2', 'phi', etc.
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json().get("response", "No response from model.")
    else:
        return "Failed to get summary from local model."
