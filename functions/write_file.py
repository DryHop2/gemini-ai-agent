import os


def write_file(working_directory, file_path, content):
    working_directory = os.path.abspath(working_directory)
    file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not (file_path.startswith(os.path.join(working_directory, ''))):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(file_path):
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
        except FileExistsError as e:
            return f'Error: {file_path} already exists: {e}'
        except Exception as e:
            return f'Error: {e}'
    if os.path.exists(working_directory) and os.path.isdir(file_path):
        return f'Error: "{file_path}" is a directory, not a file'
    
    try:
        with open(file_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: Unable to write to "{file_path}": {e}'
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
