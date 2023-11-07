#!/usr/bin/python3

def multiple_returns(sentence):
    """
        multiple_returns - returns a tuple with the
        length of a string and its first character.
    """

    length = len(sentence)

    if len(sentence) < 1:
        first = None
    else:
        first = sentence[0]

    return (length, first)
