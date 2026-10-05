# Print numbers from 1 to N using for loop 

N = int(input("Enter a number: "))
for loop_var in range(1, N + 1):

    print(loop_var) 


# print numbers from 1 to N using while loop 

N = int(input("Enter a number: "))
number = 1
while number <= N:
    print(f"{number}")
    number = number + 1