def get_text_length(text="Hello"):
    return len(text)
print(get_text_length())

def get_text_length_in_list(strings):
    total_length = 0
    for string in strings:
        total_length += get_text_length(string)
    return total_length
print(get_text_length_in_list(["Hello", "World", "Python"]))


""" def get_text_length(text="Hello"):
    return len(text)


def get_text_length_in_list(any_list: list[str]):
    total = 0
    for item in any_list:
        total += get_text_length(item)
    return total


print(get_text_length_in_list(['Alex', 'Ron', 'Gal'])) """