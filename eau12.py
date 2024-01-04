# BUBBLE SORT

import sys


# Part 1 : Function

def bubble_sort(list):
    compteur = len(list)

    for _ in range(compteur):

        for i in range(1, len(list)):
            if int(list[i - 1]) > int(list[i]):
                list[i - 1], list[i] = list[i], list[i - 1]

        compteur -= 1

    return(list)


# Part 2 : Error Handling

if not (len(sys.argv) > 2 and "".join(sys.argv[1:]).isdigit()):
    print("error")
    exit()


# Part 3 : Parcing
    
array = sys.argv[1:]


# Part 4 : Resolution

result = bubble_sort(array)


# Part 5 : Display

print(result)





