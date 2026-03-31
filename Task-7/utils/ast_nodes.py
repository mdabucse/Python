class Program:
    def __init__(self, statements):
        self.statements = statements


class FunctionDecl:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body


class IfStatement:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class ReturnStmt:
    def __init__(self, value):
        self.value = value


class LetDecl:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"LetDecl({self.name}, {self.value})"


class Call:
    def __init__(self, name, args):
        self.name = name
        self.args = args


class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Literal:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Literal({self.value})"


class Ident:
    def __init__(self, name):
        self.name = name


class PrintStmt:
    def __init__(self, value):
        self.value = value
    
class PrintStmt:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"PrintStmt({self.value})"


class Ident:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Ident({self.name})"