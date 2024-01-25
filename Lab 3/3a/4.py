import re

# Task 1
str1 = "I am 25 years and 10 months old"
only_integers = re.sub("[^0-9]", "", str1)

# Task 2
str2 = "#Jon is developer & musician"
no_specials = re.sub(r'[^\w\s]', '', str2)

# Task 3
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
cleaned_list = [item for item in str_list if item]

# Task 4
str3 = "Emma-is-a-data-scientist"
split_str = str3.split('-')

# Results
print(f"Task 1: {only_integers}")
print(f"Task 2: {no_specials}")
print(f"Task 3: {cleaned_list}")
print("Task 4:", *split_str, sep='\n')
