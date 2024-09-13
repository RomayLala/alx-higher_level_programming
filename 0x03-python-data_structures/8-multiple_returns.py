#!/usr/bin/python3
# Function that returns a tuple with the length of a string and its first character.

def multiple_returns(sentence):
    if sentence == "":
        return (0, None)  # Return length 0 and None for an empty string
    return (len(sentence), sentence[0])  # Return length and first character
