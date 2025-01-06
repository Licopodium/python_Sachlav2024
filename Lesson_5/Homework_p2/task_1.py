message = input("Enter a string with several words: ")

print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Title Case:", message.title())
print("Capitalized:",  message.capitalize())
print("List of words:", message.split())

print("Alphabetically first word:", sorted(message.split())[0])
print("Alphabetically last word:", sorted(message.split())[-1])
