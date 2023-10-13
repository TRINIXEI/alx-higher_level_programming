#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_key = list(a_dictionary.keys())

    for value_dict in list_key:
        if value == a_dictionary.get(value_dict):
            del a_dictionary[value_dict]

    return (a_dictionary)
