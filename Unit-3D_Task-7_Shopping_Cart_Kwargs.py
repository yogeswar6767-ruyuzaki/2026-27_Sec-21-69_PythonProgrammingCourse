#  program that defines a function shopping_cart(**products) to print each item with its price in ₹, compute the total, and call it as shopping_cart(apple=15, orange=12, mango=10)
def shopping_cart(**products):
    total = 0
    for item, price in products.items():
        print(f"{item}: ₹{price}")
        total += price
    print(f"Total: ₹{total}")

shopping_cart(apple=15, orange=12, mango=10)