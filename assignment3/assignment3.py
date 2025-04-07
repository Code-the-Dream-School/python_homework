import pandas as pd
import numpy as np

# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames ======================

# Step 1: Create the DataFrame from dictionary and assign to variable
task1_data_frame = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

print("Task 1 DataFrame:")
print(task1_data_frame)

# Step 2: Add new column "Salary"
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]

print("\nTask 1 with Salary:")
print(task1_with_salary)

# Step 3: Modify "Age" column
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1

print("\nTask 1 Older (Age incremented):")
print(task1_older)

# Step 4: Save to CSV
task1_older.to_csv("employees.csv", index=False)
print("\nData saved to 'employees.csv'")


# Task 2: Loading Data from CSV and JSON ===============================================

# Step 1: Load data from CSV file into a new DataFrame
task2_employees = pd.read_csv("employees.csv")
print("Task 2 - Employees from CSV:")
print(task2_employees)

# Step 2: Load data from JSON file into another DataFrame
# Create the JSON manually (if not already present)
import json

json_data = [
    {
        "Name": "Eve",
        "Age": 28,
        "City": "Miami",
        "Salary": 60000
    },
    {
        "Name": "Frank",
        "Age": 40,
        "City": "Seattle",
        "Salary": 95000
    }
]

# Save the JSON data to a file
with open("additional_employees.json", "w") as json_file:
    json.dump(json_data, json_file)

# Now read it into a DataFrame
json_employees = pd.read_json("additional_employees.json")
print("\nTask 2 - Employees from JSON:")
print(json_employees)

# Step 3: Combine the two DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\nTask 2 - Combined Employees:")
print(more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods ==================================

# 1. Use head() to get the first three rows
first_three = more_employees.head(3)
print("First three rows:")
print(first_three)

# 2. Use tail() to get the last two rows
last_two = more_employees.tail(2)
print("\nLast two rows:")
print(last_two)

# 3. Get the shape of the DataFrame
employee_shape = more_employees.shape
print("\nShape of more_employees:")
print(employee_shape)

# 4. Use info() to print summary
print("\nInfo of more_employees DataFrame:")
more_employees.info()

# Task 4: Data Cleaning ======================================

# 1. Load the CSV file
dirty_data = pd.read_csv("assignment3/dirty_data.csv")
print("Original dirty data:")
print(dirty_data)

# 2. Create a clean copy
clean_data = dirty_data.copy()

# 3. Remove duplicate rows
clean_data = clean_data.drop_duplicates()
print("\nAfter removing duplicates:")
print(clean_data)

# 4. Convert Age to numeric, handle non-numeric/missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("\nAfter converting Age to numeric:")
print(clean_data)

# 5. Convert Salary to numeric and replace placeholders with NaN
clean_data['Salary'] = pd.to_numeric(
    clean_data['Salary'].replace(["unknown", "n/a"], np.nan),
    errors='coerce'
)
print("\nAfter converting Salary to numeric and replacing placeholders:")
print(clean_data)

# 6. Fill missing numeric values
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print("\nAfter filling missing values:")
print(clean_data)

# 7. Convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print("\nAfter converting Hire Date to datetime:")
print(clean_data)

# 8. Strip extra whitespace and standardize Name and Department to uppercase
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print("\nAfter cleaning Name and Department:")
print(clean_data)
