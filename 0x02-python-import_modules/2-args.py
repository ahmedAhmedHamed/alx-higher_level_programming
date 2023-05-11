#!/usr/bin/python3
from sys import argv

if len(argv) == 0:
    print("0 arguments.")
elif len(argv) == 1:
    print("1 argument:")
else:
    print(f"{len(argv)} arguments:")

for idx, argument in enumerate(argv, 1):
    print(f"{idx}: {argument}")
