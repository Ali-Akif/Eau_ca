# UPPER 1/2

import sys


# Part 1 : Function

def upper_every_two_car(given_string):
    count = 0
    result = ""
    for i in given_string:
        if i.isalpha():
            if count % 2 == 0:
                result += i.upper()
            else:
                result += i.lower()
            count += 1
        else:
            result += i
    return result


# Part 2 : Error Handling

if len(sys.argv) != 2:
    print("erreur.")
    exit()
elif sys.argv[1].isdigit():
    print("erreur.")
    exit()
else:
    a = sys.argv[1]


# Part 3 : Slicing
    
output = upper_every_two_car(a)


# Part 4 : Display

print(output)
