# COMBINATION OF 3 NUMBERS


liste = []

for a in range(10):
    for b in range(a + 1, 10):
        for c in range(b + 1, 10):
            nombre_a_tester = f"{a}{b}{c}"
            liste.append(nombre_a_tester)

print(", ".join(liste))
