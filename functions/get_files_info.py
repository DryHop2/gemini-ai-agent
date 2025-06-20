import os

def get_files_info(working_directory, directory=None):
    if directory is None:
        directory = working_directory

    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory, directory))

    if not (abs_directory == abs_working_directory or abs_directory.startswith(abs_working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(abs_directory):
        return f'Error: "{directory}" is not a directory'
    
    output = []
    try:
        for entry in os.listdir(abs_directory):
            full_path = os.path.join(abs_directory, entry)
            is_dir = os.path.isdir(full_path)
            if not is_dir and not os.path.isfile(full_path):
                print(f'Error: "{entry}" is not a file or directory')
                continue
            file_size = os.path.getsize(full_path)
            output.append(f'- {entry}: file_size={file_size} bytes, is_dir={is_dir}')
    except OSError as e:
        return f'Error: {entry} does not exist or is inaccessible\n{e}'
    except PermissionError as e:
        return f'Error: Permission denied accessing "{entry}"\n{e}'
    except Exception as e:
        return f'Error: An unexpected error occurred\n{e}'
        
    return '\n'.join(output)