# FIBONACCI

import sys


# Part 1 : Function

def fibonacci(given_int):
    if given_int == 0:
        return 0
    elif given_int == 1:
        return 1

    a, b = 0, 1
    for i in range(given_int - 1):
        a, b = b, a + b

    return b


# Part 2 : Error Handling

if not (len(sys.argv) == 2 and sys.argv[1].isdigit()):
    print("erreur")
    exit()


# Part 3 : Resolution, Slicing and Display
    
index = int(sys.argv[1])
print(fibonacci(index))

