#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    c = argc - 1
    if c == 0:
        print("{} arguments.".format(c))
    else:
        if c == 1:
            print("1 argument:")
            print("{}: {}".format(c, sys.argv[c]))
        else:
            print("{} arguments:".format(c))
            for i in range(c):
                count = i + 1
                print("{}: {}".format(count, sys.argv[count]))
