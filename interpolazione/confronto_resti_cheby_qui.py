import numpy as np
import matplotlib.pyplot as plt
from polinomio_lagrange import Lagrange

def fun(x):
	y = np.sqrt(5-np.cos(x))
	return y

def Chebyshev(a, b, n):
	xn = np.zeros(n)
	for i in range(n):
		cos = np.cos(((2*i + 1)/(2*n + 2)) * np.pi)
		xn[i] = a + (cos + 1)*((b-a)/2)
	return xn

#intervallo di interpolazione
a = 5 
b = 20
n = 10

#nodi in cui calcolare la funzione e il polinomio
x = np.linspace(a, b, 200)

#calcolo la funzione
fx = fun(x)

#nodi equispaziati e valori associati
xn = np.linspace(a, b, n+1)
yn = fun(xn)
px = Lagrange(xn, yn, x)

#nodi Chebyshev e valori associati
xn2 = Chebyshev(a, b, n+1)
yn2 = fun(xn2)
px2 = Lagrange(xn2, yn2, x)


#grafico dei polinomi
plt.figure(1)
plt.plot(x, px, "k-", label="pn(x) equispaziati")
plt.plot(x, px2, "b-", label="pn(x) Chebyshev")
plt.plot(x, fx, "r-", label="f(x)")
plt.legend()
plt.show()

#grafico resti
plt.figure(2)
plt.semilogy(x, abs(fx-px), "k-", label="Rn(x) equispaziati")
plt.legend()
plt.show()

#grafico resti
plt.figure(3)
plt.semilogy(x, abs(fx-px2), "b-", label="Rn(x) Chebyshev")
plt.legend()
plt.show()