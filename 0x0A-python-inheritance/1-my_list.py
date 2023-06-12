#!/usr/bin/python3
"""my list - a simple class that inherits from list"""


class MyList(list):
    """my list class is a list
        all of this class's inputs have to be integers
    """
    def print_sorted(self):
        """prints the list in a sorted fashion
            (ascending)
        """
        x = self.copy()
        x.sort()
        for i in x:
            print(i)
        pass
