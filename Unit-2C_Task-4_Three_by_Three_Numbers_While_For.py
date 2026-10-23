# program to print numbers in a 3x3 grid using while-for nested loop
row_loop_var = 1
while row_loop_var <= 3:
    col_loop_var = 1
    while col_loop_var <= 3:
        print(col_loop_var + (row_loop_var - 1) * 3, end=' ')
        col_loop_var += 1
    print()
    row_loop_var += 1