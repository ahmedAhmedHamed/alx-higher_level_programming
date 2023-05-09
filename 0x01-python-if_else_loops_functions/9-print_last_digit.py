#!/usr/bin/python3
def print_last_digit(number):
    init_last_digit = number % 10
    if number < 0:
        final_last_digit = -init_last_digit + 10
    else:
        final_last_digit = init_last_digit
    print(f"{final_last_digit}")
    return (final_last_digit)
