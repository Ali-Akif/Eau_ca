# COMBINATION OF 3 NUMBERS


liste = []

for a in range(10):
    for b in range(a, 10):
        for c in range(b, 10):
            if a != b and a != c and b != c:
                nombre_a_tester = f"{a}{b}{c}"
                liste.append(nombre_a_tester)

print(", ".join(liste))
