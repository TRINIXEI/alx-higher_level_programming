#!/usr/bin/python3
def to_subtract(list_numm):
    to_subb = 0
    max_listt = max(list_numm)

    for nn in list_numm:
        if max_listt > nn:
            to_subb += nn

    return (max_listt - to_subb)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_nn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keyss = list(rom_nn.keys())

    numm = 0
    last_romm = 0
    list_numm = [0]

    for chh in roman_string:
        for r_numm in list_keyss:
            if r_numm == chh:
                if rom_nn.get(chh) <= last_romm:
                    numm += to_subtract(list_numm)
                    list_numm = [rom_nn.get(chh)]
                else:
                    list_numm.append(rom_nn.get(chh))

                last_romm = rom_nn.get(chh)

    numm += to_subtract(list_numm)

    return (numm)
