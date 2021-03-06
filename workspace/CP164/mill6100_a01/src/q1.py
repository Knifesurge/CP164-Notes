"""
------------------------------------------------------------------------
Assignment 1, Task 1: Substitute
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-08
------------------------------------------------------------------------
"""
from functions import substitute

file_handle_r = open("pelee.txt", "r")
file_handle_w = open("substitute.txt", "w")

# Read the file
file_handle_r.seek(0)
file_contents = file_handle_r.readlines()
plaintext = "".join(file_contents)  # Create a single string to hold the contents of the file

cipher = "DAVIBROWNZCEFGHJKLMPQSTUXY"

estring = substitute(plaintext, cipher)

print(estring)

for char in estring:
    file_handle_w.write(char)