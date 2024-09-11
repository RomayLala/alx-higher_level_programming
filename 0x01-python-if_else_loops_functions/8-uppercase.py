#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:  # Check if the character is lowercase
            char = chr(ord(char) - 32)  # Convert to uppercase by subtracting 32 from ASCII value
        print("{}".format(char), end="")  # Print the character without newline
    print()  # Print a newline at the end
