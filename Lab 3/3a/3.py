def middle_chars(s):
    return s[(len(s) - 4)//2:(len(s) + 4)//2]

def insert_middle(s1, s2):
    return s1[:len(s1)//2] + s2 + s1[len(s1)//2:]

def combine_chars(s1, s2):
    return s1[0] + s2[0] + s1[len(s1)//2] + s2[len(s2)//2] + s1[-1] + s2[-1]

def sort_chars(s):
    return ''.join(sorted(s, key=lambda c: c.isupper()))

def count_types(s):
    letters, digits, symbols = 0, 0, 0
    for char in s:
        if char.isalpha(): letters += 1
        elif char.isdigit(): digits += 1
        else: symbols += 1
    return letters, digits, symbols

# Variables for each task
str1, str2 = "BillDescrtran", "HoSongHu"
str3, str4 = "Ault", "Kelly"
str5, str6 = "America", "Japan"
str7 = "PyNaTive"
str8 = "P@yn2at&t%%fds$fda^^&%^$ive"

# Outputs for each task
print(f"Task 1: {middle_chars(str1)}, {middle_chars(str2)}")
print(f"Task 2: {insert_middle(str3, str4)}")
print(f"Task 3: {combine_chars(str5, str6)}")
print(f"Task 4: {sort_chars(str7)}")
print(f"Task 5: Chars = {count_types(str8)[0]}, Digits = {count_types(str8)[1]}, Symbols = {count_types(str8)[2]}")
