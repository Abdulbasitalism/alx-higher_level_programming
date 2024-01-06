#!/usr/bin/python3
# A program that prints the result of the addition of all arguments
if __name__ == "__main__":
    from sys import argv
    sumint = 0
    for i in range(1, len(argv)):
        sumint += int(argv[i])
        print("{}".format(sumint))
