 # calculate compound interest
p = float(input("Enter the principal amount: ")) # in rupees
r = float(input("Enter the rate of interest: ")) # in percentage
t = float(input("Enter the time period: ")) # in years
A = p * (1 + r/100) ** t
CI = A - p
print("The compound interest is: ", CI)