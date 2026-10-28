import csv

# Task 3: List Comprehensions Practice
with open("../csv/employees.csv", newline="") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

header = rows[0]
first_idx = header.index("first_name")
last_idx = header.index("last_name")

# Skip the heading row
names = [row[first_idx] + " " + row[last_idx] for row in rows[1:]]
print(names)

# Only names containing the letter "e"
names_with_e = [name for name in names if "e" in name]
print(names_with_e)
