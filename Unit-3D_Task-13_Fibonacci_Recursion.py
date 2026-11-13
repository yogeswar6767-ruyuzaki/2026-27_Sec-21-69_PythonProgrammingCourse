# program to generate Fibonacci series using recursion

def fib(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    return fib(k - 1) + fib(k - 2)

n = int(input("Enter the number of terms for Fibonacci series: "))
for i in range(n):
    print(fib(i), end=" ")