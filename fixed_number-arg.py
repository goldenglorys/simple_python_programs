"""
    This helps do some work based on the arguments passed irrespective of it's length
"""


def add_number(*args):
    total = 0
    for data in args:
        total += data
    print(total)


# add_number(3)
# add_number(33, 5656, 3343)


def diction():
    dict_items = {
        'movie1': 'Snowden',
        'movie2': 'Ocean',
        'movie3': 'Heist'
    }
    for k, v in dict_items.items():
        print(k, v)


# diction()


def set_in_python():
    """
        This return the values in the set and remove duplicate entries
    """
    set_example = {
        'Snowden',
        'Kim Dot Com',
        'Julian Assange',
        'Manning',
        'Gregg Braden',
        'Bruce Lipton',
        'Stephen Greer',
        'Snowden'
    }

    for data in set_example:
        print(data)


set_in_python()