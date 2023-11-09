#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dir = my_dict.copy()
    list_keys = list(new_dir.keys())

    for i in list_keys:
        new_dir[i] *=2

    return (new_dir)
