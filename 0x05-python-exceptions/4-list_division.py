#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    '''divides element by element 2 lists.'''
    newList = []
    for item in range(list_length):
        try:
            result = my_list_1[item] / my_list_2[item]
            newList.append(result)
        except ZeroDivisionError:
            result = 0
            newList.append(result)
            print("{}".format("division by 0"))
        except (TypeError, ValueError):
            print("{}".format("wrong type"))
            result = 0
            newList.append(result)
        except IndexError:
            print("{}".format("out of range"))
            result = 0
            newList.append(result)
        except Exception:
            pass
            result = 0
            newList.append(result)
    return newList
