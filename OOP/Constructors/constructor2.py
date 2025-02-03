class constructor2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

def main():
    obj = constructor2("Deepak Kumar Karna", 21)
    obj.display()

if __name__ == "__main__":
    main()