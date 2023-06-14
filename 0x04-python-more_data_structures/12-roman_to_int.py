#!/usr/bin/python3
def roman_to_int(roman_string):
    rNo = {'I': 1, 'V': 5, 'VI': 6, 'X': 10, 'L': 50,
           'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is not str or len(roman_string) == 0:
        return 0
    else:
        add = 0

        for x in range(len(roman_string)):
            if x == len(roman_string) - 1:
                num1 = +rNo[roman_string[x]]

            elif rNo[roman_string[x]] >= rNo[roman_string[x + 1]]:
                num1 = +rNo[roman_string[x]]

            else:
                num1 = -rNo[roman_string[x]]
            add = add + num1

        return add
