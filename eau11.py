# MIN ABSOLUTE DIFFERENCE

import sys


# Part 1 : Error Handling

if len(sys.argv) < 2 and not sys.argv[1:].isdigit():
    print("erreur.")
    exit()


# Part 2 : Slicing
    
numbers = sorted(sys.argv[1:])


# Part 3 : Resolution

results = int(numbers[1]) - int(numbers[0])


# Part 4 : Display

print(results)

