# PRACTICAL TASK 11

# Write a program that reads in a string and makes each alternate character into an upper case and each other alternate character a lower case character
# Then try to start with the same string but making each alternative word lower and upper case
# Using the functions split() and join() will help


# Get user input for a sentence
string_input = input("Please type a sentence: ")

# Empty string to store modified characters
string_characters = ""

# Iterate through each character in the input sentence
for character in range(len(string_input)):

    # If the index is even, convert the character to uppercase
    if character % 2 == 0:
        string_characters += string_input[character].upper()

    # If the index is odd, convert the character to lowercase
    else:
        string_characters += string_input[character].lower()

# Print the modified characters
print(string_characters)

# Initialize an empty list to store modified words
string_words = []

# Iterate through each word and its index in the input sentence
for index, word in enumerate(string_input.split()):

    # If the index is even, convert the word to uppercase
    if index % 2 == 0:
        string_words.append(word.upper())

    # If the index is odd, convert the word to lowercase
    else:
        string_words.append(word.lower())

# Print the modified words joined with spaces
print(" ".join(string_words))
