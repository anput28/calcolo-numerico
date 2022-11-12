import numpy as np
import matplotlib.pyplot as plt
from polinomio_lagrange import Lagrange

def fun(x):
	y = (2*x)/(1-x**2)
	return y

def Chebyshev(a, b, n):
	xn = np.zeros(n)
	for i in range(n):
		cos = np.cos(((2*i + 1)/(2*n + 2)) * np.pi)
		xn[i] = a + (cos - 1)*((b-a)/2)
	return xn

#intervallo di interpolazione
a = 5 
b = 15

#nodi in cui calcolare la funzione e il polinomio
x = np.linspace(a, b, 200)

#calcolo la funzione
fx = fun(x)

#calcolo il polinomio di lagrange al variare di n grado del polinomio
nmax = 10
Rn = np.zeros(nmax)
Rn2 = np.zeros(nmax)
for n in range(nmax):

	#nodi di interpolazione e valori associati
	xn = np.linspace(a, b, n+1)
	yn = fun(xn)

	#calcolo il polinomio di Lagrange
	px = Lagrange(xn, yn, x)

	#nodi di Chebyshev e valori associati
	xn2 = Chebyshev(a, b, n+1)
	yn2 = fun(xn2)

	px2 = Lagrange(xn2, yn2, x)

	#conservo il resto
	Rn[n] = max(abs(fx-px))

#grafico dei resti
plt.figure(1)
plt.semilogy(range(nmax), Rn, "k-", label="Rn(x) nodi equispaziati")
plt.semilogy(range(nmax), Rn2, "b-", label="Rn(x) nodi Chebyshev")
plt.legend()
plt.show()