# INDEX WANTED

import sys


# Part 1 : Error Handling

if sys.argv[1:]:
    chaine = sys.argv[1:]
else:
    print("erreur")
    exit()


# Part 2 : Slicing
    
last_word = chaine[-1]
chaine.pop()


# Part 3 : Resolution and Display

if last_word in chaine:
    index_wanted = chaine.index(last_word)
    print(index_wanted)
else:
    print("-1")
