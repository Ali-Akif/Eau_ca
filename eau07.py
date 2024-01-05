# UPPER

import sys


# Part 1 : Error Handling and Slicing

if len(sys.argv) != 2 or sys.argv[1].isdigit():
    print("erreur")
    exit()
else:
    arguments = sys.argv[1].split(" ")
    result = ""


# Part 2 : Resolution

for i in range(len(arguments)):
    result += arguments[i][0].upper()
    result += arguments[i][1:].lower()
    result += " "


#Part 3 : Display
    
print(result)
