import os
import sys
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()

    args = sys.argv[1:]
    prompt_parts = []
    verbose = False

    if not args:
        print("Usage: python main.py 'your prompt here'")
        print("Example: python main.py 'How do I build a calculator app?'")
        sys.exit(1)
    for arg in args:
        if arg.startswith("-"):
            if arg in ("--verbose", "-v"):
                verbose = True
            else:    
                print(f"Unknown option: {arg}")
                sys.exit(1)
        else:
            prompt_parts.append(arg)
    prompt = " ".join(prompt_parts)

    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    messages = [genai.types.Content(role="user", parts=[genai.types.Part(text=prompt)]),]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print("Response:")
    print(response.text)
    if verbose:
        print_verbose(response, messages)


def print_verbose(response, messages):
    last_user = [m for m in messages if m.role == "user"][-1]
    prompt_text = last_user.parts[0].text
    print("User prompt:", prompt_text)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Working on:", response.model_version)

if __name__ == "__main__":
    main()