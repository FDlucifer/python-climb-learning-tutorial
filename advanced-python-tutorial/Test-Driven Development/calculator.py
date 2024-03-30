class Calculator:
    def add(self, x, y):
        if not isinstance(x, int) and not isinstance(x, float):
            if not x.replace('.', '', 1).isnumeric():
                raise TypeError
            x = float(x)
        if not isinstance(y, int) and not isinstance(y, float):
            if not y.replace('.', '', 1).isnumeric():
                raise TypeError
            y = float(y)
        return x + y

    def subtract(self, x, y):
        pass

    def multiply(self, x, y):
        pass

    def divide(self, x, y):
        pass
