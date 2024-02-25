import os
from datetime import datetime

# Task 1: Create a new empty text file named 'sales.txt'
open('sales.txt', 'w').close()

# Task 2: Create a file with a DateTime in the name
datetime_filename = datetime.now().strftime('created_%Y-%m-%d-%H-%M-%S.txt')
open(datetime_filename, 'w').close()

# Task 3: Create a file with Permission
# Note: File permissions are handled differently on Windows, but you can still create the file normally
sample_filename = 'sample.txt'
open(sample_filename, 'w').close()
# If you need to set specific permissions on Unix, you would use os.chmod here
# os.chmod(sample_filename, 0o644)  # Read/write by owner, read by others

print("Files created successfully.")
