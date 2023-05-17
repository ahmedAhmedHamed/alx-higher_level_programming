#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    i = len(roman_string) - 1
    while i >= 0:
        if roman_string[i] == 'I':
            number += 1
        elif roman_string[i] == 'V':
            number += 5
            if i - 1 >= 0 and roman_string[i - 1] == 'I':
                number -= 1
        elif roman_string[i] == 'X':
            number += 10
            if i - 1 >= 0 and roman_string[i - 1] == 'V':
                number -= 5
        elif roman_string[i] == 'L':
            number += 50
            if i - 1 >= 0 and roman_string[i - 1] == 'X':
                number -= 10
        elif roman_string[i] == 'C':
            number += 100
            if i - 1 >= 0 and roman_string[i - 1] == 'L':
                number -= 50
        elif roman_string[i] == 'D':
            number += 500
            if i - 1 >= 0 and roman_string[i - 1] == 'C':
                number -= 100
        elif roman_string[i] == 'M':
            number += 1000
            if i - 1 >= 0 and roman_string[i - 1] == 'D':
                number -= 500
        i -= 1
    return number
