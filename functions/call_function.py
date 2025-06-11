from google import genai
from config import WORKING_DIR
from functions.run_python_file import run_python_file
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file


def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - calling function: {function_call_part.name}")

    function_map = {
        "run_python_file": run_python_file,
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "write_file": write_file,
    }

    func = function_map.get(function_call_part.name)

    if not func:
        return genai.types.Content(
            role="tool",
            parts=[
                genai.types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
    
    args = dict(function_call_part.args)
    args["working_directory"] = WORKING_DIR

    try:
        result = func(**args)
    except Exception as e:
        result = f'Error: Exception while calling function "{function_call_part.name}": {e}'

    return genai.types.Content(
        role="tool",
        parts=[
            genai.types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    )