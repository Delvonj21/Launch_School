# Use Python's string methods on the string 'Captain Ruby' to create a string with the value 'Captain Python'.


first_8 = "Captain Ruby"[:8]
new_str = first_8 + "Python"
print(new_str)

all_words = "Captain Ruby".split(" ")
first_word = all_words[0]
new_str = first_word + " Python"
print(new_str)

my_string = "Captain Ruby".replace("Ruby", "Python")
print(my_string)
