#!/usr/bin/python3
""" this module is for an add integer function

    the function accepts two integers or two floats
    or any combination of the above

    floats will be converted to integers
"""


def add_integer(a, b=98):
    """ adds two integers and allows floats

    :arg a: the first number
    :arg b: the second number
    b has a default value, a does not
    they are both going to be casted to floats
    :returns
        int: an integer as the result of the addition

    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
