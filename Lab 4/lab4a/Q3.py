# Task 1: Seek the Beginning of the File
with open('test.txt', 'r+') as file:
    file.seek(0)  # Move to the beginning of the file
    print(file.readline().strip())  # Read and print the first line

# Task 2: Seeking the End of File
with open('test.txt', 'a') as file:  # Open in append mode, which seeks to the end of the file
    file.write('\nThis content is added to the end of the file')

# Task: Move the file pointer 5 bytes forward from the current position in binary mode
with open('test.txt', 'rb+') as file:
    file.seek(5, 1)  # Move 5 bytes forward from the current position
    print(file.read().decode('utf-8'))  # Read and print the rest of the file


# Task 4: Seek backward With Negative Offset - 5 characters back from the end
# This requires binary mode to use negative seek.
with open('test.txt', 'rb+') as file:
    file.seek(-5, 2)  # Move 5 characters back from the end of the file
    print(file.read().decode('utf-8'))  # Read and print the last 5 characters

# Task 5: Use tell() Function To Get File Handle Position
with open('test.txt', 'r+') as file:
    print('File handle at:', file.tell())  # Print the initial position, should be 0 at the start
    file.readline()  # Read a line
    print('File handle at:', file.tell())  # Print the position after reading a line
