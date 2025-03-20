# Given these inputs
numbers = (2, 4, 6, 8, 10)
word = "hello"

# Challenge:
# Create a single line that makes a tuple containing:
# 1. The word where each letter is repeated twice ('h' -> 'hh')
# 2. The sum of the first three numbers in the tuple
# 3. The word in uppercase, but only first and last letters, including other in lower case

# Your solution should be ONE line:
result = (''.join(c * 2 for c in word), sum(numbers[:3]), word[0].upper() + word[1:-1].lower() + word[-1].upper())

# This will produce: ('hheelllloo', 12, 'HellO')
# Because:
# - Each letter in 'hello' is doubled
# - 2 + 4 + 6 = 12
# - First and last letters are in uppercase

# print(result)
print(word[0])
print(word[1])
final_string = ""
for c in word:
    print(c)
    final_string+=c*2

print(final_string)
print(''.join(c * 2 for c in word))
print(list(c * 2 for c in word))