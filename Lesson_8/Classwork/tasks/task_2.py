salary = int(input("Enter your salary: "))

# option 1
# if salary >= 20000:
#     print(f"{salary * 0.87}")
# else:
#     print(salary)

# option 2
# print(f"{salary * 0.87}") if salary >= 20000 else print(salary)

# option 3
if salary >= 20000:
    salary *= 0.87

print(salary)
