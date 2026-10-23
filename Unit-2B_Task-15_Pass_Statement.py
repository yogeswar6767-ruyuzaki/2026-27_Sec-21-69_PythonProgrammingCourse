# Example solution: pass statement using a for loop
n = int(input("Enter N (use pass for multiples of 3): "))

for number in range(1, n + 1):
    if number % 3 == 0:
        pass
        print(f"Used pass for multiple of 3: {number} (N is {n})")
    else:
        print(f"for loop number = {number} (up to {n})")

# Example solution: pass statement using a while loop
n = int(input("Enter N (use pass for multiples of 3): "))
i = 1
while i <= n:
    if i % 3 == 0:
        pass
        print(f"Used pass for multiple of 3: {i} (N is {n})")
    else:
        print(f"while loop number = {i} (up to {n})")
    i += 1
    