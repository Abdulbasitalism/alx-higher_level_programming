#!/usr/bin/python3
# A program that prints the number of and the list of its arguments.
if __name__ == "__main__":
    from sys import argv
    x = len(argv) - 1
    if x < 1:
        print("{} arguments.".format(x))
    elif x == 1:
        print("{} argument:".format(x))
    else:
        print("{} arguments:".format(x))

    for i in range(x):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
