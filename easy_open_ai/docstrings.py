import sys
import ast


def extract_functions_from_file(file_path) -> dict:
    """ignores a function if it has a docstring though"""
    functions = {}

    with open(file_path, "r") as file:
        file_contents = file.read()

    try:
        tree = ast.parse(file_contents)
    except SyntaxError:
        raise Exception("Invalid Python syntax in the file.")

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not ast.get_docstring(node):
                # function_name = node.name
                function_body = ast.unparse(node)
                functions[function_body.split("\n")[0]] = function_body

    return functions

# if __name__ == "__main__":
#     file_path = (
#         "easy_open_ai\\functions\\text.py"  # Replace with the path to your Python file
#     )
#     function_dict = extract_functions_from_file(file_path)
#     # for function_name, function_block in function_dict.items():
#     #     print(f"Function Name: {function_name}")
#     #     print(f"Function Block:\n{function_block}\n")
#     print(function_dict)

def generate_docstring(function_block):
    return '''test'''

def count_leading_whitespace(line):
    spaces=0
    for char in line:
        if char == ' ':
            spaces += 1
        elif char == '\t':
            spaces += 4
        else:
            break  # Stop counting when a non-whitespace character is encountered
    return spaces

def get_leading_whitespace(line):
    return ' '*(count_leading_whitespace(line)+4)

def process_file(file_path):
    """
    Processes the given Python file and adds docstrings to functions without one.
    """
    func_dict=extract_functions_from_file(file_path)
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        new_lines = []
        for line in lines:
            new_lines.append(line)
            if line.strip() in func_dict:
                docst=get_leading_whitespace(line)+r'"""'+generate_docstring(func_dict[line.strip()])+r'"""'+'\n'
                new_lines.append(docst)
                
        # Write the updated content to the same file
        with open(file_path, 'w') as file:
            file.writelines(new_lines)

    except IOError as e:
        print(f"An IOError occurred: {e.strerror}")

def main():
    """
    Main function to process command-line arguments.
    """
    if len(sys.argv) != 2:
        print("Usage: docstring <file_name.py>")
        sys.exit(1)

    file_name = sys.argv[1]
    process_file(file_name)

if __name__ == "__main__":
    main()