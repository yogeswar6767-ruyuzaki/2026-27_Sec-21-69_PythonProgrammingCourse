# angles of a triangle 
A = float(input("Enter angle A ")) #  in degrees
B = float(input("Enter angle B ")) # in degrees
C = float(input("Enter angle C ")) # in degrees
if A > 0 and B > 0 and C > 0:
    if A + B + C == 180:
        print("The angles form a triangle")
    else:
        print("The angles do not form a triangle")
else:
    print("Invalid input. Angles must be positive.")