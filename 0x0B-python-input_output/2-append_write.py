#!/usr/bin/python3
'''this module has a function that writes to a file'''


def append_write(filename="", text=""):
    '''write_file wwrites to a file,
    it creates the file if doesnt exist and overwite content'''
    with open(filename, 'a', encoding='utf-8') as myfile:
        charNum = myfile.write(text)
        return charNum
