#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary or not isinstance(a_dictionary, dict):
        return None

    best_key = None
    max_score = float('-inf')

    for key, score in a_dictionary.items():
        if score > max_score:
            max_score = score
            best_key = key

    return best_key
