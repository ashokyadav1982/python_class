# A function based program to handle read and write to the file systems

# file read function
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            return data
        
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return str(e)
    finally:
        if file and not file.closed:
            file.close()
    
# file write function
def write_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
            return "Data written successfully."
    except Exception as e:
        return str(e)
    finally:
        if file and not file.closed:
            file.close()

# file append function
def append_file(file_path, data):
    try:
        with open(file_path, 'a') as file:
            file.write(data)
            return "Data appended successfully."
    except Exception as e:
        return str(e)
    finally:
        if file and not file.closed:
            file.close()

def main():
    file_path = 'myfile.txt'
    data_to_write = "Hello, World!\n"
    
    # Writing to file
    write_result = write_file(file_path, data_to_write)
    print(write_result)
    
    # Appending to file
    append_result = append_file(file_path, "Appending this line.\n")
    print(append_result)
    
    # Reading from file
    read_result = read_file(file_path)
    print(read_result)

if __name__ == "__main__":
    main()