#  program to find the GCD of two numbers using recursion
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print(f"The GCD of {x} and {y} is: {gcd(x, y)}")