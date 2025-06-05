from functions.get_files_info import get_files_info

tests = [
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../"),
]

for working_dir, target_dir in tests:
    print(f'Test: working_directory="{working_dir}", directory="{target_dir}"')
    print(get_files_info(working_dir, target_dir))
    print("=" * 40)