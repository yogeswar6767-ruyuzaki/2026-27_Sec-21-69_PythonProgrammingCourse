# n program that defines a function print_details(**kwargs) to print each key and value from kwargs; call it as print_details(name="Krishna", age=26, city="Guntur")
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="krishna", age=26, city="Guntur")        