import csv
import traceback
import os
import custom_module

def read_employees():
    data = {}
    rows = []

    try:
        with open("csv/employees.csv", newline='') as csvfile:
            reader = csv.reader(csvfile)
            for index, row in enumerate(reader):
                if index == 0:
                    data["fields"] = row  # ['employee_id', 'first_name', 'last_name', 'phone']
                else:
                    rows.append(row)     # Add each employee row
            data["rows"] = rows
            return data

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

# Global variable for output
employees = read_employees()
print(employees)



# Task 3: Find the Column Index
employees = read_employees()

def column_index(column_name):
    return employees["fields"].index(column_name)

# Call the function and store the result in a global variable
employee_id_column = column_index("employee_id")

# Print to verify (optional)
print(f"Index of 'employee_id': {employee_id_column}")

# Task 4: Find the Employee First Name
def first_name(row_number):
    # Get the index of the "first_name" column
    index = column_index("first_name")

    # Get the value at the specified row and column
    return employees["rows"][row_number][index]

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    # Inner function to check if the row matches the given employee_id
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    # Filter rows using the inner function
    matches = list(filter(employee_match, employees["rows"]))
    
    return matches

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    # Using a lambda function to match the employee_id in rows
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    # Using column_index to get the index of the 'last_name' column
    last_name_column = column_index("last_name")
    
    # Sorting the rows in place using the last name from the row
    employees["rows"].sort(key=lambda row: row[last_name_column])
    
    # Returning the sorted rows
    return employees["rows"]

# Task 8: Create a dict for an Employee
def employee_dict(row):
    # Get the list of fields (column headers)
    fields = employees["fields"]
    
    # Create a dictionary excluding the employee_id field
    employee_info = {fields[i]: row[i] for i in range(1, len(fields))}
    
    # Return the resulting dictionary
    return employee_info

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    # Initialize an empty dictionary to hold the employee data
    all_employees = {}

    # Iterate over each row in employees["rows"]
    for row in employees["rows"]:
        # Get the employee_id from the row (assuming the first column is employee_id)
        employee_id = row[0]
        
        # Use employee_dict function to get the employee's data without employee_id
        employee_data = employee_dict(row)
        
        # Add the employee data to the all_employees dictionary with employee_id as the key
        all_employees[employee_id] = employee_data
    
    # Return the resulting dictionary of employee dictionaries
    return all_employees

# Task 10: Use the os Module

# Define the function to get the value of the environment variable THISVALUE
def get_this_value():
    return os.getenv("THISVALUE", None)
print(get_this_value())  # Should print "ABC" if the environment variable is set

# Task 11: Creating Your Own Module

# Function to set the secret in custom_module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)  # Call set_secret in custom_module to set the secret

# Test: Set a new secret and print the updated secret
set_that_secret("newsecret123")
print(custom_module.secret)  # Should print "newsecret123"


# Task 12: Read minutes1.csv and minutes2.csv
def read_csv(file_path):
    minutes = {"fields": [], "rows": []}
    
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            
            # Read fields (headers)
            minutes["fields"] = next(reader)
            
            # Read rows and convert each row to a tuple
            for row in reader:
                minutes["rows"].append(tuple(row))
    
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    
    return minutes

# Function to read both minutes CSV files
def read_minutes():
    minutes1 = read_csv('csv/minutes1.csv')  # Read first file
    minutes2 = read_csv('csv/minutes2.csv')  # Read second file
    return minutes1, minutes2

# Call the function and store the returned values
minutes1, minutes2 = read_minutes()

# Print out the dictionaries to verify
print("Minutes1:", minutes1)
print("Minutes2:", minutes2)

# Task 13: Create minutes_set
from datetime import datetime
def create_minutes_set():
    # Convert rows from minutes1 and minutes2 to sets
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    # Combine the sets using the union operation
    minutes_union = set1.union(set2)

    # Return the resulting set
    return minutes_union

# Call the function and store the result in the global variable
minutes_set = create_minutes_set()

# Print the resulting set to verify
print("Minutes Set:", minutes_set)

# Task 14: Convert to datetime
def create_minutes_list():
    # Convert minutes_set to a list
    minutes_list_temp = list(minutes_set)
    
    # Use map to convert each element
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list_temp))
    
    # Return the resulting list
    return minutes_list

# Call the function and store the result in the global variable
minutes_list = create_minutes_list()

# Print the minutes_list to verify the result
print("Minutes List:", minutes_list)

# Task 15: Write Out Sorted List
def write_sorted_list():
    # Sort minutes_list in ascending order of datetime
    minutes_list_sorted = sorted(minutes_list, key=lambda x: x[1])

    # Convert datetime objects back to string format
    minutes_list_converted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list_sorted))

    # Open the file for writing
    try:
        with open('./minutes.csv', mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write the header row (fields from minutes1)
            writer.writerow(minutes1["fields"])

            # Write the sorted rows
            writer.writerows(minutes_list_converted)

    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

    return minutes_list_converted

# Call the function
# write_sorted_list()