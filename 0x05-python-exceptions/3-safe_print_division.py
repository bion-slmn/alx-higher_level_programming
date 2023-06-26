#!/usr/bin/python3
def safe_print_division(a, b):
    '''divides 2 integers and prints the result.'''
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("{}".format(result))
        return result
