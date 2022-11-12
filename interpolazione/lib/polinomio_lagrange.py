'''
======================================================
@author Angelo Putignano

@file polinomio_lagrange.py
@version 0.1
======================================================
'''

'''
==============================================================================
Libreria che contiene tutte le routine per implementare la formula di
Lagrange per la costruzione di un polinomio di interpolazione
==============================================================================
'''

import numpy as np
import matplotlib.pyplot as plt

'''
==============================================================================
POLINOMIO DI LAGRANGE

Questo metodo costruisce un polinomio di interpolazione con la formula di 
Lagrange.
==============================================================================
-------------------------------------INPUT------------------------------------
Parametri:
	- xn : array di nodi di interpolazione
	- yn : array di valori associati ai nodi di interpolazione
	- x : array di valori in cui calcolare il polinomio
------------------------------------------------------------------------------

-------------------------------------OUTPUT-----------------------------------
Parametri:
	- p : polinomio di interpolazione
------------------------------------------------------------------------------
'''
def Lagrange(xn, yn, x):
	n = len(x)

	p = np.zeros(n)
	for i in range(n):
		for j in range(len(xn)):
			p[i] += yn[j]*L(x[i], xn, j)
	return p

'''
==============================================================================
Metodo che calcola un elemento della base di Lagrange
==============================================================================
-------------------------------------INPUT------------------------------------
Parametri:
	- xi : punto in cui si sta calcolando il polinomio
	- xn : array di nodi di interpolazione
	- j : indice che indica quale elemento della base di Lagrange deve essere calcolato
------------------------------------------------------------------------------

-------------------------------------OUTPUT-----------------------------------
Parametri:
	- L : elemento j-esimo della base di Lagrange
------------------------------------------------------------------------------
'''
def L(xi, xn, j):
	N = Nj(xi, xn, j)
	D = Dj(xn, j)

	Lj = N/D
	return Lj

'''
==============================================================================
Routine che calcola la parte del j-esimo elemento della base di Lagrange che
dipende da xi punto in cui si sta calcolando il polinomio di interpolazione.
==============================================================================
-------------------------------------INPUT------------------------------------
Parametri:
	- xi : punto in cui si sta calcolando il polinomio
	- xn : array di nodi di interpolazione
	- j : indice che indica quale elemento della base di Lagrange si sta calcolando
------------------------------------------------------------------------------

-------------------------------------OUTPUT-----------------------------------
Parametri:
	- N : parte del j-esimo elemento della base di Lagrange che dipende da xi
------------------------------------------------------------------------------
'''
def Nj(xi, xn, j):
	N = 1
	for k in range(len(xn)):
		if k != j:
			N = N * (xi - xn[k])

	return N

'''
==============================================================================
Routine che calcola la parte fissa del j-esimo elemento della base di Lagrange.
==============================================================================
-------------------------------------INPUT------------------------------------
Parametri:
	- xn : array di nodi di interpolazione
	- j : indice che indica quale elemento della base di Lagrange si sta calcolando
------------------------------------------------------------------------------

-------------------------------------OUTPUT-----------------------------------
Parametri:
	- D : parte fissa del j-esimo elemento della base di Lagrange.
------------------------------------------------------------------------------
'''
def Dj(xn, j):
	n = len(xn)

	#matrice che memorizza le differenze
	X = np.eye(n)
	for i in range(n):
		for k in range(n):
			if k > i:
				X[i, k] = xn[i] - xn[k]
			elif k < i:
				X[i, k] = -X[k, i]

	#proddo delle differenze della matrice
	Dj = np.prod(X[j, :])

	return Dj

