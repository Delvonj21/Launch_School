# Write another function that returns True if the string passed as an argument is a palindrome, or False otherwise. This time, however, your function should be case-insensitive, and should ignore all non-alphanumeric characters. If you wish, you may simplify things by calling the is_palindrome function you wrote in the previous exercise.


def is_palindrome(string):
    reversed_string = string[::-1]

    if reversed_string == string:
        return True
    else:
        return False


def is_real_palindrome(string):
    filtered_string = ""
    for char in string:
        if char.isalnum():
            filtered_string += char.casefold()

    return is_palindrome(filtered_string)


print(is_real_palindrome("madam") == True)  # True
print(is_real_palindrome("356653") == True)  # True
print(is_real_palindrome("356635") == False)  # True
print(is_real_palindrome("356a653") == True)  # True
print(is_real_palindrome("123ab321") == False)  # True

# case doesn't matter
print(is_real_palindrome("Madam") == True)  # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True)  # True
