import numpy as np
import matplotlib.pyplot as plt
from polinomio_lagrange import Lagrange

def fun(x):
	y = np.sin(x)
	return y

a = 0
b = 3*np.pi

n = 5
xn = np.linspace(a,b, n+1)
yn = fun(xn)

#calcolo la funzione
x = np.linspace(a,b, 200)
fx = fun(x)

#calcolo polinomio
px = Lagrange(xn, yn, x)

plt.figure(1)
plt.plot(x, fx, "k-", label="f(x)")
plt.plot(x, px, "b-", label="pn(x)")
plt.legend()
plt.show()