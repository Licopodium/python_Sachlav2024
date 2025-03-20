text = input("Enter a first word: ")
text_2 = input("Enter a second word: ")

if text == text_2[::-1]:
    print('YES')
else:
    print('NO')