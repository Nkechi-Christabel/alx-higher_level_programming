#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

len = len(argv)
sum = 0

if len < 2:
    print("0")
else:
    for i in range(1, len):
        sum += int(argv[i])

print("{:d}".format(sum))
