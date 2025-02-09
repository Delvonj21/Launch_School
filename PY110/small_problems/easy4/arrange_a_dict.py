# Given a dictionary, return its keys sorted by the values associated with each key.


def sort_key(item):
    return item[1]


def order_by_value(dict):
    sorted_items = sorted(dict.items(), key=sort_key)
    return [key for key, value in sorted_items]


my_dict = {"p": 8, "q": 2, "r": 6}
keys = ["q", "r", "p"]
print(order_by_value(my_dict) == keys)  # True
