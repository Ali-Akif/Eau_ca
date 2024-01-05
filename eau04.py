# SUPERIOR PRIME NUMBER

import sys


# Part 1 : Function

def nombre_premier_superieur(number_string):
    number_int = int(number_string)
    for i in range(number_int + 1, number_int + 21):
        for nombre in [2, 3, 4, 5, 6, 7, 8, 9]:
            if i % nombre == 0 and i != nombre:
                break
        else:
            print(i)
            exit()
            

# Part 2 : Error Handling and Slicing
            
if not (len(sys.argv) == 2 and sys.argv[1].isdigit()):
    print("erreur.")
    exit()
else:
    n = sys.argv[1]


# Part 3 : Display
    
nombre_premier_superieur(n)