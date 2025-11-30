#!/usr/bin/python3
"""
Function that returns the dictionary description of a class instance
with only simple data structures for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns a dictionary 
    """
    simple_types = (list, dict, str, int, bool)
    return {
        k: v
        for k, v in obj.__dict__.items()
        if isinstance(v, simple_types)
    }
