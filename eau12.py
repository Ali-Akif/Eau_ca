# BUBBLE SORT

import sys


# Part 1 : Function

def bubble_sort(list):
    for _ in range(len(list)):
        for i in range(len(list) - 1):
            if int(list[i]) > int(list[i+1]):
                list[i], list[i+1] = list[i+1], list[i]
    return(list)


# Part 2 : Error Handling

if not (len(sys.argv) > 2 and "".join(sys.argv[1:]).isdigit()):
    print("error")
    exit()


# Part 3 : Parcing
    
array = sys.argv[1:]


# Part 4 : Resolution

result = ", ".join(bubble_sort(array))


# Part 5 : Display

print(result)





