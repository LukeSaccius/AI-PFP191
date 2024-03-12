# Given lists
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# Concatenating the lists index-wise
concatenated_list = [i + j for i, j in zip(list1, list2)]
print(concatenated_list)