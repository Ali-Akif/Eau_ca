#STRING IN STRING

import sys


# Part 1 : Error Handling

if len(sys.argv) != 3 and "".join(sys.argv[1:]).isdigit(): 
    print("erreur.")
    exit()


# Slicing, Resolution and Display

arg1, arg2 = sys.argv[1], sys.argv[2]
verif = arg1.count(arg2)

if verif == 1:
    print(True)
else:
    print(False)

