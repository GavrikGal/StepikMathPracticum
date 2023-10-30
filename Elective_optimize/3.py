from scipy.optimize import golden


a = 3
b = 4

def f(x):
    return (x + a)**2 - b

def g(x):
    return abs(f(x))


min_f = golden(f, brack=(-10, -4))
min_g = golden(g, brack=(-10, -4))

print(f(min_f), g(min_g))