class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayDetails(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
def main():
    person1 = Person("Deepak Kumar Karna", 21)
    person2 = Person("John Doe", 30)
    
    print(f"Person1: {person1}")
    print(f"Person2: {person2}")
    print(person1.displayDetails())
    print(person2.displayDetails())

if __name__ == "__main__":
    main()