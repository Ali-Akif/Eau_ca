# UPPER

import sys


# Part 1 : Error Handling

if len(sys.argv) != 2:
    print("erreur")
    exit()
elif sys.argv[1].isdigit():
    print("erreur")
    exit()
else:
    a = sys.argv[1]


# Part 2 : Slicing
    
result = ""
a = a.split(" ")


# Part 3 : Resolution

for i in range(len(a)):
    result += a[i][0].upper()
    result += a[i][1:].lower()
    result += " "


#Part 4 : Display
    
print(result)
