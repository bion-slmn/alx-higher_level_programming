# islower checks if a character is in lower case
# c is the character that is passed to be checked

def islower(c):
    x = ord(c)
    if x >= 97 and x <= 122:
        return (True)
    else:
        return (False)
