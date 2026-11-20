# program that reads a list index and handles ValueError and IndexError separately
list_data = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter an index to access the list: "))
    value = list_data[index]
    print("Value at index", index, "is:", value)
except ValueError:
    print("Error: Please enter a valid integer index.")
except IndexError:
    print("Error: Index out of range.")       