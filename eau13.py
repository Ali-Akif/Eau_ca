# SELECTION SORT

import sys

# Part 1 : Function

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for value in range(i + 1, len(array)):
            if int(array[min_index]) > int(array[value]):
                min_index = value
        array[min_index], array[i] = array[i], array[min_index]
    return array


# Part 2 : Error Handling

if not (len(sys.argv) > 2 and "".join(sys.argv[1:]).isdigit()):
        print("erreur")
        exit()


# Part 3 : Slicing and Convertion

input_array = sys.argv[1:]
sorted_array = selection_sort(input_array)


# Part 4 : Display

print(", ".join(sorted_array))