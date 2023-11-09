# import sys
# import re

# def generate_docstring(function_name):
#     return f"'''test_text_{function_name}'''"

# def process_file(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()

#     # Use regular expression to find function names
#     function_names = re.findall(r'def (\w+)\(', content)

#     if not function_names:
#         print("No functions found in the file.")
#         return

#     # Create a new content with updated docstrings
#     new_content = content
#     for function_name in function_names:
#         docstring = generate_docstring(function_name)
#         new_content = re.sub(
#             rf'def {function_name}\(', f'def {function_name}(', new_content)
#         new_content = re.sub(
#             rf'def {function_name}\(', f'def {function_name}:\n    {docstring}\n', new_content
#         )

#     # Write the updated content back to the file
#     with open(file_path, 'w') as file:
#         file.write(new_content)

# def main():
#     if len(sys.argv) != 2:
#         print("Usage: easy-open-ai <file_name.py>")
#         sys.exit(1)

#     file_name = sys.argv[1]
#     process_file(file_name)

# if __name__ == "__main__":
#     main()
import sys
import re

def generate_docstring(function_name):
    return f"'''test_text_{function_name}'''"

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Use regular expression to find function names and their docstrings
    function_matches = re.finditer(r'def (\w+)\(([^)]*)\):(\s*["\']{3}.*?["\']{3})?', content, re.MULTILINE | re.DOTALL)

    if not function_matches:
        print("No functions found in the file.")
        return

    # Create a new content with updated docstrings
    new_content = content
    for match in function_matches:
        function_name = match.group(1)
        existing_docstring = match.group(3)

        if existing_docstring:
            continue  # Skip functions with existing docstrings

        docstring = generate_docstring(function_name)
        replacement = f'def {function_name}({match.group(2)}):\n    {docstring}\n'
        new_content = new_content[:match.start()] + replacement + new_content[match.end():]

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(new_content)

def main():
    if len(sys.argv) != 2:
        print("Usage: docstring <file_name.py>")
        sys.exit(1)

    file_name = sys.argv[1]
    process_file(file_name)

if __name__ == "__main__":
    main()