#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__("12-roman_to_int").roman_to_int

roman_number = "CCM"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IICIID"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VIIM"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
