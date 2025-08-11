
import csv
import traceback
import os
from datetime import datetime
import custom_module

# Task 2: Read employees.csv and return a dict with fields and rows
def read_employees():
    data = {}
    rows = []
    try:
        with open('csv/employees.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i == 0:
                    data['fields'] = row
                else:
                    rows.append(row)
        data['rows'] = rows
        return data
    except Exception as e:
        print(f"An exception occurred. The exception name is: {type(e).__name__}")
        traceback.print_exc()
        exit(1)

employees = read_employees()
print(employees)

# Task 3: Find the Column Index
def column_index(col_name):
    return employees["fields"].index(col_name)

employee_id_column = column_index("employee_id")

# Task 4: Find the Employee First Name
def first_name(row_num):
    idx = column_index("first_name")
    return employees["rows"][row_num][idx]

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_col = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_col])
    return employees["rows"]

sort_by_last_name()
print(employees)

# Task 8: Create a dict for an Employee
def employee_dict(row):
    return {k: v for k, v in zip(employees["fields"], row) if k != "employee_id"}

print(employee_dict(employees["rows"][0]))

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    eid_col = column_index("employee_id")
    return {row[eid_col]: employee_dict(row) for row in employees["rows"]}

print(all_employees_dict())

# Task 10: Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")

# Task 11: Creating Your Own Module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("my_new_secret")
print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    def read_one_minutes(path):
        d = {}
        rows = []
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i == 0:
                    d['fields'] = row
                else:
                    rows.append(tuple(row))
        d['rows'] = rows
        return d
    m1 = read_one_minutes('csv/minutes1.csv')
    m2 = read_one_minutes('csv/minutes2.csv')
    return m1, m2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

# Task 13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])
    return set1 | set2

minutes_set = create_minutes_set()
print(minutes_set)

# Task 14: Convert to datetime
def create_minutes_list():
    lst = list(minutes_set)
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), lst))

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15: Write Out Sorted List
def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    converted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list))
    with open('minutes.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(minutes1['fields'])
        for row in converted:
            writer.writerow(row)
    return converted

print(write_sorted_list())

