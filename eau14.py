# ORD ASCII

import sys

# Part 1 : Function

def sort_by_ascii(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


# Part 2: Error Handling

if not (len(sys.argv) > 2 and " ".join(sys.argv[1:]).istitle()):
    print("erreur")
    exit()


# Part 3 : Resolution and Display
    
sorted_array = sort_by_ascii(sys.argv[1:])
print(" ".join(sorted_array))