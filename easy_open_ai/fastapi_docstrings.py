import sys
import ast
from .functions.text import get_answer_with_instruction


def get_function_definition_line(function_block: str) -> str:
    l = function_block.split("\n")
    for i in l:
        if i.strip().startswith("def ") or i.strip().startswith("async def "):
            return i.strip()


def is_fastapi_decorator(decorator: str) -> bool:
    return (".get('/" or ".post('/") in decorator


def is_fastapi_function(node) -> str:
    for d in node.decorator_list:
        if is_fastapi_decorator(ast.unparse(d)):
            return True
    return False


def extract_all_functions_from_file(file_path) -> dict:
    """ignores a function if it has a docstring though"""
    fastapi_functions = {}
    other_functions = {}

    with open(file_path, "r") as file:
        file_contents = file.read()

    try:
        tree = ast.parse(file_contents)
    except SyntaxError:
        raise Exception("Invalid Python syntax in the file.")

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not ast.get_docstring(node):
                if is_fastapi_function(node):
                    function_body = ast.unparse(node)
                    fastapi_functions[
                        get_function_definition_line(function_body)
                    ] = function_body
                else:
                    function_body = ast.unparse(node)
                    other_functions[
                        get_function_definition_line(function_body)
                    ] = function_body
    return {"fastapi": fastapi_functions, "other": other_functions}


# if __name__ == "__main__":
#     file_path = (
#         "easy_open_ai\\test.py"  # Replace with the path to your Python file
#     )
#     function_dict = extract_fastapi_functions_from_file(file_path)
#     # for function_name, function_block in function_dict.items():
#     #     print(f"Function Name: {function_name}")
#     #     print(f"Function Block:\n{function_block}\n")
#     print(function_dict)


def generate_fastapi_docstring(function_block):
    print("gen_fastapi_docs")
    instruction = """Generate a docstring for a FastAPI endpoint Python source code with the following instructions:

        1. The endpoint is defined in the source code and accessible at http://example.com/api/v1/contacts/, do not include this information in dockstring.
        2. Only include parametes which could be passed as query parameters in url.
        3. Specify that the access to the endpoint requires users to be authenticated, and the allowed roles are "Admin", "Moderator", "User".
        4. Mention that the access JWT token should be passed in the request header for authentication.
        5. Include request limit information in the docstring, specifying the allowed amount of requests per defined time as (10, 60 seconds) respectively.
        6. Write dockstring using this as template:
        # [Short desription]

        ### Description
        [long but not to much description]

        ### Authorization
        - [Authorization information with allowed roles if provided]

        ### Request limit
        - [Reques limit information]

        ### Query Parameters
        - `[parameter]` (**[type]**, [scpecify weather is otional]): [Description] (default: [default value if provided]).

        ### Returns
        - `[Return type]`: [Description]

        ### Raises
        - `[Exeption with HTTP code]`: [Description]

        ### Example
        - [Description]: [[HTTP method]] `[URL example]`
        7. return ONLY docstring to the user 

    """
    question = function_block
    return get_answer_with_instruction(question, instruction, chaos_coefficient=0)


def generate_general_docstring(function_block):
    instruction = '''
    1. Generate a docstring for a Python source code like in this example:

        def add(a: int, b: int) -> int:
            """
            Returns the sum of two integers.

            :param a: The first integer.
            :type a: int
            :param b: The second integer.
            :type b: int
            :return: The sum of a and b.
            :rtype: int
            """
            return a + b
    
    2. return ONLY the docstring to the user .

    '''
    question = function_block
    return get_answer_with_instruction(question, instruction, chaos_coefficient=0)


def count_leading_whitespace(line):
    spaces = 0
    for char in line:
        if char == " ":
            spaces += 1
        elif char == "\t":
            spaces += 4
        else:
            break  # Stop counting when a non-whitespace character is encountered
    return spaces


def get_leading_whitespace(line):
    return " " * (count_leading_whitespace(line) + 4)


def process_file(file_path):
    """
    Processes the given Python file and adds docstrings to functions without one.
    """
    functions = extract_all_functions_from_file(file_path)
    fastapi_func_dict = functions["fastapi"]
    print(fastapi_func_dict)
    others_func_dict = functions["other"]
    print(others_func_dict)
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        new_lines = []
        for line in lines:
            new_lines.append(line)
            print(line.strip())
            if line.strip() in fastapi_func_dict:
                print('here')
                doc = generate_fastapi_docstring(fastapi_func_dict[line.strip()])
                docst = get_leading_whitespace(line) + r'"""' + doc + r'"""' + "\n"
                new_lines.append(docst)
            elif line.strip() in others_func_dict:
                print('here1')
                doc = generate_general_docstring(others_func_dict[line.strip()])
                docst = get_leading_whitespace(line)  + doc  + "\n"
                new_lines.append(docst)

        # Write the updated content to the same file
        with open(file_path, "w") as file:
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
