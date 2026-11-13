# program that defines a function to calculate simple interest with parameters principal, time, and rate (default rate = 5); call it using the default rate and also with an explicit rate
def simple_interest(principal, time, rate=5):
    interest = (principal * time * rate) / 100
    return interest

print("SI (default rate):", simple_interest(1000, 2))
print("SI (rate=8):", simple_interest(1000, 2, 8))