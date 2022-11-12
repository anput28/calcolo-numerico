import numpy as np

def Lagrange(xn, yn, x):
	zn = coefficienti(xn, yn)

	n = len(x)
	p = np.zeros(n)
	for i in range(n):
		p[i] = calcolo_polinomio(xn, zn, yn, x[i])
	return p

def coefficienti(xn, yn):
	n = len(xn)

	#calcolo le differenze della produttoria in una matrice X
	X = np.eye(n)
	for j in range(n):
		for k in range(n):
			if k > j:
				X[j, k] = xn[j] - xn[k]
			elif k < j:
				X[j, k] = -X[k, j]

	#calcolo gli zj
	zn = np.zeros(n)
	for j in range(n):
		zn[j] = yn[j]/np.prod(X[j, :])

	return zn

def calcolo_polinomio(xn, zn, yn, xi):
	check_nodi = abs(xi-xn) < 1.0e-14

	if True in check_nodi:
		temp = np.flatnonzero(check_nodi == True)
		pn = yn[temp[0]]
	else:
		n = len(xn)
		somma = 0
		for j in range(n):
			somma = somma + (zn[j]/(xi - xn[j]))
		pn = np.prod(xi-xn) * somma
	return pn
