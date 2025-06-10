from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


def test():
    # tests = [
    #     ("calculator", "."),
    #     ("calculator", "pkg"),
    #     ("calculator", "/bin"),
    #     ("calculator", "../"),
    # ]

    # for working_dir, target_dir in tests:
    #     print(f'Test: working_directory="{working_dir}", directory="{target_dir}"')
    #     print(get_files_info(working_dir, target_dir))
    #     print("=" * 40)

    tests = [
        ("calculator", "main.py"),
        ("calculator", "pkg/calculator.py"),
        ("calculator", "/bin/cat")
    ]

    for working_dir, file_path in tests:
        print(f'Test: working_directory="{working_dir}", file_path="{file_path}"')
        print(get_file_content(working_dir, file_path))
        print("=" * 40)

if __name__ == "__main__":
    test()