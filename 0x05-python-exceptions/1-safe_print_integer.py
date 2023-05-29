#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except IndexError:
        return False
    except TypeError:
        return False
    except:
        return False
    finally:
        return True
