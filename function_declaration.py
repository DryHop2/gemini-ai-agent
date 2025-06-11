from google import genai

schema_get_files_info = genai.types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "directory": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = genai.types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the content as a string, up to 10,000 characters, constrained to the current working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The file path to read content from, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)

schema_run_python_file = genai.types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file (with .py extension) in a secure sandbox, limited to 30 seconds. Captures and returns STDOUT, STDERR, and exit code.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="Path to the Python (.py) file to execute, relative to the working directory. Absolute paths and paths outside the working directory are not allowed.",
            ),
            "args": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                items=genai.types.Schema(
                    type=genai.types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
            ),
        },
        required=["file_path"],
    ),
)

schema_write_file = genai.types.FunctionDeclaration(
    name="write_file",
    description="Writes text content to a file. Creates parent directories and the file if they do not exist. Overwrites existing files. All paths are constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="Path to the file to write to, relative to the working directory. Absolute paths and traversal outside the working directory are not allowed.",
            ),
            "content": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The text data to write to the file. Overwriting existing file contents is allowed."
            ),
        },
        required=["file_path", "content"],
    ),
)