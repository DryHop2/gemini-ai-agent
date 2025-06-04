import os
import sys
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()

    query = sys.argv[1:]
    if not query:
        print("Usage: python main.py 'your prompt here'")
        print("Example: pythong main.py 'How do I build a calculator app?'")
        sys.exit(1)
    prompt = " ".join(query)

    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    messages = [genai.types.Content(role="user", parts=[genai.types.Part(text=prompt)]),]

    generate_content(client, messages)


def generate_content(client, messages):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()