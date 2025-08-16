# Task 1
import pandas as pd

task1_data_frame = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
})

task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]

task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1

task1_older.to_csv("employees.csv", index=False)

# Task 2
task2_employees = pd.read_csv("employees.csv")

with open("additional_employees.json", "w") as f:
    f.write("""
[
  {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
  {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]
""")

json_employees = pd.read_json("additional_employees.json")

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)


# Task 3
first_three = more_employees.head(3)
last_two = more_employees.tail(2)
employee_shape = more_employees.shape
more_employees.info()


# Task 4
dirty_data = pd.read_csv("dirty_data.csv")
clean_data = dirty_data.copy()
clean_data = clean_data.drop_duplicates()

clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"].replace({"unknown": None, "n/a": None}), errors="coerce")

clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
clean_data["Hire Date"] = clean_data["Hire Date"].fillna(pd.Timestamp("1900-01-01"))

clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())

clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
