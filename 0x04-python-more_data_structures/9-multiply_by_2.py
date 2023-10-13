#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dr = a_dictionary.copy()
    list_key = list(new_dr.keys())

    for i in list_key:
        new_dr[i] *= 2

    return (new_dr)
