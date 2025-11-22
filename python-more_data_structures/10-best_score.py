#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    else:
        a = []
        for i in sorted(a_dictionary):
            a += [a_dictionary[i]]
        return max(a)
