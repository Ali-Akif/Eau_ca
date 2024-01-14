# REVERSE TERMINAL ARGUMENTS

import sys


# Part 1 : Slicing

input_args = sys.argv


# Part 2 : Error Handling, Resolution and Display

if len(input_args) < 2:
    print("erreur.")
    exit()
else:
    print("\n".join(input_args[:0:-1]))