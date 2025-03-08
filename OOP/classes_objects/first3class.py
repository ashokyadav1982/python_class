class first3class:
    
    def printname(self):
        self.name = 'first3'
        self.name = 4
        print(f"name: {self.name}")

def main():
    first3obj = first3class()
    first3obj.printname()

if __name__ == "__main__":
    main()