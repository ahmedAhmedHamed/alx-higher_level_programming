#!/usr/bin/python3
def roman_to_int(roman_string):
    flag = 0
    number = 0

    for i in range(len(roman_string) - 1, -1, -1):
        if roman_string[i] == 'I':
            number += 1
            if flag == 1:
                number -= 2
        elif roman_string[i] == 'V':
            number += 5
            flag = 1
        elif roman_string[i] == 'X':
            number += 10
            flag = 1
        elif roman_string[i] == 'L':
            number += 50
            flag = 1
        elif roman_string[i] == 'C':
            number += 100
            flag = 1
        elif roman_string[i] == 'D':
            number += 500
            flag = 1
        elif roman_string[i] == 'M':
            number += 1000
            flag = 1
    return number
