# program to find the last digit of a number 


num = int(input("Enter a number: "))

last_digit = num % 10

print(f"The last digit of {num} is {last_digit}")

# program to find the remaining digits of a number 


num = int(input("Enter a number: "))

remaining_digits = num // 10

print(f"The remaining digits of {num} are {remaining_digits}")
