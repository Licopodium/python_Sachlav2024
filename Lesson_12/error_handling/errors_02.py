try:
    print(2 - "")
except NameError:
    print("There is a NameError")
except Exception as e:
    print(e)

print("------ After try-except ------")