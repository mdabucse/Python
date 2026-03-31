class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value is None:
            return f"{self.type.name}"
        
        if isinstance(self.value, str):
            return f'{self.type.name}("{self.value}")'
        
        return f"{self.type.name}({self.value})"