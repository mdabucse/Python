from utils.lexer import Lexer
from utils.parser import Parser
from utils.interpreter import Interpreter

code = """
let x = 10
print(x)
"""

# LEXER
lexer = Lexer(code)

tokens = []
while True:
    token = lexer.get_next_token()
    tokens.append(token)
    if token.type.name == "EOF":
        break

print("=== Lexer Output ===")
print(tokens)


# PARSER
print("\n=== Parsing... ===")

lexer = Lexer(code)
parser = Parser(lexer)

try:
    ast = parser.parse()
    print("=== AST ===")
    print(ast)
except Exception as e:
    print("❌ Parser Error:", e)


# INTERPRETER
print("\n=== Running... ===")

try:
    interpreter = Interpreter()
    interpreter.run(ast)
except Exception as e:
    print("❌ Interpreter Error:", e)