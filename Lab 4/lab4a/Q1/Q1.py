import os
from datetime import datetime

# Define the base path where the files will be created
base_path = r"E:\Learn\FPT\Python\Github\AI-PFP191\Lab 4\lab4a\Q1"

# Ensure the base directory exists
os.makedirs(base_path, exist_ok=True)

# Task 1: Create an empty text file named 'sales.txt'
sales_file_path = os.path.join(base_path, 'sales.txt')
with open(sales_file_path, 'w') as file:
    pass  # 'pass' is used to create an empty file without writing anything to it

print(f"'sales.txt' created at {sales_file_path}")

# Task 2: Create a file with the current date and time as its name
date_time_file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.txt")
date_time_file_path = os.path.join(base_path, date_time_file_name)
with open(date_time_file_path, 'w') as file:
    pass

print(f"Date-time file created at {date_time_file_path}")

# Task 3: Create a file normally
sample_file_path = os.path.join(base_path, 'sample.txt')
with open(sample_file_path, 'w') as file:
    pass  # 'pass' is used to create an empty file without writing anything to it

print(f"'sample.txt' created at {sample_file_path}")
