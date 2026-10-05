# program to find the sum of digits of a number using while loop 
num = int(input("Enter a number: "))
original_N = num
work = num
total = 0
while work > 0:
    digit = work % 10
    total =total + digit
    work //= 10
print(f"The sum of digits of {original_N} is: {total}")