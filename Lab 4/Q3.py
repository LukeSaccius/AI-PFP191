import os

path = "./Lab04/a/"
filename = f"{path}test.txt"

def seek_beginning(fname):
    with open(fname, 'r') as file:
        file.seek(0, os.SEEK_SET)
        print(file.read())

def seek_end(fname):
    with open(fname, 'a') as file:
        file.seek(0, os.SEEK_END)
        file.write("\nThis content is added to the end of the file")
        print(f"file handel at: {file.tell()}")
    
def seek_current(fname, offset):
    with open(fname, 'r') as file:
        current = file.tell()
        new = current + offset
        file.seek(new, os.SEEK_SET)
        print(file.read())

# def seek_end_negative(fname, offset):    DOESN'T WORK WITH PYTHON 3
#     with open(fname, 'r') as file:
#         file.seek(offset, os.SEEK_SET)
#         print(file.read())

seek_beginning(filename)
print("*************")
seek_end(filename)
print("*************")
seek_current(filename, 3)
print("*************")
# seek_end_negative(filename, 3)
# print("*************")

