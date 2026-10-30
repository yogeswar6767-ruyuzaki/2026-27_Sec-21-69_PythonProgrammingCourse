#  program to remove duplicate elements from a list

from numpy import unique


list_data = [1, 2, 2, 3, 1, 4, 3,6, 5, 4, 5]
unique = unique(list_data)

print("Original:", list_data)
print("Without duplicates:", unique)