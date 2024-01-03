# VALUE BETWEEN TWO NUMBERS

import sys


# Part 1 : Error Handling

if len(sys.argv) != 3:
    print("erreur")
    exit()
elif not (sys.argv[1].isdigit() and sys.argv[2].isdigit()):
    print("erreur")
    exit()


# Part 2 : Slicing
    
a = int(sys.argv[1])
b = int(sys.argv[2])


# Part 3 : Resolution and Display

if a > b:
    a, b = b, a

for i in  range(a, b + 1):
    print(i, end = " ")