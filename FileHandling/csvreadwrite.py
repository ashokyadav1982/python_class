# Handling of a csv file
import csv
def csv_read(file):
    """Read a CSV file and return its contents as a list of dictionaries."""
    try:
        with open(file, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return str(e)
    finally:
        if csvfile and not csvfile.closed:
            csvfile.close()
    
# function to write csv
def csv_write(file, data):
    """Write a list of dictionaries to a CSV file."""
    try:
        with open(file, mode='w', newline='') as csvfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            return "Data written successfully."
    except Exception as e:
        return str(e)
    finally:
        if csvfile and not csvfile.closed:
            csvfile.close()

# main function
def main():
    # Example CSV file path
    csv_read_file = 'csvfile.csv'
    csv_write_file = 'csvwritefile.csv'

    
    # Example data to write to CSV
    data_to_write = [
        {'Name': 'Deepak', 'Age': 30, 'City': 'Kathmandu'},
        {'Name': 'Ram', 'Age': 25, 'City': 'Delhi'},
        {'Name': 'Himal', 'Age': 35, 'City': 'Washington'},
    ]
    
    # Writing to CSV
    write_result = csv_write(csv_write_file, data_to_write)
    print(write_result)
    
    # Reading from CSV
    read_result = csv_read(csv_read_file)
    print(read_result)

if __name__ == "__main__":
    main()