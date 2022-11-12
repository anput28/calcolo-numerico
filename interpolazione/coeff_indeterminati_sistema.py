import numpy as np
import matplotlib.pyplot as plt
import algebra_lineare as al

def fun(x):
	y = np.exp(np.sqrt(x-2))
	return y

#================ Dati di iterpolazione ================
#intervallo di interpolazine
a = 5
b = 50

n = 3 #grado del polinomio

xn = np.linspace(a,b, n+1)
yn = fun(xn) #valori di interpolazione
#=======================================================

#================ Calcolo del polinomio ================
x = np.linspace(a, b, 200)

Vm = np.zeros((n+1, n+1))
for i in range(n+1):
	for j in range(n+1):
		Vm[i,j] = xn[i]**j

c = al.risoluzione_sistema(Vm, yn)
px = np.polyval(np.flip(c), x)
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