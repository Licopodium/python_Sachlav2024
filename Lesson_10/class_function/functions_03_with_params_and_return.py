def get_formatted_greeting(value: str):
    return f"...Hello, {value.upper()}... :)"


def sum_of_two_numbers(num_1: int, num_2: int) -> int:
    if num_2 > num_1:
        return num_2 + num_1
    else:
        return num_2 + num_1

def print_formatted_result(result: int | float):
    print(f"{result = }")


print(get_formatted_greeting("Alex"))
formatted_strig = get_formatted_greeting("Iryna")
print(formatted_strig)
tuple_of_strings = (get_formatted_greeting("Viktor") , get_formatted_greeting("Roman"))
print(tuple_of_strings)

res = sum_of_two_numbers(2, 5)
print(res)
print_formatted_result(sum_of_two_numbers(10, 5))