
#Imports

import csv
import traceback
import os
from datetime import datetime
import custom_module




# Task 2: Reading CSV File
def read_employees():
    try:
        with open("../csv/employees.csv", newline="") as file:
            reader = csv.reader(file)
            fields = next(reader)
            rows = list(reader)
            return {"fields": fields, "rows": rows}
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        for trace in trace_back:
            print(f"File: {trace[0]}, Line: {trace[1]}, Func: {trace[2]}, Message: {trace[3]}")
        print("Error occurred while reading the CSV file.")
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {str(e)}")
        exit()

employees = read_employees()  # Initializing globally, only once

# Task 3: Find Column Index
def column_index(col_name):
    return employees["fields"].index(col_name) # Getting the index of the column name

employee_id_column = column_index("employee_id")
print("employee_id column index:", employee_id_column)
print("first_name column index:", column_index("first_name"))

# Task 4: Find First Name
def first_name(row_num):
    col = column_index("first_name")
    return employees["rows"][row_num][col]
print("\n---- Task 4: First Name ----")
print("First name in row 0:", first_name(0))

# Task 5: Find Employee with Nested Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches
print("\n---- Task 5: employee_find ----")
print("Employee with ID 3:", employee_find(3))

# Task 6: Lambda version of employee_find
def employee_find_2(employee_id):
    return list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
print("\n---- Task 6: employee_find_2 (lambda) ----")
print("Employee with ID 3 (lambda):", employee_find_2(3))

# Task 7: Sort by Last Name
def sort_by_last_name():
    last_name_col = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_col])
    return employees["rows"]
print("\n---- Task 7: Sorted by Last Name ----")
sort_by_last_name()
print("First 3 after sort:", employees["rows"][:3])

# Task 8: Create employee_dict
def employee_dict(row):
    fields = employees["fields"]
    return {k: v for i, (k, v) in enumerate(zip(fields, row)) if k != "employee_id"}
print("\n---- Task 8: employee_dict ----")
print("Employee dict from row 0:", employee_dict(employees["rows"][0]))

# Task 9: All employees dict
def all_employees_dict():
    return {row[employee_id_column]: employee_dict(row) for row in employees["rows"]}
print("\n---- Task 9: all_employees_dict ----")
all_emps = all_employees_dict()
print("Employee 1 info:", all_emps["1"])

# Task 10: Get environment variable
def get_this_value():
    return os.getenv("THISVALUE")
print("\n---- Task 10: Get THISVALUE from env ----")
print("THISVALUE:", get_this_value())

# Task 11: Custom module interaction
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("abracadabra")
print(custom_module.secret)

print("\n---- Task 11: Custom Module ----")
print("custom_module.secret after setting:", custom_module.secret)

# Task 12: Read minutes1 and minutes2 as tuples
def read_minutes():
    def read_file(path):
        data = {}
        rows = []
        with open(path, newline="") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(tuple(row))
        data["rows"] = rows
        return data

    return read_file("../csv/minutes1.csv"), read_file("../csv/minutes2.csv")

minutes1, minutes2 = read_minutes()
print("\n---- Task 12: Read Minutes ----")
print("Minutes1 sample:", minutes1["rows"][:2])
print("Minutes2 sample:", minutes2["rows"][:2])

# Task 13: Combine rows into a set
def create_minutes_set():
    return set(minutes1["rows"]).union(set(minutes2["rows"]))

minutes_set = create_minutes_set()
print("\n---- Task 13: Union of Minutes ----")
print("Minutes set sample:", list(minutes_set)[:3])

# Task 14: Convert to datetime
def create_minutes_list():
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))

minutes_list = create_minutes_list()
print("\n---- Task 14: Convert to datetime ----")
print("Minutes list sample:", minutes_list[:3])

# Task 15: Sort + write csv
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    converted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))
    with open("./minutes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted)
    return converted

write_sorted_list()
print("\n---- Task 15: Write sorted CSV ----")
final_minutes = write_sorted_list()
print("Wrote minutes.csv with rows like:", final_minutes[:3])