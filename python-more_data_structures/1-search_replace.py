#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list1 = my_list[:]
    for i in range(my_list1.count(search)):
        my_list1 = my_list1.replace(search, replace)
    return my_list1
