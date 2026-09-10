import sympy as sp

x = sp.symbols("x")
expr1 = 1//(x**x)

lim1 = sp.limit(expr1, x, sp.oo)
print(lim1)

# This program is taking very long to complete running. And, gives no result.
# Will fix later
