import csv

with open("../csv/employees.csv", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

employee_names = [f"{row[0]} {row[1]}" for row in data[1:]]
print(employee_names)

names_with_e = [name for name in employee_names if 'e' in name.lower()]
print(names_with_e)
