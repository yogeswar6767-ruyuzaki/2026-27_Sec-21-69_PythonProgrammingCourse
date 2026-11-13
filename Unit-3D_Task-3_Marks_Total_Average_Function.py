# program that defines a function taking marks of three subjects as parameters and returns the total and average
def marks_total_average(marks1, marks2, marks3):
    total = marks1 + marks2 + marks3
    average = total / 3
    return total, average
marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))
total, average = marks_total_average(marks1, marks2, marks3)
print(f"The total marks are: {total}")
print(f"The average marks are: {average}")     