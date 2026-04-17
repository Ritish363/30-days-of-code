import ast

def explain_code(code):
    tree = ast.parse(code)

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            print(f"Function defined: {node.name}")

        elif isinstance(node, ast.For):
            print("Contains a for loop")

        elif isinstance(node, ast.While):
            print("Contains a while loop")

        elif isinstance(node, ast.Assign):
            print("Variable assignment detected")

file = input("Enter Python file name: ")

with open(file, "r", encoding="utf-8", errors="ignore") as f:
    code = f.read()

print("\nAnalysis:")
explain_code(code)