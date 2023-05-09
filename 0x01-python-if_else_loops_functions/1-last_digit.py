#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberString = repr(number)
print(f"Last digit of {number} is {numberString[-1]}", end=" ")
if int(numberString[-1]) > 5:
	print("and is greater than 5")
elif int(numberString[-1]) == 0:
	print("and is 0")
else:
	print("and is less than 6 and not 0")
