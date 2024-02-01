#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_value = max(a_dictionary.values(), default=None)
    for i, v in a_dictionary.items():
        if v == max_value:
            return i
