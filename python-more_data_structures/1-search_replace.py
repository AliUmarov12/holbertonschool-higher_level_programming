#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list1 = my_list[:]
    b=my_list1.count(search)
    for i in range(b):
        my_list1[my_list.index(search)] = replace
    return my_list1
