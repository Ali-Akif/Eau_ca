#COMBINATION OF 2 NUMBERS

liste =[]

for i in range(100):
    for e in range(i + 1,100):
        liste.append(f"{i:02d} {e:02d}")

print(", ".join(liste))