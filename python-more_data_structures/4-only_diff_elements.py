#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = []
    for i in set_1:
        for k in set_2:
            if i == k:
                a += [k]
    for i in list(set_1) + list(set_2):
        for k in a:
            if not i == k:
                c += [i]
    return set(c)
