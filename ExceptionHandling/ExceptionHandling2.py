class Exception2:
    def __init__(self, a, b):
        self.firstnum = a
        self.secondnum = b

    def divide(self):
        try:
            result = self.firstnum / self.secondnum
            return result
        except ZeroDivisionError as e:
            print(f"Error: Division by zero is not allowed. {e}")
        except TypeError as e:
            print(f"Error: Invalid input types. {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        finally:
            print("Execution of the divide method is complete.")

# Call the class and function

def main():
    firstcalc = Exception2(10, 2)
    print(firstcalc.divide())
    secondcalc = Exception2(10, 0)
    print(secondcalc.divide())
    thirdcalc = Exception2(10, "a")
    print(thirdcalc.divide())

if __name__ == "__main__":
    main()



    