#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elem_printed = 0
    for i in range(0, x):
        try:
            print(my_list=[], end = "")
            elem_printed =+ 1
        except BaseException:
            break
    print()
    return elem_printed
