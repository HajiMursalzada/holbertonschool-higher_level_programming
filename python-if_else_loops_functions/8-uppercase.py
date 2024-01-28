#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            cpy = chr(ord(i) - 32)
        else:
            cpy = i
        print("{}".format(cpy), end="")
    print("")
