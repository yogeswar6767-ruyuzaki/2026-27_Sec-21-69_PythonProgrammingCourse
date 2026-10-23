# program to print a 5x5 grid of stars (*); generalize the program so the grid size is based on user input
grid_size = 5

for row in range(grid_size):
    for col in range(grid_size):
        print("*", end=" ")
    print()