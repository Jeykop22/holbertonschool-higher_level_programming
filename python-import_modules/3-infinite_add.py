#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    args = argv[1:]
    numberOfArgs = len(args)
    if (numberOfArgs == 0):
        print("0")
    else:
        sum = 0
        for index in range(numberOfArgs):
            sum += int(args[index])
        print(f"{sum}")