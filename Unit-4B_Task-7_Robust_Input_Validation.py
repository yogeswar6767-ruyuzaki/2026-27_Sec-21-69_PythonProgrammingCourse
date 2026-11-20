# program that validates student marks 0–100 with InvalidMarksError, prints Pass/Fail (≥40), and uses finally
class InvalidMarksError(Exception):
    pass    

try:
    marks = int(input("Enter student marks (0-100): "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")
    if marks >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")
except InvalidMarksError as err:
    print("Custom error:", err) 
except ValueError:
    print("Please enter a valid integer.")
finally:
    print("Program finished.")              