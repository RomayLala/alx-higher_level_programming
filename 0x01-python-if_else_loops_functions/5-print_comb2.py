#!/usr/bin/python3
# Print numbers from 00 to 99, separated by ", "

for i in range(100):
    if i != 99:
        print(f"{i:02d}, ", end="")
    else:
        print(f"{i:02d}")
