import os
from datetime import datetime

# Task 1: Rename a file after checking whether it exists
def rename_file(old_name, new_name):
    if os.path.isfile(old_name):
        os.rename(old_name, new_name)
        print(f"{old_name} has been renamed to {new_name}")
    else:
        print(f"The file {old_name} does not exist.")

# Task 2: Rename Multiple Files in Python
def rename_multiple_files(folder_path, old_extension, new_extension):
    for filename in os.listdir(folder_path):
        if filename.endswith(old_extension):
            new_filename = filename.replace(old_extension, new_extension)
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            print(f"{filename} renamed to {new_filename}")

# Task 3: Renaming only a list of files in a folder
def rename_specific_files(folder_path, files_to_rename, new_extension):
    for filename in files_to_rename:
        old_file = os.path.join(folder_path, filename)
        if os.path.isfile(old_file):
            new_filename = filename.replace('.txt', new_extension)
            os.rename(old_file, os.path.join(folder_path, new_filename))
            print(f"{filename} renamed to {new_filename}")

# Task 4: Renaming files with a timestamp
def rename_files_with_timestamp(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            timestamp = datetime.now().strftime("%d-%b-%Y")
            new_filename = f"{filename[:-4]}-{timestamp}.txt"
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            print(f"{filename} renamed to {new_filename}")

# Task 5: Renaming the Extension of the Files
def rename_file_extensions(folder_path, old_extension, new_extension):
    for filename in os.listdir(folder_path):
        if filename.endswith(old_extension):
            new_filename = filename.replace(old_extension, new_extension)
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            print(f"{filename} renamed to {new_filename}")

# Task 6: Renaming and then moving a file to a new location
def rename_and_move_file(old_path, new_path, new_name):
    if os.path.isfile(old_path):
        os.rename(old_path, new_path)
        print(f"{old_path} has been moved and renamed to {new_path}")
    else:
        print(f"The file {old_path} does not exist.")

# Example usage:
rename_file('oldname.txt', 'newname.txt')
rename_multiple_files('path_to_folder', '.txt', '.new')
rename_specific_files('path_to_folder', ['file1.txt', 'file2.txt'], '.new')
rename_files_with_timestamp('path_to_folder')
rename_file_extensions('path_to_folder', '.txt', '.pdf')
rename_and_move_file('path_to_folder/oldname.txt', 'new_folder/newname.txt', 'newname.txt')
