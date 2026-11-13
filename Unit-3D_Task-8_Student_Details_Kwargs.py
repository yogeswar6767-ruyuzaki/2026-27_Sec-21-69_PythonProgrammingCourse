#  program that defines a function using **kwargs to display a student's name and subject marks
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
student_details(name="Alice", math=95, science=90, english=88)