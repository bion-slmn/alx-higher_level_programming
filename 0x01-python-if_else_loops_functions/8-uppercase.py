#!/usr/bin/python3
# uppercase convert string to uppercase
# str is the string to be converted to uppercase

def uppercase(str):
    for x in str:
        charNo = ord(x)
        if charNo >= 97 and charNo <= 122:
            charNo -= 32
        print("{}".format(chr(charNo)), end="")
    print("")
