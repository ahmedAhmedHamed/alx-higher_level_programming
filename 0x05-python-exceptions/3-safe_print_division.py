#!/usr/bin/python3
def safe_print_division(a, b):
    division_value = 0
    try:
        if b == 0:
            raise ValueError("divide by zero")
        division_value = a / b
    except ValueError:
        pass
    finally:
        print("Inside result: {}".format(division_value))
    return division_value
