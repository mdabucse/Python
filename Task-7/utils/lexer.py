from utils.token_types import TokenType
from utils.token import Token

KEYWORDS = {
    "let": TokenType.LET,
    "fn": TokenType.FN,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "return": TokenType.RETURN,
    "print": TokenType.PRINT,
}

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = text[self.pos] if text else None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def number(self):
        result = ""
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(TokenType.INT, int(result))

    def identifier(self):
        result = ""
        while self.current_char and (self.current_char.isalnum() or self.current_char == "_"):
            result += self.current_char
            self.advance()

        token_type = KEYWORDS.get(result, TokenType.IDENT)
        return Token(token_type, result if token_type == TokenType.IDENT else None)

    def string(self):
        self.advance()  # skip opening "
        result = ""
        while self.current_char and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()  # skip closing "
        return Token(TokenType.STRING, result)

    def get_next_token(self):
        while self.current_char:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return self.number()

            if self.current_char.isalpha() or self.current_char == "_":
                return self.identifier()

            if self.current_char == '"':
                return self.string()

            # Operators
            if self.current_char == "+":
                self.advance()
                return Token(TokenType.PLUS)

            if self.current_char == "-":
                self.advance()
                return Token(TokenType.MINUS)

            if self.current_char == "*":
                self.advance()
                return Token(TokenType.MUL)

            if self.current_char == "/":
                self.advance()
                return Token(TokenType.DIV)

            if self.current_char == "=":
                self.advance()
                return Token(TokenType.ASSIGN)

            # Comparisons
            if self.current_char == "<":
                self.advance()
                if self.current_char == "=":
                    self.advance()
                    return Token(TokenType.LTE)
                return Token(TokenType.LT)

            if self.current_char == ">":
                self.advance()
                if self.current_char == "=":
                    self.advance()
                    return Token(TokenType.GTE)
                return Token(TokenType.GT)

            # Symbols
            if self.current_char == "(":
                self.advance()
                return Token(TokenType.LPAREN)

            if self.current_char == ")":
                self.advance()
                return Token(TokenType.RPAREN)

            if self.current_char == "{":
                self.advance()
                return Token(TokenType.LBRACE)

            if self.current_char == "}":
                self.advance()
                return Token(TokenType.RBRACE)

            if self.current_char == ",":
                self.advance()
                return Token(TokenType.COMMA)

            raise Exception(f"Invalid character: {self.current_char}")

        return Token(TokenType.EOF)