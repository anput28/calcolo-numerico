'''
======================================================
@author Angelo Putignano

@file interpolazione.py
@version 0.1
======================================================
'''

'''
==============================================================================
Libreria che contiene funzioni che riguardano il problema dell'interpolazione

indice libreria:
	- Nodi di Chebyshev
	- Metodo dei coefficienti indeterminati
	- Formula di Lagrange normale
	- Prima formula baricentrica di Lagrange
	- Formula di Newton
==============================================================================
'''

import numpy as np
from algebra_lineare import risoluzione_sistema
import polinomio_lagrange as pl
import polinomio_newton as pn
import polinomio_lagrange_baricentrica as plb

'''
==============================================================================
NODI DI CHEBYSHEV

Questo metodo costruisce i nodi secondo la distribuzione di Chebyshev.
==============================================================================
-------------------------------------INPUT------------------------------------
Parametri:
	- a, b : estremi di interpolazione
	- n : grado del polinomio di interpolazione
------------------------------------------------------------------------------

-------------------------------------OUTPUT-----------------------------------
Parametri:
	- xn : nodi di interpolazione secondo la distribuzione di Chebyshev
------------------------------------------------------------------------------
'''
def Chebyshev(a, b, n):
	xn = np.zeros(n+1)
	for i in range(n+1):
		cos = np.cos( ((2*i + 1)/(2*n + 2)) * np.pi)
		xn[i] = a + (cos + 1)*((b-a)/2)
	return xn


'''
==============================================================================
METODO DEI COEFFICIENTI INDETERMINATI

Questo metodo permette di trovare i coefficienti di un polinomio di interpolazione
risolvendo un sistema di equazioni lineari creato dall'applicazione dei
vincoli di interpolazione ad un generico polinomio.
==============================================================================
-------------------------------------INPUT------------------------------------
Parametri:
	- xn : array di nodi di interpolazione
	- yn : array di valori associati ai nodi di interpolazione
------------------------------------------------------------------------------

-------------------------------------OUTPUT-----------------------------------
Parametri:
	- c : array dei coefficienti del polinomio di interpolazione
------------------------------------------------------------------------------
'''
def coefficienti_indeterminati(xn, yn):
	n = len(xn)

	#costruzione della matrice di Vandermonde
	Vm = np.ones((n,n))
	for j in range(1, n):
		for i in range(n):
			Vm[i, j] = xn[i]**j

	#risolvo il sistema di equazioni lineari
	c = risoluzione_sistema(Vm, yn)
	return c	