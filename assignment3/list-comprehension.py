import csv
with open("csv/employees.csv", "r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)


# 2b: List Comprehensions
names = ["Alice", "Bob", "Charlie", "Denton", "Williams", "Martherton"]
# Create a new list with names containing 'e'
names_with_e = [name for name in names if 'e' in name]
print(names_with_e)


 