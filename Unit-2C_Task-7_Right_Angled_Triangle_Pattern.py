# program to print a right-angled triangle pattern; read the number of rows and the symbol to print (e.g. * or 0) from the user
rows = int(input("Enter the number of rows: "))
symbol = input("Enter the symbol to print: ")

for i in range(1, rows + 1):
    print(symbol * i) 