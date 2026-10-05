# program to write fibonacci series up to N terms using for loop
N = int(input("Enter a number: "))
a, b = 0, 1
for i in range(N):
    print(a)
    nxt = a + b 
    a = b 
    b = nxt 