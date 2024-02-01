def word_filter_counter(text, filter_words):
    words = text.split()
    filter_words_lower = [word.lower() for word in filter_words]

    # Initialize an empty dictionary to store word counts
    word_counts = {}

    # Iterate through each word in the input text
    for every_word in words:
        lowercase_word = every_word.lower()  # Fix: Correct variable name
        if lowercase_word in filter_words_lower:
            if lowercase_word in word_counts:
                word_counts[lowercase_word] += 1
            else:
                word_counts[lowercase_word] = 1

    return word_counts

# Get input from the user
user_text = input("Enter the text: ")
user_filter_words = input("Enter filter words separated by space: ").split()

# Call the function and print the result
result = word_filter_counter(user_text, user_filter_words)
print(result)