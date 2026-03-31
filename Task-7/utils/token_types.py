from enum import Enum, auto

class TokenType(Enum):
    # Keywords
    LET = auto()
    FN = auto()
    IF = auto()
    ELSE = auto()
    RETURN = auto()
    PRINT = auto()

    # Identifiers + literals
    IDENT = auto()
    INT = auto()
    STRING = auto()

    # Operators
    PLUS = auto()
    MINUS = auto()
    MUL = auto()
    DIV = auto()
    ASSIGN = auto()

    # Comparisons
    LT = auto()
    LTE = auto()
    GT = auto()
    GTE = auto()
    EQ = auto()
    NEQ = auto()

    # Symbols
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    COMMA = auto()

    EOF = auto()
