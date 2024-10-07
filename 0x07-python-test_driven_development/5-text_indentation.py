#!/usr/bin/python3
"""
Module for text_indentation function.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?', and ':'.
    
    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove leading and trailing whitespace from each split sentence.
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ['.', '?', ':']:
            result += "\n\n"
            i += 1
            # Skip any spaces right after '.', '?', or ':'
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    # Print the formatted result, trimming unnecessary spaces
    print(result.strip(), end="")
