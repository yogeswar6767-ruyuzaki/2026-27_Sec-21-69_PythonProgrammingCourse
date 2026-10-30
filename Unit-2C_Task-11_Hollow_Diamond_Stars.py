# program to print a hollow diamond pattern of stars
# Upper half (including middle)

rows = int(input("Enter number of rows (half diamond): "))

for row_loop_var in range(1, rows + 1):
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):
        print(" ", end=" ")
    for column_loop_var_dots in range(1, 2 * row_loop_var):
        if column_loop_var_dots == 1 or column_loop_var_dots == 2 * row_loop_var - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Lower half

for row_loop_var in range(rows - 1, 0, -1):
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):
        print(" ", end=" ")
    for column_loop_var_dots in range(1, 2 * row_loop_var):
        if column_loop_var_dots == 1 or column_loop_var_dots == 2 * row_loop_var - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()    