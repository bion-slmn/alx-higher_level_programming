#!/usr/bin/python3
'''prints a text with 2 new lines after each of these
    characters: ., ? and :'''


def text_indentation(text):
    '''adds 2 new lines after each of these
    characters: ., ? and :

    Args:
        text(str): the test containing ., and :
    '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    skip_next = False
    string = ""
    for x in text:
        if skip_next:
            skip_next = False
            continue

        if x in ('.', '?', ':'):
            string += x + '\n' + '\n'
            skip_next = True
        else:
            string += x
    print(string)
