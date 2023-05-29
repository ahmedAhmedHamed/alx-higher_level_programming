#!/usr/bin/python3
def safe_print_division(a, b):
    division_value = 0
    try:
        if b == 0:
            raise Exception("divide by zero")
        division_value = a / b
    except:
        return None
    finally:
        print("Inside result: {}".format(division_value))
    return division_value