#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for index in range(0, x):
            count = count + 1
            print('{}'.format(my_list[index]), end='')
        print()
        return x
    except IndexError:
        print()
        return index
