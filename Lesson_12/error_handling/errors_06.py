class CustomException(Exception):
    """
    Our created custom exception
    """
    pass

x = 2
y = 3

try:
    if x != y:
        raise CustomException(f"{x} and {y} are not equal")
    print("Numbers are equal")
except CustomException as ce:
    print("error", ce)
