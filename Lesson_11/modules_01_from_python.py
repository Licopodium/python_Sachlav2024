import datetime
from functools import reduce

print(datetime.date.today())

list_of_nums = [5, 10, 15 , 20, 25]

sum_of_nums = reduce(lambda x, y: x + y, list_of_nums)
print(sum_of_nums)