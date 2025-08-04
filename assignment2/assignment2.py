# assignment2.py
import csv
import traceback
import os
from datetime import datetime
import custom_module

# Globals
employees = {}
employee_id_column = None
minutes1 = {}
minutes2 = {}
minutes_set = set()
minutes_list = []

# Task 2: Read a CSV File
def read_employees():
    d = {}
    rows = []
    try:
        with open("../csv/employees.csv", newline='') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    d["fields"] = row
                else:
                    rows.append(row)
        d["rows"] = rows
        return d
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit(1)

employees = read_employees()
print("Employees loaded:", employees)

# Task 3: Find Column Index
def column_index(col_name: str):
    return employees["fields"].index(col_name)

employee_id_column = column_index("employee_id")
print("Employee ID column index:", employee_id_column)

# Task 4: Find Employee First Name
def first_name(row_num: int):
    idx = column_index("first_name")
    return employees["rows"][row_num][idx]

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6: Find Employee with Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# Task 7: Sort rows by last_name using lambda
def sort_by_last_name():
    idx = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[idx])
    return employees["rows"]

# Call and print sorted employees for demo
sorted_rows = sort_by_last_name()
print("Employees sorted by last name:", employees)

# Task 8: Create dict for an employee row
def employee_dict(row):
    result = {}
    for key, val in zip(employees["fields"], row):
        if key != "employee_id":
            result[key] = val
    return result

print("Employee dict for first row:", employee_dict(employees["rows"][0]))

# Task 9: Dict of dicts for all employees
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        emp_id = row[employee_id_column]
        result[emp_id] = employee_dict(row)
    return result

print("All employees dict of dicts:", all_employees_dict())

# Task 10: Use os module
def get_this_value():
    return os.getenv("THISVALUE")

# Task 11: Create your own module and function
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("NewSecretValue123")
print("Custom module secret:", custom_module.secret)

# Helper function for reading csv to dict with tuple rows
def read_csv_to_dict_tuple(filepath):
    d = {}
    rows = []
    try:
        with open(filepath, newline='') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    d["fields"] = row
                else:
                    rows.append(tuple(row))
        d["rows"] = rows
        return d
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit(1)

# Task 12: Read minutes1 and minutes2
def read_minutes():
    global minutes1, minutes2
    minutes1 = read_csv_to_dict_tuple("../csv/minutes1.csv")
    minutes2 = read_csv_to_dict_tuple("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print("Minutes1:", minutes1)
print("Minutes2:", minutes2)

# Task 13: Create minutes_set (union of unique rows)
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)

minutes_set = create_minutes_set()
print("Minutes combined set:", minutes_set)

# Task 14: Convert to datetime in list
def create_minutes_list():
    lst = list(minutes_set)
    converted = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), lst))
    return converted

minutes_list = create_minutes_list()
print("Minutes list with datetime:", minutes_list)

# Task 15: Write out sorted list
def write_sorted_list():
    # Sort by datetime
    sorted_list = sorted(minutes_list, key=lambda x: x[1])

    # Convert datetime back to string format
    converted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list))

    # Write to CSV
    with open("minutes.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])  # Write header
        writer.writerows(converted)

    return converted

write_sorted_list()
print("Sorted minutes.csv written.")

# If you want to add any calls or print here, you can do so



