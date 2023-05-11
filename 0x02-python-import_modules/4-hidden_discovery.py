#!/usr/bin/python3
from hidden_4.py import *

for item in dir():
    if not item.startswith("__"):
        print(f"{item}")

if __name__ == "__main__":
    pass
