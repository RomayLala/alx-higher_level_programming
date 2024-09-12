#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Start the sum from 0
    total_sum = 0
    
    # Loop through the arguments (ignoring the first one which is the script name)
    for arg in sys.argv[1:]:
        total_sum += int(arg)
    
    # Print the result followed by a new line
    print(total_sum)
