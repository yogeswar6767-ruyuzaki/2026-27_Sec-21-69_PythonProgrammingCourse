#  program that defines a function divide(a, b) returning a / b; call it with keyword arguments divide(b=10, a=20) and with positional arguments divide(10, 20), and print both results
def divide (a, b):
    return a / b

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

result = divide(a, b)
print("Result with keyword arguments:", result)

result = divide(10, 20)
print("Result with positional arguments:", result)