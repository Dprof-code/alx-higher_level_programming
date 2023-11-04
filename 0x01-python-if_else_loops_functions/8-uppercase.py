#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if (ord(char) >= 97 and ord(char) <= 122):
            upper_code = 90 - (122 - ord(char))
            print("{}".format(chr(upper_code)), end="")
        else:
            print("{}".format(char), end="")
    print("")
