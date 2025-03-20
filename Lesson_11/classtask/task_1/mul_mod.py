from add_mod import *

def mul(num1: int, num2: int):
    total = 0
    for _ in range(num2):
        total = add(total, num1)
    return total
