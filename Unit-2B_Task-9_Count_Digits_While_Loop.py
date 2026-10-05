# program to count the number of digits in a number using while loop 
num = int(input("Enter a number: "))
digit_count = 0
if num == 0:
    digit_count = 1
else:
    while num > 0:
        digit_count = digit_count + 1
        num = num // 10
print(f"The number of digits in the number is: {digit_count}")        