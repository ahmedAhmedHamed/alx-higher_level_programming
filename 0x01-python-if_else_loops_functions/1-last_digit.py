#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
init_last_digit = number % 10
if number < 0:
    final_last_digit = -init_last_digit + 10
else:
    final_last_digit = init_last_digit

print(f"Last digit of {number} is", end=" ")
if number < 0:
    print("-", end="")
print(f"{final_last_digit} ", end="")
if final_last_digit > 5 and number > 0:
    print("and is greater than 5")
elif number == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
