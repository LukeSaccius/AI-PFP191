# Let's perform the tasks as described in the user's uploaded image.

# Task 1: Merge two dictionaries
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
merged_dict = {**dict1, **dict2}

# Task 2: Print the value of key 'history'
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
history_value = sampleDict["class"]["student"]["marks"]["history"]

# Task 3: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": "Developer", "salary": 8000}
employees_dict = {emp: defaults.copy() for emp in employees}

# Print results
print(merged_dict)
print(history_value)
print(employees_dict)
