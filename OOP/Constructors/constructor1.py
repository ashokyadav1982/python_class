class constructor1:
    def __init__(self):
        print("Constructor is called")
    def display(self):
        print("Display method is called")

def main():
    obj = constructor1()
    obj.display()

if __name__ == "__main__":
    main()