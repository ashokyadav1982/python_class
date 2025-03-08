class first2:
    a = 1
    b = 'ashok'
    c = 2.5

    def printvalues(self):
        print(f"a: {self.a}")
        print(f"b: {self.b}")
        print(f"c: {self.c}")

def abc():
    first2obj = first2()
    first2obj.printvalues()

if __name__ == "__main__":
    abc()
    print("End of program")