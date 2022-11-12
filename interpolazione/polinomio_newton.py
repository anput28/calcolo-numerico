import numpy as np

def Newton(xn, yn, x):
	#calcolo i coefficienti del polinomio
	dn = differenze_successive(xn, yn)

	#calcolo il polinomio
	n = len(xn)
	p = dn[n-1]
	for i in range(n-2, -1, -1):
		p = dn[i] + p*(x-xn[i])
	return p

def differenze_successive(xn, yn):
	#inizializzo il vettore
	n = len(xn)

	dn = yn
	for j in range(1, n):
		for i in range(n-1, j-1, -1):
			dn[i] = (dn[i] - dn[i-1])/(xn[i] - xn[i-j])
	return dn

