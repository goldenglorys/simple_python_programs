"""
    This helps do some work based on the arguments passed irrespective of it's length
"""

def add_number(*args):
    total = 0
    for data in args:
        total += data
    print(total)


add_number(3)
add_number(33, 5656, 3343)