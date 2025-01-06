import string
text = "abcde, abcde, abcde"
# print(text.split(sep=","))
list_of_strings = text.split()
print(list_of_strings)
print(type(list_of_strings))
print(string.punctuation)