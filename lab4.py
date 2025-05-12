def g(x, lam):
    return x - lam * (x**0.5) * math.cos(x**0.5)

def simple_iteration(x0, lam, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = g(x, lam)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x
