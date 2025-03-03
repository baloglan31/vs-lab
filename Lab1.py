import math


y = 3
epsilon = 0.001
n = 2  

term = 4 / math.factorial(2)  
while abs(term) >= epsilon:
    y += term
    n += 1
    term = (n + 2) / math.factorial(n) 

print(f"netice: {y:.6f}")
