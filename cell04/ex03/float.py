#!/usr/bin/env python3
num1 = float(input("Give me a number: "))

decimal = num1 - int(num1)
if not decimal:
    print("This number is an integer.")
else:
    print("This number is a decimal.")
    
