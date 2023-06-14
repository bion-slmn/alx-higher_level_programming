#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        nlist = a_dictionary.items()
        sorted_list = sorted(nlist, key=lambda x: x[1], reverse=True)

        return sorted_list[0][0]
