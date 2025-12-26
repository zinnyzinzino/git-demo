from typing import Dict

def combine_dicts(*args):
    result = {}
    for d in args:
        for key, value in d.items():
            result[key] = result.get(key, 0) + value
    return result
