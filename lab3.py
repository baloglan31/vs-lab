import random

def iki_olculu_massiv_ve_cem(n, m):
    massiv = [[random.randint(1, 9) for _ in range(m)] for _ in range(n)]
    cem = sum(sum(satir) for satir in massiv)
    return massiv, cem

n = int(input("Sətir sayı (n): "))
m = int(input("Sütun sayı (m): "))
massiv, cem = iki_olculu_massiv_ve_cem(n, m)

print("Massiv:")
for satir in massiv:
    print(satir)
print("Cəmi:", cem)
