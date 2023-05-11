#!/usr/bin/python3
from calculator_1 import add, div, mul, sub
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
    print(f"{num1} {argv[2]} {num2} = {add(num1, num2)}")
elif argv[2] == operators[1]:
    print(f"{num1} {argv[2]} {num2} = {sub(num1, num2)}")
elif argv[2] == operators[2]:
    print(f"{num1} {argv[2]} {num2} = {div(num1, num2)}")
elif argv[2] == operators[3]:
    print(f"{num1} {argv[2]} {num2} = {mul(num1, num2)}")

if __name__ == '__main__':
    pass
