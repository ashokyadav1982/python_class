class first2:
    a = 1
    b = 'first2'
    c = 2.5

    def printvalues(self):
        print(f"a: {self.a}")
        print(f"b: {self.b}")
        print(f"c: {self.c}")

def main():
    first2obj = first2()
    first2obj.printvalues()

if __name__ == "__main__":
    main()