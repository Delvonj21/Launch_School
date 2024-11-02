# Write a function that takes an integer argument and returns a list containing all integers between 1 and the argument (inclusive), in ascending order.

# You may assume that the argument will always be a positive integer.


def sequence(number):
    new_list = []

    for element in range(1, number + 1):
        new_list.append(element)

    return new_list


print(sequence(5) == [1, 2, 3, 4, 5])  # True
print(sequence(3) == [1, 2, 3])  # True
print(sequence(1) == [1])  # True
