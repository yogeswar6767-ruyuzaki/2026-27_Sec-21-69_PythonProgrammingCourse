# program that shows a local variable inside a function does not change a global variable with the same name
x = 10  # global variable
def my_function():
    x = 5  # local variable
    print("Inside the function, x =", x)

my_function()
print("Outside the function, x =", x)