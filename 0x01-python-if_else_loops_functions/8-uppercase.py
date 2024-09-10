#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        # Check if character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert to uppercase by adjusting ASCII value
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)

