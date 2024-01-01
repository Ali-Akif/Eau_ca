# SUPERIOR PRIME NUMBER

import sys


# Part 1 : Function

def nombre_premier_superieur(n):
    n = int(n)
    for i in range(n + 1, n + 21):
        divisible = False
        for nombre in [2, 3, 4, 5, 6, 7, 8, 9]:
            if i % nombre == 0 and i != nombre:
                divisible = True
                break
        if not divisible:
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