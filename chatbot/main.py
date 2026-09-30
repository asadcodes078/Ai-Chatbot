from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

SYSTEM_PROMPT = """
you are a helpful AI assistant answer according to user query and give answer in shortly
"""
while True:

    user_query = input("you: ")
    if user_query == "exit":
        break

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents= user_query,
        config={
            'system_instruction':SYSTEM_PROMPT 
        }
    )
    print(f"AI👉 ",response.text)