#!/usr/bin/python3
def weight_average(my_listt=[]):
    if not my_listt:
        return 0

    numm = 0
    denn = 0

    for tupp in my_listt:
        numm += tupp[0] * tupp[1]
        denn += tupp[1]

    return (numm / denn)
