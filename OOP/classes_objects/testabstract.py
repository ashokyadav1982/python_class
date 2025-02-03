class calculator_new:
    a = 1
    b = 1

    def assignvalues(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b
    
def main():
    calc = calculator_new()
    calc.assignvalues(10, 20)
    print(f"Addition: {calc.add()}")
    print(f"Subtraction: {calc.subtract()}")
    print(f"Multiplication: {calc.multiply()}")
    print(f"Division: {calc.divide()}")

if __name__ == "__main__":
    main()