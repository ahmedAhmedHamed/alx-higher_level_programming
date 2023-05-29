#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_result = [None] * list_length
    for i in range(list_length):
        try:
            my_result[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            my_result[i] = 0
            print("division by 0")
        except TypeError:
            my_result[i] = 0
            print("wrong type")
        except IndexError:
            my_result[i] = 0
            print("out of range")
        finally:
            pass
    return my_result
