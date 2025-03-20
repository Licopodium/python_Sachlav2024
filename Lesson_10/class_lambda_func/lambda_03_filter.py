my_list = [1, 2, 10, 30, -3, 5, -10, 0]

def is_positive(num: int | float):
    return num > 0

filter_res = filter(is_positive, my_list)
print(filter_res)
filter_res = list(filter_res)
print(filter_res)

filtered_data = tuple(filter(lambda x: x > 0, my_list))
print(filtered_data)
# print(is_positive(1))
# print(is_positive(-5))