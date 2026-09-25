#  python program to check whether a number is positive, negative, or zero
Number = float(input("Enter a number: "))
if Number > 0:
    print(f"{Number} is a positive number ")
elif Number < 0:
    print(f"{Number} is a negative number ")
else:
    print(f"{Number} is zero ")  