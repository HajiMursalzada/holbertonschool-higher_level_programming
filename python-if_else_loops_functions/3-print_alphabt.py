#!/usr/bin/python3

for i in range(ord('a'), ord('z') + 1):
    if i == 113 or i == 101:
        continue
    print("{}".format(chr(i)), end="")
