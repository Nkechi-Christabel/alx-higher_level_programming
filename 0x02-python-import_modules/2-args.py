#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

len = len(argv) - 1
argStr = "argument:" if len == 1 else "arguments:"

if len == 0:
    print("0 arguments.")
else:
    print("{:d} {:s}".format(len, argStr))
    for i in range(1, len + 1):
        print("{:d}: {:s}".format(i, argv[i]))
