#!/usr/bin/python3
"""
Function 
"""


def class_to_json(obj):
    """
    ksdnfkjnfjnrjnfr
    """
    # __dict__ bütün instance atributlarını verir
    simple_types = (list, dict, str, int, bool)
    return {k: v for k, v in obj.__dict__.items() if isinstance(v, simple_types)}
