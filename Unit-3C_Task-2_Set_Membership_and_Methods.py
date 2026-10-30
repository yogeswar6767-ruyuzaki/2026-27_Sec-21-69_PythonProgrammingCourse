# program to demonstrate set membership testing and methods (add, remove, discard)

set_data = {106, 67, 69}
print("Set:", set_data)

print("20 in set?", 20 in set_data)
print("40 not in set?", 40 not in set_data)

set_data.add(40)
print("After add:", set_data)

set_data.remove(106)
print("After remove:", set_data)

set_data.discard(99)
print("After discard:", set_data)