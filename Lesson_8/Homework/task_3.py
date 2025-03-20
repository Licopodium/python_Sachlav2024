
# Original text
text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

# Split the text into words while preserving punctuation
words = text.split()
processed_words = []

# Process each word
for word in words:
    # Check if the word ends with punctuation
    if word[-1] in [',', '.']:
        # Separate punctuation from word
        pure_word = word[:-1]
        punctuation = word[-1]
        # Add 'ing' and restore punctuation
        processed_word = pure_word + 'ing' + punctuation
    else:
        # Just add 'ing' if no punctuation
        processed_word = word + 'ing'

    processed_words.append(processed_word)

# Join the words back together
result = ' '.join(processed_words)

# Print results
print("Original text:")
print(text)
print("\nProcessed text:")
print(result)