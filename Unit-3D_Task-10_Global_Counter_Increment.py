#  program that uses a global counter and increments it inside a function using the global keyword
counter = 0  # global variable
def increment_counter():
    global counter  # declare counter as global to modify it
    counter += 1
    print("Counter inside the function:", counter)  
print("Counter before calling the function:", counter)
increment_counter() 
print("Counter after calling the function:", counter)   
    