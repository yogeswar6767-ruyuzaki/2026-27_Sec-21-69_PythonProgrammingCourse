#    program that raises InvalidSpeedError when vehicle speed is outside 0–120 km/h
class InvalidSpeedError(Exception):
    pass

try: 
    speed = int(input("Enter Speed (km/h)"))
    if speed < 0 or speed > 120:
            raise InvalidSpeedError("Speed must be between 0 - 120")
    print("Speed is accepted ")
except InvalidSpeedError as err:
     print("Custom error:", err)
except ValueError:
    print("Please enter a valid integer.")
