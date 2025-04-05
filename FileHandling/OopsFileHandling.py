class OopsFileHandler:
    def __init__(self, filename, mode = "r"):
        self.filename = filename
        self.mode = mode
        self.file = None

    def open_file(self):
        try:
            self.file = open(self.filename, self.mode)
            return True
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
            return False
        except IOError:
            print(f"Error opening file {self.filename}.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False
        
    def close_file(self):
        # close the file if opened
        if self.file and not self.file.closed:
            self.file.close()
            return True
        return False

    def read_file(self):
        if not self.file:
            if not self.open_file():
                return None
        try:
            data = self.file.read()
            return data
        except IOError:
            print(f"Error reading file {self.filename}.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
    
    def write_file(self, data):
        if not self.file:
            if not self.open_file():
                return False
        try:
            self.file.write(data)
            return True
        except IOError:
            print(f"Error writing to file {self.filename}.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

def main():
    # Example usage
    filename = 'oopfile.txt'
    file_handler = OopsFileHandler(filename, 'w')

    if file_handler.open_file():
        print(f"File {filename} opened successfully.")
    
    # Writing to the file
        if file_handler.write_file("Hello, World!\n"):
            print(f"Data written to {filename} successfully.")
        
        # Reading from the file
        file_handler = OopsFileHandler(filename, 'r')
        data = file_handler.read_file()
        if data:
            print(f"Data read from {filename}:\n{data}")
        
        file_handler.close_file()
    
if __name__ == "__main__":
    main()