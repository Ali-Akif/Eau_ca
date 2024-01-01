# REVERSE TERMINAL ARGUMENTS

import sys


# Part 1 : Slicing

terminal_arguments = sys.argv


# Part 2 : Error Handling, Resolution and Display

if len(terminal_arguments) < 2:
    print("erreur.")
    exit()
else:
    print("\n".join(terminal_arguments[:0:-1]))