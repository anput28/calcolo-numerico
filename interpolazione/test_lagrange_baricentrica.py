import numpy as np
import matplotlib.pyplot as plt
from polinomio_lagrange_baricentrica import Lagrange

def fun(x):
	y = x**3 - np.sqrt(x)
	return y

#definisco l'intervallo di interpolazione e il grado del polinomio
a = 5
b = 20

n = 40

#definisco i nodi di interpolazione e i valori associati
xn = np.linspace(a, b, n+1)
yn = fun(xn)

#nodi in cui calcolare il polinomio
x = np.linspace(a, b, 200)

#calcolo il polinomio di interpolazione
px = Lagrange(xn, yn, x)

#calcolo la funzione nei punti x
fx = fun(x)

#creo il grafico del polinomio
plt.figure(1)
plt.plot(x, px, "k-", label="p(x)")
plt.plot(x, fx, "b-", label="f(x)")
plt.legend()
plt.show()

#creo il grafico del resto
plt.figure(2)
plt.semilogy(x, abs(fx-px), "k-", label="||f(x) - p(x)||")
plt.legend()
plt.show()