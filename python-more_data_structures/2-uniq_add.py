#!/usr/bin/python3
def uniq_add(my_list=[]):
    copy = set(my_list)
    result = 0
    for i in copy:
        result += i
    return result
