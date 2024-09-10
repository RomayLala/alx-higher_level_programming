#!/usr/bin/python3
# Script to print the ASCII alphabet in lowercase except 'q' and 'e', without a new line.

for letter in range(97, 123):  # ASCII values for 'a' to 'z'
    if letter != 113 and letter != 101:  # ASCII for 'q' is 113, 'e' is 101
        print("{:c}".format(letter), end="")
