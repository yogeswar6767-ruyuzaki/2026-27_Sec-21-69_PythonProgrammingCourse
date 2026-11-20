#  program that divides two numbers with try-except-else-finally and always prints Program finished     
try:
    a = int(input("Enter a number to divide 10 by: "))
    b = int(input("Enter another number to divide 10 by: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers.")
else:
    print("Result:", result)
finally:
    print("Program finished.")                