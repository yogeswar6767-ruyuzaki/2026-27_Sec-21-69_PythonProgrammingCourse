# program that defines a function to calculate the area and perimeter of a rectangle (length and breadth as parameters) and returns both values
def rectangle_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area, perimeter = rectangle_area_perimeter(length, breadth)
print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")