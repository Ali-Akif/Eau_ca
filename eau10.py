# INDEX WANTED

import sys


# Part 1 : Error Handling and Slicing

if sys.argv[1:]:
    chaine = sys.argv[1:]
    last_word = chaine[-1]
    chaine.pop()
else:
    print("erreur")
    exit()

# Part 2 : Resolution and Display

if last_word in chaine:
    index_wanted = chaine.index(last_word)
    print(index_wanted)
else:
    print("-1")
