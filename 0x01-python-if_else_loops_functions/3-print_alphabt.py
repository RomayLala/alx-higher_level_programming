#!/usr/bin/python3
# This script prints the ASCII alphabet in lowercase except 'q' and 'e'

print("".join(["{:c}".format(i) for i in range(97, 123) if i != 101 and i != 113]), end="")
