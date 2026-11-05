import pandas as pd

# 1. Create a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}
task1_data_frame = pd.DataFrame(data)
print("Step 1: original DataFrame")
print(task1_data_frame)
print()

# 2. Add a new column
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
print("Step 2: with Salary")
print(task1_with_salary)
print()

# 3. Modify an existing column
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1
print("Step 3: Age incremented")
print(task1_older)
print()

# 4. Save as CSV without the index
task1_older.to_csv("employees.csv", index=False)
print("Step 4: contents of employees.csv")
with open("employees.csv") as f:
    print(f.read())

