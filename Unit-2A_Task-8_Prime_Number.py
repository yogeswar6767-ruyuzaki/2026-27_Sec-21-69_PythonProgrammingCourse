number = int(input("Enter a number: "))

if number < 2:
    print("Not prime")
else:
    for divisor in range(2, number):
        if number % divisor == 0:
            print(f"{number} is not a prime number")
    else:
        print(f"{number} is a prime number")