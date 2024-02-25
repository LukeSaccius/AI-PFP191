import os

# Define the base path for Q2
base_path = r"E:\Learn\FPT\Python\Github\AI-PFP191\Lab 4\lab4a\Q2"
os.makedirs(base_path, exist_ok=True)

# Task 1: Write to a new file
new_file_path = os.path.join(base_path, 'new_file.txt')
with open(new_file_path, 'w', encoding='utf-8') as file:
    file.write("Done Writing\nThis is new content\nWrite to a Text file in Python\n")

print(f"New content written to {new_file_path}")

# Task 2: Writing to an existing file (overwriting it)
existing_file_path = os.path.join(base_path, 'existing_file.txt')
with open(existing_file_path, 'w', encoding='utf-8') as file:
    file.write("This is new content\nopening file again...\nThis is overwritten content\n")

print(f"Existing file content overwritten at {existing_file_path}")

# Task 3: Write a list of lines to a file
lines_to_write = ["Name: Emma\n", "Address: 221 Baker Street\n", "City: London\n"]
list_file_path = os.path.join(base_path, 'list_file.txt')
with open(list_file_path, 'w', encoding='utf-8') as file:
    file.writelines(lines_to_write)

print(f"List of lines written to {list_file_path}")
