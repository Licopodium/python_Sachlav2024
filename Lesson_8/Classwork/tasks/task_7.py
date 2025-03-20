text = input("Enter your sentence: ")

type_of_sentence = "Question" if text[-1] == "?" else "Regular"

print(type_of_sentence)