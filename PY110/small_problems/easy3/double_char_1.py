# Write a function that takes a string, doubles every character in the string, then returns the result as a new string.


def repeater(string):
    doubled_string = ""

    for char in string:
        doubled_string += char * 2

    return doubled_string


print(repeater("Hello") == "HHeelllloo")  # True
print(repeater("Good job!") == "GGoooodd  jjoobb!!")  # True
print(repeater("") == "")
