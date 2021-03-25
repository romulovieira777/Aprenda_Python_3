class Calculator:  # Calculadora

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        result = self.a + self.b
        self.impressao(result)

    def subtraction(self):  # Subtração
        return self.a - self.b

    def impressao(self, a):
        print(a)
