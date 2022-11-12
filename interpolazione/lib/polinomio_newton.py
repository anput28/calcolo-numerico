'''
======================================================
@author Angelo Putignano

@file polinomio_newton.py
@version 0.1
======================================================

==============================================================================
Libreria che contiene tutte le routine per implementare la formula di Newton
per la costruzione di un polinomio di interpolazione.
==============================================================================
'''

import numpy as np

'''
==============================================================================
POLINOMIO DI NEWTON

Questo metodo costruisce un polinomio di interpolazione con la formula di Newton.
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
def Newton(xn, yn, x):
	#calcolo i coefficienti del polinomio
	dn = differenze_successive(xn, yn)

	#calcolo il polinomio
	n = len(xn)
	p = dn[n-1]
	for i in range(n-2, -1, -1):
		p = dn[i] + p*(x-xn[i])
	return p

'''
==============================================================================
Questo metodo calcola i coefficienti del polinomio di newton una riformulazione
del metodo delle differenze divise.
==============================================================================
-------------------------------------INPUT------------------------------------
Parametri:
	- xn : array di nodi di interpolazione
	- yn : array di valori associati ai nodi di interpolazione
------------------------------------------------------------------------------

-------------------------------------OUTPUT-----------------------------------
Parametri:
	- dn : array dei coefficienti da usare nel polinomio di Newton.
------------------------------------------------------------------------------
'''
def differenze_successive(xn, yn):
	#inizializzo il vettore
	n = len(xn)

	dn = yn
	#rappresenta i passi da fare per arrivare ad ottenere i valori finali nel vettore
	for j in range(1, n): 
		#itera sugli elementi del vettore
		for i in range(n-1, j-1, -1):
			dn[i] = (dn[i] - dn[i-1])/(xn[i] - xn[i-j])
	return dn

