#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

a = int(argv[1])
op = argv[2]
b = int(argv[3])

ops = {'+': add, '-': sub, '*': mul, '/': div}

if op in ops:
    result = ops[op](a, b)
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, result))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
