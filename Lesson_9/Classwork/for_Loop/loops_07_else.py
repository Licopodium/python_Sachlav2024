list_of_statuses = [100, 200, 300, 400, 500, 600]

# for status in list_of_statuses:
#     print(status)
# else:
#     print("All iterations were finished!")


for status in list_of_statuses:
    if status == 400:
        print(status)
        break
    print(status)
else:
    print("All iterations were finished!")