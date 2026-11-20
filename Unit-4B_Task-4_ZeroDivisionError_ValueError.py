# program that reads numerator and denominator and handles ZeroDivisionError and ValueError
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator    
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers.")    
finally:
    print("Program finished.")    