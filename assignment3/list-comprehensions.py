import csv

with open("csv/employees.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# Skip header
data_no_header = data[1:]

# Filter out any empty or incomplete rows
filtered_data = [row for row in data_no_header if len(row) >= 3]

# Create full names list
full_names = [f"{row[1]} {row[2]}" for row in filtered_data]
print("All employee names:")
print(full_names)

# Filter names containing the letter "e"
names_with_e = [name for name in full_names if 'e' in name.lower()]
print("\nNames containing 'e':")
print(names_with_e)
