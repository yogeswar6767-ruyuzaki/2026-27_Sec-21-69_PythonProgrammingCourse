# program to print numbers in a 3x3 grid using for-for nested loop
for row_loop_var in range(1, 4):
    for col_loop_var in range(1, 4):
        print(col_loop_var + (row_loop_var - 1) * 3, end=' ')
    print()