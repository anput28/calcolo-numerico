'''
======================================================
@author Angelo Putignano

@file radici_funzione.py
@version 0.1
======================================================



==================================================================
Libreria che contiene funzioni che permettono di trovare le radici
di una funzione.
I metodi contenuti in questa libreria permettono di trovare una sola 
radice della funzione, anche se la funzione ne ha più di una.

indice libreria:
	- Metodo delle bisezioni successive
	- Metodo delle tangenti
	- Metodo delle secanti
	- Metodo delle corde
===================================================================
'''

import numpy as np
from math import ceil
from scipy.misc import derivative


'''
==============================================================================
METODO DELLE BISEZIONI SUCCESSIVE

Questa routine implementa in metodo delle bisezioni successive che permette di 
trovare una approssimazione della radice di una certa funzione.
==============================================================================
-------------------------------------INPUT------------------------------------
Parametri:
	- a, b : estremi del dominio della funzione
	- tol : accuratezza che l'approssimazione della radice deve raggiungere
	- fun : funzione di cui si vuole trovare la radice
------------------------------------------------------------------------------

-------------------------------------OUTPUT-----------------------------------
Parametri:
	- c : approssimazione della radice della funzione
------------------------------------------------------------------------------
'''
def bisezioni_successive(a, b, tol, fun):
	#verifico la presenza della radice
	fa = fun(a); fb = fun(b)
	if fa*fb > 0:
		print("Errore: la presenza della radice non è garantita nell'intervallo [%d, %d]." % (a,b))
	else:
		#calcolo il numero di iterazioni per raggiungere la tolleranza
		n = ceil(np.log2(b-a) - np.log2(tol) - 1)
		for k in range(n+1):
			c = (a+b)/2
			fc = fun(c)
			if fa*fc < 0:
				b=c
			else:
				a=c; fa = fc
	return c

'''
==============================================================================
METODO DELLE TANGENTI (O DI NEWTON)

Questa routine implementa in metodo delle tangenti che permette di 
trovare una approssimazione della radice di una certa funzione.
==============================================================================
-------------------------------------INPUT------------------------------------
Parametri:
	- x0 : approssimazione iniziale
	- fun : funzione di cui si vuole trovare la radice
	- tol : accuratezza che l'approssimazione della radice deve raggiungere
	- kmax : numero massimo di iterazioni da compiere
------------------------------------------------------------------------------

-------------------------------------OUTPUT-----------------------------------
Parametri:
	- x1 : approssimazione della radice della funzione
------------------------------------------------------------------------------
'''
def metodo_tangenti(x0, fun, tol, kmax):
	stop = False
	k = 0

	while not(stop) and k < kmax:
		#calcolo gli elmenti da applicare nella formula
		y0 = fun(x0)
		d0 = derivative(fun, x0)

		#calcolo la nuova approssimazione
		x1 = x0 - (y0/d0)

		#verifico se si è raggiunta l'accuratezza tramite i criteri di arresto
		stop = abs(fun(x1)) + ( abs(x1-x0)/(1+abs(x1)) ) < tol/5
		x0 = x1
		k +=1

	return x1

'''
==============================================================================
METODO DELLE SECANTI

Questa routine implementa in metodo delle secanti che permette di 
trovare una approssimazione della radice di una certa funzione.
Il metodo delle secanti è una variazione più lenta del metodo delle tangenti.
==============================================================================
-------------------------------------INPUT------------------------------------
Parametri:
	- x0, x1: intervallo in cui calcolare il rapporto incrementale (coeff. angol.
			  retta secante)
	- fun : funzione di cui si vuole trovare la radice
	- tol : accuratezza che l'approssimazione della radice deve raggiungere
	- kmax : numero massimo di iterazioni da compiere
------------------------------------------------------------------------------

-------------------------------------OUTPUT-----------------------------------
Parametri:
	- x2 : approssimazione della radice della funzione
------------------------------------------------------------------------------
'''
def metodo_secanti(x0, x1, fun, tol, kmax):
	stop = False
	k = 0

	while not(stop) and k < kmax:
		#calcolo gli elmenti da applicare nella formula
		y1 = fun(x1)
		s1 = (fun(x1)-fun(x0))/(x1-x0) #rapporto incrementale

		#calcolo la nuova approssimazione
		x2 = x1 - (y1/s1)

		#verifico se si è raggiunta l'accuratezza tramite i criteri di arresto
		stop = abs(fun(x2)) + ( abs(x2-x1)/(1+abs(x2)) ) < tol/5
		x0 = x1
		x1 = x2
		k +=1

	return x2

'''
==============================================================================
METODO DELLE CORDE

Questa routine implementa in metodo delle corde che permette di 
trovare una approssimazione della radice di una certa funzione.
Il metodo delle corde è una variazione più lenta del metodo delle tangenti.
==============================================================================
-------------------------------------INPUT------------------------------------
Parametri:
	- x0: approssimazione iniziale
	- fun : funzione di cui si vuole trovare la radice
	- m : coefficiente angolare delle rette che vengono costruite
	- tol : accuratezza che l'approssimazione della radice deve raggiungere
	- kmax : numero massimo di iterazioni da compiere
------------------------------------------------------------------------------

-------------------------------------OUTPUT-----------------------------------
Parametri:
	- x1 : approssimazione della radice della funzione
------------------------------------------------------------------------------
'''
def metodo_corde(x0, fun, m, tol, kmax):
	stop = False
	k = 0 

	while not(stop) and k <= kmax:
		f0 = fun(x0)
		x1 = x0 - (f0/m)

		stop = abs(fun(x1)) + (abs(x1-x0)/(1+abs(x1))) < tol

		x0 = x1
		k = k+1
	return x1
