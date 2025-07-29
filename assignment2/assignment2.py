# Task 2: Read a CSV File
import csv
import os
import traceback
from datetime import datetime
import custom_module


# Globals used throughout the tasks
employees = {}
employee_id_column = None
minutes1 = {}
minutes2 = {}
minutes_set = set()
minutes_list = []

# Task 2: Read the employees.csv and return dict
def read_employees():
    data = {}
    rows = []
    try:
        with open("../csv/employees.csv", newline="") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(row)
            data["rows"] = rows
            return data
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

# Load and print employees for verification
employees = read_employees()
print(employees)

# Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

# Task 4: Find the Employee First Name
def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]

# Task 5: Find the Employee using filter with inner function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    return list(filter(employee_match, employees["rows"]))

# Task 6: Find the Employee using Lambda
def employee_find_2(employee_id):
    return list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))

# Task 7: Sort rows by last name
def sort_by_last_name():
    index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[index])
    return employees["rows"]

sort_by_last_name()
print(employees)

# Task 8: Create a dict for an employee (excluding employee_id)
def employee_dict(row):
    fields = employees["fields"]
    return {fields[i]: row[i] for i in range(len(fields)) if i != employee_id_column}

print(employee_dict(employees["rows"][0]))

# Task 9: Create a dict of dicts for all employees
def all_employees_dict():
    return {row[employee_id_column]: employee_dict(row) for row in employees["rows"]}

print(all_employees_dict())

# Task 10: Use os module to get environment variable
def get_this_value():
    return os.getenv("THISVALUE")

# Task 11: Use custom_module to set secret value
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("abracadabra")
print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv with tuple rows
def read_csv_as_dict(path):
    result = {}
    rows = []
    try:
        with open(path, newline="") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    result["fields"] = row
                else:
                    rows.append(tuple(row))
            result["rows"] = rows
            return result
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

def read_minutes():
    global minutes1, minutes2
    minutes1 = read_csv_as_dict("../csv/minutes1.csv")
    minutes2 = read_csv_as_dict("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

# Task 13: Create minutes_set by union of both sets
def create_minutes_set():
    global minutes_set
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    minutes_set = set1.union(set2)
    return minutes_set

minutes_set = create_minutes_set()
print(minutes_set)

# Task 14: Convert date string to datetime object
def create_minutes_list():
    global minutes_list
    minutes_list = list(minutes_set)
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return minutes_list

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15: Sort and write the final minutes list to a CSV file
def write_sorted_list():
    global minutes_list
    minutes_list.sort(key=lambda x: x[1])
    minutes_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))
    try:
        with open("minutes.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(minutes1["fields"])
            for row in minutes_list:
                writer.writerow(row)
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    return minutes_list

write_sorted_list()
