class RuleGenerator(dict):
    def __init__(self, symbols, result=None):
        dict.__init__(self, symbols=symbols, result=result)

        self.symbols = symbols
        self.result = result

    def __str__(self):
        if None in self.symbols:
            return "|- " + self.result
        return ", ".join(self.symbols) + " |- " + self.result
