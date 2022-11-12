import numpy as np
import matplotlib.pyplot as plt
from polinomio_newton import Newton


def fun(x):
	y = (x**3 - np.sqrt(x))
	return y

#intervallo di interpolazione
a = 5
b = 45
n = 3 #grado del polinomio

#nodi di interpolazione e i valori associati
xn = np.linspace(a, b, n+1)
yn = fun(xn)

#punti in cui calcolare il polinomio e la funzione
x = np.linspace(a, b, 200)

#calcolo il polinomio
pn = Newton(xn, yn, x)

fx = fun(x)

#grafico del polinomio
plt.figure(1)
plt.plot(x, fx, "k-", label="f(x)")
plt.plot(x, pn, "b-", label="pn(x)")
plt.legend()
plt.show()

#grafico del resto
plt.figure(2)
plt.semilogy(x, abs(fx-pn), label="|f(x) - Pn(x)|")
plt.legend()
plt.show()