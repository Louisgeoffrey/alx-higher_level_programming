#!/usr/bin/python3
def complex_delete(my_dict, value):
    list_keys = list(my_dict.keys())

    for value_dict in list_keys:
        if value == my_dict.get(value_dict):
            del my_dict[value_dict]

    return (my_dict)
