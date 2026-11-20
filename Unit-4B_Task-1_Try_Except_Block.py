#  program that catches ZeroDivisionError when dividing 10 by 0
try:
    a = int(input("Enter a number to divide 10 by: "))
    b = int(input("Enter another number to divide 10 by: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
