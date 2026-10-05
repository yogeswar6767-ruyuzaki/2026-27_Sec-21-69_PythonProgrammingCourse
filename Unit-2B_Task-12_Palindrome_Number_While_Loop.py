# program to check whether a number is an palindrome number or not using while loop 
number = int(input("Enter a number: ")) 
original_number = number 
work = number 
reverse = 0  
while work > 0: 
    digit = work % 10 
    reverse = reverse * 10 + digit 
    work //= 10 
if reverse == original_number: 
    print(f"{original_number} is a palindrome number.") 
else: 
    print(f"{original_number} is not a palindrome number.") 