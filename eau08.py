# ONLY DIGITS

import sys


# Part 1 : Error Handling

if len(sys.argv) != 2:
    print("erreur.")
    exit()


# Part 2 : Resolution
    
for i  in sys.argv[1]:
    if not ( i >= "0" and i <= "9"):
        only_digit = False
        break    
    else:
        only_digit = True
        


# Part 3 : Display
    
print(only_digit)
