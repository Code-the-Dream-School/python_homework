import pandas as pd
import numpy as np

# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(data)
print("Task 1 DataFrame:")
print(task1_data_frame)

# Add a new column Salary
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("\nTask 1 with Salary:")
print(task1_with_salary)

# Modify an existing column (increment Age by 1)
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print("\nTask 1 Older (Age + 1):")
print(task1_older)

# Save to CSV (without index)
task1_older.to_csv('employees.csv', index=False)
print("\nSaved task1_older DataFrame to employees.csv")

# Task 2: Loading Data from CSV and JSON

# Load CSV file created above
task2_employees = pd.read_csv('employees.csv')
print("\nTask 2 Loaded CSV DataFrame:")
print(task2_employees)

# Create JSON file (additional_employees.json)
import json
additional_employees = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]

with open('additional_employees.json', 'w') as f:
    json.dump(additional_employees, f)

# Load JSON file
json_employees = pd.read_json('additional_employees.json')
print("\nTask 2 Loaded JSON DataFrame:")
print(json_employees)

# Combine DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\nCombined DataFrame (more_employees):")
print(more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods

# Use head() - first 3 rows
first_three = more_employees.head(3)
print("\nFirst three rows:")
print(first_three)

# Use tail() - last 2 rows
last_two = more_employees.tail(2)
print("\nLast two rows:")
print(last_two)

# Shape of DataFrame
employee_shape = more_employees.shape
print("\nShape of more_employees DataFrame:")
print(employee_shape)

# info() summary
print("\nInfo summary of more_employees:")
more_employees.info()

# Task 4: Data Cleaning

# Load dirty_data.csv into DataFrame
dirty_data = pd.read_csv('dirty_data.csv')
print("\nDirty Data:")
print(dirty_data)

# Make a copy for cleaning
clean_data = dirty_data.copy()

# Remove duplicates
clean_data = clean_data.drop_duplicates()
print("\nAfter removing duplicates:")
print(clean_data)

# Convert Age to numeric, coerce errors, handle missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("\nAfter converting Age to numeric:")
print(clean_data)

# Convert Salary to numeric, replacing placeholders with NaN
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], np.nan)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print("\nAfter cleaning Salary:")
print(clean_data)

# Fill missing values: Age with mean, Salary with median
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print("\nAfter filling missing Age and Salary:")
print(clean_data)

# Convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print("\nAfter converting Hire Date to datetime:")
print(clean_data)

# Strip whitespace and uppercase Name and Department
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print("\nAfter stripping and uppercasing Name and Department:")
print(clean_data)
