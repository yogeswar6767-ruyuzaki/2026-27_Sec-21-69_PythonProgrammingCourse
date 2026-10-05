# program to print the multiplication table of a number using for loop 

N = int(input("Enter a number: "))

for i in range(1, 11):

    print(f"{N} x {i} = {N * i}")

# program to print the multiplication table of a number using while loop 3
 
N = int(input("Enter a number: "))

i = 1

while i <= 10:

    print(f"{N} x {i} = {N * i}")

    i += 1