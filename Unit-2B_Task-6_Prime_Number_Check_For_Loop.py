    #program to check whether a given number is prime or not using for loop (assume the input number is between 1 and 100)
number = int(input("Enter a number: "))
is_prime = True
for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
if is_prime and number > 1:
        print(f"{number} is a prime number.") 
else:
        print(f"{number} is not a prime number.")        