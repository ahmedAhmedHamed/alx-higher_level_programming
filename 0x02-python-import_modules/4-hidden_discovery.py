#!/usr/bin/python3
import hidden_4
#this code works only on python 3.8
for item in dir(hidden_4):
    if not item.startswith("__"):
        print(f"{item}")

if __name__ == "__main__":
    pass
