#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if not my_list:
        return (None)
    max_int = my_list[0]
    for item in my_list:
        if max_int < item:
            max_int = item
    return max_int
