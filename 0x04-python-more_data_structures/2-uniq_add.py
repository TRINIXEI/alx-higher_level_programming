#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_set = set(my_list)
    numb = 0

    for i in uniq_set:
        numb += i

    return (numb)
