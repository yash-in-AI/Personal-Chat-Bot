import os
from dotenv import load_dotenv
from google import genai


# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()


# ==========================================
# GET GEMINI API KEY
# ==========================================

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. "
        "Please check your .env file."
    )


# ==========================================
# CREATE GEMINI CLIENT
# ==========================================

client = genai.Client(
    api_key=api_key
)


# ==========================================
# AI INSTRUCTIONS
# ==========================================

SYSTEM_INSTRUCTION = """
You are a helpful AI assistant .

Your main purpose is to help the user learn about anything:

 

Follow these rules:

1. Explain concepts in simple language.

2. Use Roman Urdu when appropriate.

3. When explaining code, explain it step by step.

4. Give beginner-friendly examples.

5. If the user asks for code, provide complete runnable code.

6. Avoid unnecessarily advanced concepts.

7. If the user provides code containing an error:
   - Identify the error.
   - Explain why it happened.
   - Provide the corrected code.

8. For technical questions, provide practical examples.

9. Keep answers clear and organized.

10. Be friendly and helpful.
"""


# ==========================================
# ASK GEMINI FUNCTION
# ==========================================

def ask_gemini(question):

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        system_instruction=SYSTEM_INSTRUCTION,
        input=question
    )

    return interaction.output_text


# ==========================================
# CHATBOT
# ==========================================

print("======================================")
print("        Your Personal AI CHATBOT")
print("======================================")
print("Type 'exit' to close the chatbot.")
print()


while True:

    user_input = input("You: ")

    # Exit chatbot
    if user_input.lower() == "exit":
        print("AI: Allah Hafiz! 👋")
        break

    # Don't send empty messages
    if not user_input.strip():
        print("AI: Please enter a question.")
        continue

    try:

        response = ask_gemini(user_input)

        print()
        print("AI:", response)
        print()

    except Exception as e:

        print()
        print("Error:", e)
        print()