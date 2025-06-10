import os
import subprocess


def run_python_file(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not (abs_file_path.startswith(os.path.join(abs_working_directory, ''))):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if abs_file_path.split('.')[-1] != 'py':
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(["python3", abs_file_path], 
                       timeout=30, 
                       capture_output=True, 
                       cwd=working_directory,
                       text=True)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    output_parts = []

    if result.stdout:
        output_parts.append("STDOUT:\n" + result.stdout.strip())
    if result.stderr:
        output_parts.append("STDERR:\n" + result.stderr.strip())
    if result.returncode != 0:
        output_parts.append(f'Process exited with code {result.returncode}')
    if not output_parts:
        return "No output produced."
    
    return "\n\n".join(output_parts)