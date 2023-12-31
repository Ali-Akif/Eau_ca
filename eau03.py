import sys


# Part 1 : Function

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b

    return b


# Part 2 : Error Handling

if len(sys.argv) != 2:
    print("Erreur : Veuillez fournir un seul argument.")
    exit()
elif not sys.argv[1].isdigit():
    print("Erreur : L'argument doit être un nombre entier positif.")
    exit()


# Part 3 : Resolution, Slicing and Display
    
index = int(sys.argv[1])
print(fibonacci(index))

