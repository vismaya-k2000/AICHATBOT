from groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()


api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")


client = Groq(api_key=api_key)

SYSTEM_PROMPT = """
You are a helpful AI assistant.

Instructions:
- Use previous conversation context.
- Understand words like it, its, they based on previous messages.
- Do not hallucinate.
- Ask clarification if unsure.
- Avoid repeating answers.
"""

chat_history = []

MAX_HISTORY = 8

print("Groq Chatbot Started! Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    
    chat_history.append({
        "role": "user",
        "content": user_input
    })

    
    if len(chat_history) > MAX_HISTORY:
        chat_history = chat_history[-MAX_HISTORY:]

    
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ] + chat_history

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=1024
        )

        answer = response.choices[0].message.content
        print(f"\nBot: {answer}\n")

        
        chat_history.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        print("\nError:", e)