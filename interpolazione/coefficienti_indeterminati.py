import numpy as np
import matplotlib.pyplot as plt

def fun(x):
	y = np.exp(np.sqrt(x-2))
	return y

#================ Dati di iterpolazione ================
#intervallo di interpolazine
a = 5
b = 50

n = 3 #grado del polinomio

xn = np.linspace(a, b, n+1) #nodi di interpolazione
yn = fun(xn) #valori di interpolazione
#=======================================================

#================ Calcolo del polinomio ================
x = np.linspace(a, b, 200)

p_coeff = np.polyfit(xn, yn, n)
px = np.polyval(p_coeff, x)
#=======================================================

#================ Calcolo della funzione ================
fx = fun(x)
#========================================================


plt.figure(1)
plt.plot(x, px, "k-", label="p(x)")
plt.plot(x, fx, "b-", label="f(x)")
plt.plot(xn, yn, "ro")
plt.legend()
plt.show()

#grafico del resto
plt.figure(2)
plt.semilogy(x, abs(fx-px))
plt.legend()
plt.show()