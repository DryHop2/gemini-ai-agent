import os
import sys
from dotenv import load_dotenv
from google import genai
from config import SYSTEM_PROMPT
from functions.call_function import call_function
from function_declaration import (
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file,
)


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

    messages = [
        # genai.types.Content(role="system", parts=[genai.types.Part(text=SYSTEM_PROMPT)]),
        genai.types.Content(role="user", parts=[genai.types.Part(text=prompt)]),
    ]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
    available_functions = genai.types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )

    for iteration in range(20):
        if verbose:
            print(f"\n--- Iteration {iteration + 1} ---")

        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=genai.types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=SYSTEM_PROMPT,
            ),
        )

        for candidate in response.candidates:
            if candidate.content:
                messages.append(candidate.content)
                if verbose:
                    print(f"Model response candidate: {candidate.content.parts[0].text}")

        if response.function_calls:
            for call in response.function_calls:
                if verbose:
                    print(f"Function call detected: {call.name}({call.args})")
                function_call_result = call_function(call, verbose=verbose)

                try:
                    _ = function_call_result.parts[0].function_response.response
                except Exception:
                    raise RuntimeError("Fatal Error: No response returned from tool execution.")
                
                if verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")

                messages.append(function_call_result)

            continue

        print("\nAgent finished:\n")
        print(response.text or "No output produced.")
        break
    else:
        print("\nAgent stopped after max iterations.")


def print_verbose(response, messages):
    last_user = [m for m in messages if m.role == "user"][-1]
    prompt_text = last_user.parts[0].text
    print("User prompt:", prompt_text)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Working on:", response.model_version)

if __name__ == "__main__":
    main()