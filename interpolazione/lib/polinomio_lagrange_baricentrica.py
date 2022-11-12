'''
======================================================
@author Angelo Putignano

@file polinomio_lagrange_baricentrica.py
@version 0.1
======================================================

==============================================================================
Libreria che contiene tutte le routine per implementare la prima formula 
baricentrica di Lagrange per la costruzione di un polinomio di interpolazione.
==============================================================================
'''

import numpy as np

'''
==============================================================================
POLINOMIO DI LAGRANGE

Questo metodo costruisce un polinomio di interpolazione con la prima formula 
baricentrica di Lagrange.
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
	zn = coefficienti(xn, yn)

	n = len(x)
	p = np.zeros(n)
	for i in range(n):
		p[i] = calcolo_polinomio(xn, zn, yn, x[i])
	return p

'''
==============================================================================
Questo metodo calcola i coefficienti zj.
==============================================================================
-------------------------------------INPUT------------------------------------
Parametri:
	- xn : array di nodi di interpolazione
	- yn : array di valori associati ai nodi di interpolazione
------------------------------------------------------------------------------

-------------------------------------OUTPUT-----------------------------------
Parametri:
	- zn : array dei coefficienti da usare nel polinomio di Lagrange
------------------------------------------------------------------------------
'''
def coefficienti(xn, yn):
	n = len(xn)

	'''
	Calcolo le differenze della produttoria in una matrice X,
	per fare meno operazioni si calcolano metà delle differenze
	e le altre si ottengono cambiando il segno a quelle già ottenute.
	'''
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

'''
==============================================================================
Questo metodo calcola il valore del polinomio di Lagrange, con formula
baricentrica, in un certo punto xi
==============================================================================
-------------------------------------INPUT------------------------------------
Parametri:
	- xn : array di nodi di interpolazione
	- yn : array di valori associati ai nodi di interpolazione
	- zn : array di coefficienti del polinomio
	- xi : punto in cui calcolare il valore del polinomio
------------------------------------------------------------------------------

-------------------------------------OUTPUT-----------------------------------
Parametri:
	- pn : valore del polinomio calcolato nel punto xi
------------------------------------------------------------------------------
'''
def calcolo_polinomio(xn, zn, yn, xi):
	#vettore di booleani
	check_nodi = abs(xi-xn) < 1.0e-14

	'''
	Controllo se xi è proprio uno dei nodi di interpolazione,
	in questo caso il valore del polinomio in questo punto è proprio
	il valore associato al nodo.
	'''
	if True in check_nodi:
		#recupero l'indice del nodo di interpolazione a cui xi è uguale
		temp = np.flatnonzero(check_nodi == True)
		pn = yn[temp[0]]
	else:
		n = len(xn)
		somma = 0
		for j in range(n):
			somma = somma + (zn[j]/(xi - xn[j]))
		pn = np.prod(xi-xn) * somma
	return pn
