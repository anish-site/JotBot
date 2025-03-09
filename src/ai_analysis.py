import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def analyze_task(task_text):
    """Uses AI to analyze task difficulty and detect repetitive patterns."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Analyze the difficulty of a task and check if it's repetitive."},
                  {"role": "user", "content": task_text}]
    )
    return response["choices"][0]["message"]["content"].strip()

