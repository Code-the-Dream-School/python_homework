import pandas as pd

#Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
#1.1. Create a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}
task1_data_frame = pd.DataFrame(data)
print("Step 1: original DataFrame")
print(task1_data_frame)
print()

#1.2. Add a new column
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
print("Step 2: with Salary")
print(task1_with_salary)
print()

#1.3. Modify an existing column
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1
print("Step 3: Age incremented")
print(task1_older)
print()

#1.4. Save as CSV without the index
task1_older.to_csv("employees.csv", index=False)
print("Step 4: contents of employees.csv")
with open("employees.csv") as f:
    print(f.read())

#Task 2: Loading Data from CSV and JSON
#2.1. Read the CSV from Task 1
task2_employees = pd.read_csv("employees.csv")
print("Task 2.1: task2_employees")
print(task2_employees)
print()

#2.2. Read the JSON file
json_employees = pd.read_json("additional_employees.json")
print("Task 2.2: json_employees")
print(json_employees)
print()

#2.3. Combine, resetting the index to 0-4
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("Task 2.3: more_employees")
print(more_employees)
print()

#Task 3: Data Inspection - Using Head, Tail, and Info Methods
#3.1. First three rows
first_three = more_employees.head(3)
print(first_three)

#3.2. Last two rows
last_two = more_employees.tail(2)
print(last_two)

#3.3. Shape
employee_shape = more_employees.shape
print(employee_shape)

#3.4. Summary
more_employees.info()

#Task 4: Data Cleaning
#Task 4.1. Load raw data, then copy
dirty_data = pd.read_csv("dirty_data.csv")
print(dirty_data)
clean_data = dirty_data.copy()

#Task 4.2. Remove duplicates
clean_data = clean_data.drop_duplicates()
print(clean_data)

#Task 4.3. Age to numeric
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print(clean_data)

#Task 4.4. Salary: strip, replace placeholders, convert
clean_data["Salary"] = clean_data["Salary"].astype(str).str.strip()
clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print(clean_data)

#Task 4.5. Fill missing values
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())
print(clean_data)

#Task 4.6. Hire Date to datetime (mixed formats)
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"].str.strip(), format="mixed")
print(clean_data)

#Task 4.7. Standardize text
clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
print(clean_data)