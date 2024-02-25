import os
from datetime import datetime
import shutil

# Define the base path for Q4
base_path = r"E:\Learn\FPT\Python\Github\AI-PFP191\Lab 4\lab4a\Q4"
os.makedirs(base_path, exist_ok=True)

# Task 1: Rename a file after checking whether it exists
def rename_file_if_exists(original, new_name):
    original_path = os.path.join(base_path, original)
    new_path = os.path.join(base_path, new_name)
    if os.path.exists(original_path):
        os.rename(original_path, new_path)
        print(f"File renamed from {original} to {new_name}")
    else:
        print(f"The file {original} does not exist.")

# Example usage
rename_file_if_exists('test.txt', 'sales_1.txt')

# Task 2: Rename multiple files
def rename_multiple_files():
    files_to_rename = ['sales_1.txt', 'sales_2.txt']
    for filename in files_to_rename:
        original_path = os.path.join(base_path, filename)
        new_name = f"new_{filename}"
        new_path = os.path.join(base_path, new_name)
        if os.path.exists(original_path):
            os.rename(original_path, new_path)
            print(f"File renamed from {filename} to {new_name}")
        else:
            print(f"The file {filename} does not exist.")

rename_multiple_files()

# Task 3: Renaming only a list of files in a folder
# Assuming the list of files is already defined, similar to Task 2

# Task 4: Renaming files with a timestamp
def rename_files_with_timestamp():
    timestamp = datetime.now().strftime("%d-%b-%Y")
    files_to_rename = ['sales_1_new.txt', 'sales_2_new.txt']
    for filename in files_to_rename:
        original_path = os.path.join(base_path, filename)
        new_name = f"{filename.split('.')[0]}_{timestamp}.txt"
        new_path = os.path.join(base_path, new_name)
        if os.path.exists(original_path):
            os.rename(original_path, new_path)
            print(f"File renamed from {filename} to {new_name}")
        else:
            print(f"The file {filename} does not exist.")

rename_files_with_timestamp()

# Task 5: Renaming the extension of the files
def rename_file_extensions():
    files_to_rename = ['sales_1_new.pdf', 'sales_2_new.pdf']  # Assuming these are the initial file names
    for filename in files_to_rename:
        original_path = os.path.join(base_path, filename)
        new_name = f"{filename.split('.')[0]}.txt"
        new_path = os.path.join(base_path, new_name)
        if os.path.exists(original_path):
            os.rename(original_path, new_path)
            print(f"File extension changed from {filename} to {new_name}")
        else:
            print(f"The file {filename} does not exist.")

rename_file_extensions()

# Task 6: Renaming and then moving a file to a new location
def rename_and_move_file(original, new_name, new_folder):
    original_path = os.path.join(base_path, original)
    new_folder_path = os.path.join(base_path, new_folder)
    os.makedirs(new_folder_path, exist_ok=True)  # Create the new
