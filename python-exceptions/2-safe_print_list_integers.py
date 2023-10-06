#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number_printed = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            number_printed += 1
        except IndexError:
            raise
        except Exception:
            pass
    print("")
    return number_printed
