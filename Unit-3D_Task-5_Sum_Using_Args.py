# program that defines a function using *args to find the sum of any number of values
def sum_values(*args):
    total = 0 
    for value in args:
        total += value
    return total

print("Sum of 1, 2, 3:", sum_values(1, 2, 3))
print("Sum of 10, 20, 30, 40:", sum_values(10, 20, 30, 40))