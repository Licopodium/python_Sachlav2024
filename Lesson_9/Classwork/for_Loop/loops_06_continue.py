import string
# list_of_statuses = [100, 200, 300, 400, 500, 600]
#
# for status in list_of_statuses:
#     print("checking...")
#     if status == 400:
#         continue
#     print(status)
#     print("end of iteration")


# Original text
text = "Etiamtinciduntequeerat,quis.molestieenimimperdietvel!"

new_string = ""
print(f"{new_string = }")
for char in text:
    if char in string.punctuation:
        continue
    new_string+=char

print(f"{new_string = }")
