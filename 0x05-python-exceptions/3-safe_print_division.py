#!/usr/bin/python3
def safe_print_division(a, b):
    division_value = None
    try:
        if b == 0:
            raise ValueError("divide by zero")
        division_value = a / b
    except ValueError:
        return None
    finally:
        print("Inside result: {}".format(division_value))
    return division_value
