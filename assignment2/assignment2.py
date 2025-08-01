import csv
import os

# Task 2
def read_employees():
    employees_data = {"fields": [], "rows": []}
    try:
        with open("../csv/employees.csv", newline='') as file:
            reader = csv.reader(file)
        employees_data["fields"] = next(reader)

        employees_data["rows"] = []
        for row in reader:
            employees_data["rows"].append(row)

    except Exception as e:
       print(f"Error reading CSV file: {e}")
       exit(1)

    return employees_data

employees = read_employees()
print(employees)

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

    return result
    print(employee_dict(employees["rows"][0]))


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

        # Task 12

        # Task 13

        # Task 14

        # Task 15
