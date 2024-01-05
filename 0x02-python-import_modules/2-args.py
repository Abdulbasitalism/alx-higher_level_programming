#!/usr/bin/python3
# A program that prints the number of and the list of its arguments.
if __name__ == "__main__":
    import sys

    count = len(sys.arg) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 arguments:")
    elif:
        print("{} arguments:".format(count))
        for i in range(count):
            print("{}: {}".format(i + 1, sys.argv(i + 1)))
