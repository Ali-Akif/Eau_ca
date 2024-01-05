# VALUE BETWEEN TWO NUMBERS

import sys


# Part 1 : Error Handling

if not (len(sys.argv) == 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit()):
    print("erreur")
    exit()


# Part 2 : Slicing
    
number1 = int(sys.argv[1])
number2 = int(sys.argv[2])


# Part 3 : Resolution and Display

if number1 > number2:
    number1, number2 = number2, number1

while number1 != number2 + 1:
    print(number1, end =" ")
    number1 += 1
