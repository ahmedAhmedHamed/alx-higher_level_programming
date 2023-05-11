#!/usr/bin/python3
from sys import argv

count = 0

for idx, arg in enumerate(argv):
    if idx == 0:
        continue
    count += int(arg)

print(f"{count}")

if __name__ == '__main__':
    pass
