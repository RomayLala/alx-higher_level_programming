#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # Counter for number of elements printed
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass  # If an index error occurs, we stop printing
    print("")  # Move to a new line after printing
    return count  # Return the number of elements printed
