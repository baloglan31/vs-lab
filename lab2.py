import random

def random_siyahi_ve_cem(n):
    siyahi = [random.random() for _ in range(n)]
    cem = sum(siyahi)
    return siyahi, cem

n = int(input("Neçə ədəd təsadüfi ədəd olsun? "))
siyahi, cem = random_siyahi_ve_cem(n)

print("Siyahı:", siyahi)
print("Cəmi:", cem)
