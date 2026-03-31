from utils.token_types import TokenType
from utils.ast_nodes import LetDecl, Literal, PrintStmt, Ident


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f"Expected {token_type}, got {self.current_token.type}")

    def parse(self):
        statements = []

        while self.current_token.type != TokenType.EOF:
            statements.append(self.statement())

        return statements

    def statement(self):
        if self.current_token.type == TokenType.LET:
            return self.let_statement()
        elif self.current_token.type == TokenType.PRINT:
            return self.print_statement()

    def let_statement(self):
        self.eat(TokenType.LET)

        name = self.current_token.value
        self.eat(TokenType.IDENT)

        self.eat(TokenType.ASSIGN)

        value = self.current_token.value
        self.eat(TokenType.INT)

        return LetDecl(name, Literal(value))

    def print_statement(self):
        self.eat(TokenType.PRINT)
        self.eat(TokenType.LPAREN)

        name = self.current_token.value
        self.eat(TokenType.IDENT)

        self.eat(TokenType.RPAREN)

        return PrintStmt(Ident(name))