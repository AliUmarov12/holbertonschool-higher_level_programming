#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list = my_list.sort()
    my_list = my_list[len(my_list) - 1: 0 : -1]
    for i in my_list:
        print("{:d}".format(i))
