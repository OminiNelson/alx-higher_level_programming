#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    if not my_list:
        return (None)
    for item in my_list:
        bool_list.append(True) if (item % 2 == 0) else bool_list.append(False)
    return bool_list
