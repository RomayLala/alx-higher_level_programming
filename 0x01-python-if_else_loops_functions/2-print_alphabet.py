#!/usr/bin/python3
# Print the ASCII alphabet in lowercase without a newline at the end.

for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
