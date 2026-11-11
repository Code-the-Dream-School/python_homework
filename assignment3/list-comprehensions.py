import csv


with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)
    employees = list(reader)

names = [employee[1] + " " + employee[2] for employee in employees[1:]]

filtered_names = [name for name in names if "e" in name]

print(names)
print(filtered_names)