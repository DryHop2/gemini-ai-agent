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

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()