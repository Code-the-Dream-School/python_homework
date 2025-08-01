import csv
import os
import custom_module
from datetime import datetime


# Task 2
def read_employees():
    employees_data = {"fields": [], "rows": []}
    try:
        with open("../csv/employees.csv", newline='') as file:
            reader = csv.reader(file)
            employees_data["fields"] = next(reader)
            employees_data["rows"] = [row for row in reader]
    except Exception as e:
       print(f"Error reading CSV file: {e}")
       exit(1)

    return employees_data
employees = read_employees()

# Task 3
def column_index(column_name):
    try:
        return employees["fields"].index(column_name)
    except ValueError:
        print(f"Column '{column_name}' not found.")
        exit(1)

employee_id_column = column_index("employee_id")
# Task 4

def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]

# Task 5

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    try:
        matches = list(filter(employee_match, employees["rows"]))
        return matches
    except Exception as e:
        print(f"'{employee_id}' not found.")
        exit(1)

# Task 6

def employee_find_2(employee_id):
    try:
        matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
        return matches
    except Exception as e:
        print(f"'{employee_id}' not found.")
        exit(1)

# Task 7

def sort_by_last_name():
    try:
        last_name_column = column_index("last_name")
        employees["rows"].sort(key=lambda row: row[last_name_column])
        return employees["rows"]
    except Exception as e:
        print("Not sorted")
        exit(1)

# Task 8

def employee_dict(row):
    result = {}
    fields = employees["fields"]

    if len(row) != len(employees["fields"]):
        raise ValueError("Row length doesn't match the number of fields.")

    for i in range(len(fields)):
        if fields[i] != "employee_id":
            result[fields[i]] = row[i]


    print(employee_dict(employees["rows"][0]))
    return result

# Task 9

def all_employees_dict():
    if not employees.get("fields") or not employees.get("rows"):
        raise ValueError("Invalid or empty data.")

    employee_id_col = column_index("employee_id")

    return {
        str(row[employee_id_col]): employee_dict(row)
        for row in employees["rows"]
        if len(row) == len(employees["fields"])
    }

# Task 10
def get_this_value():
    return os.getenv('THISVALUE')
print(get_this_value())

# Task 11

def set_that_secret(secret):
    custom_module.set_secret(secret)

# Task 12
def read_minutes():
    try:
        minutes_data = {}
        with open('../csv/minutes1.csv', 'r') as file1:
            reader = csv.reader(file1)
            first_row = True
            rows = []
            for row in reader:
                if first_row:
                    first_row = False
                    minutes_data["minutes1"] = {"fields": row}
                else:
                    rows.append(tuple(row))
            minutes_data["minutes1"]["rows"] = rows
        with open('../csv/minutes2.csv', 'r') as file2:
            reader = csv.reader(file2)
            first_row = True
            rows = []
            for row in reader:
                if first_row:
                    first_row = False
                    minutes_data["minutes2"] = {"fields": row}
                else:
                    rows.append(tuple(row))
            minutes_data["minutes2"]["rows"] = rows
        return minutes_data["minutes1"], minutes_data["minutes2"]
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
minutes1, minutes2 = read_minutes()

# Task 13

def create_minutes_set():
    try:
        minutes_set_1 = set(minutes1["rows"])
        minutes_set_2 = set(minutes2["rows"])
        result_set = minutes_set_1.union(minutes_set_2)
        return result_set
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

minutes_set = create_minutes_set()

# Task 14

def create_minutes_list():
    try:
        minutes_list = list(minutes_set)
        minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
        return minutes_list
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

minutes_list = create_minutes_list()

# Task 15


def write_sorted_list():
    try:
        sorted_minutes = sorted(minutes_list, key=lambda x: x[1])
        sorted_minutes = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_minutes))

        with open('./minutes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1['fields'])
            for row in sorted_minutes:
                writer.writerow(row)
        return sorted_minutes
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

sorted_minutes_list = write_sorted_list()
