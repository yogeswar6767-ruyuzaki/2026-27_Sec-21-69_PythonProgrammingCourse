# program to print a number right-angled triangle pattern
rows = int(input("Enter the number of rows : "))
for row_loop_var in range (1, rows +1):
    for col_loop_var in range (1, row_loop_var + 1):
        print(col_loop_var, end=" ")
    print()