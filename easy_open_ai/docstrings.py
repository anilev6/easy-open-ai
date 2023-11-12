import sys
import ast
import astor
from .functions.text import get_answer_with_instruction


def generate_fastapi_docstring(function_block):
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
    instruction = """
    You are a docstring assistant. Generate a docstring for a Python source code like in this example:

        user:

        def add(a: int, b: int) -> int:
            return a + b

        assistant:

            Returns the sum of two integers.

            :param a: The first integer.
            :type a: int
            :param b: The second integer.
            :type b: int
            :return: The sum of a and b.
            :rtype: int

    """
    question = function_block
    return get_answer_with_instruction(question, instruction, chaos_coefficient=0)


def is_fastapi_decorator(decorator: str) -> bool:
    return ('.get("/' or ".get('/" or ".post('/" or '.post("/' or ".delete('/" or '.delete("/' or ".put('/" or '.put("/') in decorator


def is_fastapi_function(node) -> str:
    for d in node.decorator_list:
        if is_fastapi_decorator(ast.unparse(d)):
            return True
    return False


def create_docstring(function_node):
    if is_fastapi_function(function_node):
        docstring = generate_fastapi_docstring(ast.unparse(function_node))
    else:
        docstring = generate_general_docstring(ast.unparse(function_node))
    docstring_node = ast.Expr(ast.Str(docstring))
    function_node.body.insert(0, docstring_node)


def process_file(input_file, output_file):
    with open(input_file, "r") as file:
        source_code = file.read()

    tree = ast.parse(source_code)

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not ast.get_docstring(node):
                create_docstring(node)

    modified_source_code = astor.to_source(tree)

    with open(output_file, "w") as file:
        file.write(modified_source_code)


def main():
    """
    Main function to process command-line arguments.
    """
    if len(sys.argv) != 2:
        print("Usage: docstring <file_name.py>")
        sys.exit(1)

    file_name = sys.argv[1]
    input_file = file_name
    output_file = input_file

    process_file(input_file, output_file)


if __name__ == "__main__":
    main()
