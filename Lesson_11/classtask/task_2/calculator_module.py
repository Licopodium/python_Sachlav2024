def __add(x, y):
    return x + y


def __subtract(x, y):
    return x - y


def __multiply(x, y):
    return x * y


def __divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def calculate(x, y, operation):
    match operation:
        case '+':
            return __add(x, y)
        case '-':
            return __subtract(x, y)
        case '*':
            return __multiply(x, y)
        case '/':
            return __divide(x, y)
        case _:
            raise ValueError("Invalid operation")