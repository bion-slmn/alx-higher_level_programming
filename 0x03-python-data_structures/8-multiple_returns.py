#!/usr/bin/python3

# multiple_returns - returns tuple with length of string
# and its first character.
# If the sentence is empty, the first character should be equal to None

def multiple_returns(sentence):
    length = len(sentence)

    if length == 0:
        first = None
    else:
        first = sentence[0][0]

    return length, first
