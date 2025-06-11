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