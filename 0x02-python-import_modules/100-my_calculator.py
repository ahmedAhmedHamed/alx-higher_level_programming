#!/usr/bin/python3
import calculator_1 as calc
from sys import argv

if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

operators = ["+", "-", "/", "*"]

if argv[2] not in operators:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

num1 = int(argv[1])
num2 = int(argv[3])

if argv[2] == operators[0]:
    print(f"{num1} {argv[2]} {num2} = {calc.add(num1, num2)}")
elif argv[2] == operators[1]:
    print(f"{num1} {argv[2]} {num2} = {calc.sub(num1, num2)}")
elif argv[2] == operators[2]:
    print(f"{num1} {argv[2]} {num2} = {calc.div(num1, num2)}")
elif argv[2] == operators[3]:
    print(f"{num1} {argv[2]} {num2} = {calc.mul(num1, num2)}")

if __name__ == '__main__':
    pass
