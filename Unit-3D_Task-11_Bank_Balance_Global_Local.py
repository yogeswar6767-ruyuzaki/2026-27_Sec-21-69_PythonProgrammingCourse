# program for a simple bank balance: a global balance, a function to deposit (uses global), and a function that uses a local balance to show it does not update the account
balance = 1000  # global variable
def deposit(amount):
    global balance
    balance = balance + amount
    print(f"Deposited: {amount}, New Balance: {balance}")

def show_local_balance():
    balance = 500  # local variable
    print(f"Local Balance: {balance}")

print("start:" , balance)   
deposit(200)  # deposit 200
print("account balance:" , balance)
show_local_balance()  # show local balance
print("account balance after still:" , balance)  # global balance remains unchanged