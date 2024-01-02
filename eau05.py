#STRING IN STRING

import sys


# Part 1 : Error Handling

if len(sys.argv) != 3:
    print("erreur.")
    exit()
else:
    a = sys.argv[1]
    b = sys.argv[2]

if a.isdigit() or b.isdigit():
    print("erreur.")
    exit()


# Slicing, Resolution and Display
    
verif = a.count(b)

if verif == 1:
    print(True)
else:
    print(False)

