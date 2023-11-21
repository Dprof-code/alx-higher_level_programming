#!/usr/bin/python3

try:
    file = open("mydata2.txt", "r")
except FileNotFoundError:
    print("This file doesnt exist")
else:
    print(file.read())
    file.close()
finally:
    file_2 = open("mydata3.txt", "r")
