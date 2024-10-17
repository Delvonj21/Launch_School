# What would the following code output? Try to answer without running the code.

words = ["ant", "bear", "cat"]
selected_words = []
for word in words:
    if len(word) > 3:
        selected_words.append(word)

print(selected_words)

# ['bear'], This code will only append words to `selected_words` that have a length greater than 3 characters
