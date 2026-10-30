# program to print a number pattern (e.g., Floyd's triangle)
rows = int(input("Enter the number of rows: "))
num = 1
for row_loop_var in range (1, rows + 1):
    for col_loop_var in range (1, row_loop_var + 1):
        print(num, end=" ")
        num += 1
    print()