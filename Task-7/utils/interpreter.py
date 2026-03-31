class Interpreter:
    def __init__(self):
        self.env = {}  # variable storage

    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name)
        return method(node)

    def run(self, statements):
        for stmt in statements:
            self.visit(stmt)

    def visit_LetDecl(self, node):
        value = self.visit(node.value)
        self.env[node.name] = value

    def visit_Literal(self, node):
        return node.value

    def visit_Ident(self, node):
        return self.env[node.name]

    def visit_PrintStmt(self, node):
        value = self.visit(node.value)
        print(value)