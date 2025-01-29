# First class program on OOP

class FirstClass:
    firstnum = 1
    second_num = 2

    def add(self):
        return self.firstnum + self.second_num
    
    def subtract(self):
        return self.firstnum - self.second_num
    
    def multiply(self):
        return self.firstnum * self.second_num
    
    def divide(self):
        return self.firstnum / self.second_num
    

def main():
    firstclass = FirstClass()
    print(f"Addition: {firstclass.add()}")
    print(f"Subtraction: {firstclass.subtract()}")
    print(f"Multiplication: {firstclass.multiply()}")
    print(f"Division: {firstclass.divide()}")

if __name__ == "__main__":
    main()
