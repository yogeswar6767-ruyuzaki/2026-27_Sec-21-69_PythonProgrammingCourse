# program that raises ValueError if the entered age is negative
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Your age is:", age)
except ValueError as ve:
    print("Error:", ve)