#!/usr/bin/python3
from sys import argv

if len(argv) - 1 == 0:
    print("0 arguments.")
    exit(0)
elif len(argv) - 1 == 1:
    print("1 argument:")
else:
    print(f"{len(argv) - 1} arguments:")

for idx, argument in enumerate(argv):
    if idx == 0:
        continue
    print(f"{idx}: {argument}")


if __name__ == '__main__':
    pass
