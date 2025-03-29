class Person:
    def __init__(self):
        self.__name = ""
        self.__age = 0

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def displayDetails(self):
        return f"Name: {self.__name}, Age: {self.__age}"

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}"
    
def main():
    person1 = Person()
    person1.set_age(21)
    person1.set_name("Deepak Kumar Karna")
    person1.get_name()
    person1.get_age()

if __name__ == "__main__":
    main()