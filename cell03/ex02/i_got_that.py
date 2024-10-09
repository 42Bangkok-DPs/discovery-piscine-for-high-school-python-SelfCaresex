#!/usr/bin/env python3

word = "-1"

while True:
    if word == "-1":
        word = str(input("What you gotta say? : "))
    elif  word == "STOP":
        break
    else:
        print("I got that! Anything else? : ", end="")
        word = input()
