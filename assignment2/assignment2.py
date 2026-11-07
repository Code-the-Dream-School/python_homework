
import csv
import os
import custom_module
from datetime import datetime

def read_employees():
    employees = {"fields": [], "rows": []}

    try:
        with open("../csv/employees.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for index, row in enumerate (reader):
                if index == 0:
                    employees["fields"] = row
                else:
                    employees["rows"].append(row)
    
    except Exception as e:
        print("An exception occurred.")
        print(type(e).__name__, str(e))
        raise

    return employees

employees = read_employees()
print(employees)


def column_index(column_name):
    return employees["fields"].index(column_name)


employee_id_column = column_index("employee_id")

def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]

def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))

    return matches

def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id,
            employees["rows"]
        )
    )
    return matches

def sort_by_last_name():
    employees["rows"].sort(
        key=lambda row: row[column_index("last_name")]
    )
    return employees["rows"]

def employee_dict(row):
    employee = {}

    for index, field in enumerate(employees["fields"]):
        if field != "employee_id":
            employee[field] = row[index]
    return employee

def all_employees_dict():
    all_employees = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        all_employees[employee_id] = employee_dict(row)

    return all_employees

def get_this_value():
    return os.getenv("THISVALUE")

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

def read_minutes():
    minutes1 = {"fields": [], "rows": []}
    minutes2 = {"fields": [], "rows": []}

    try:
        with open("../csv/minutes1.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for index, row in enumerate (reader):
                if index == 0:
                    minutes1["fields"] = row
                else:
                    minutes1["rows"].append(tuple(row))
    
        with open("../csv/minutes2.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for index, row in enumerate (reader):
                if index == 0:
                    minutes2["fields"] = row
                else:
                    minutes2["rows"].append(tuple(row))
    
    except Exception as e:
        print("An exception occurred.")
        print(type(e).__name__, str(e))
        raise

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

def create_minutes_set():
    minutes1_set = set(minutes1["rows"])
    minutes2_set = set(minutes2["rows"])

    minutes_set = minutes1_set.union(minutes2_set)

    return minutes_set

minutes_set = create_minutes_set()

def create_minutes_list():
    minutes_list = (minutes_set)

    minutes_list = [
        (name, datetime.strptime(date, "%B %d, %Y"))
        for name, date in minutes_set
    ]

    return minutes_list

minutes_list = create_minutes_list()

def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])

    formatted_list = [
        (name, date.strftime("%B %d, %Y"))
        for name, date in sorted_list
    ]

    try:
        with open("./minutes.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(minutes1["fields"])
            writer.writerows(formatted_list)
    except Exception as e:
        print("An exception occurred.")
        print(type(e).__name__, str(e))
        raise
    
    return formatted_list