class first4class:
    def assignvalue(self, value):
        self.value = value

    def printvalue(self):
        print(f"value: {self.value}")

def main():
    first4obj = first4class()
    first4obj.assignvalue("Deepak Kumar Karna")
    first4obj.printvalue()

if __name__ == "__main__":
    main()