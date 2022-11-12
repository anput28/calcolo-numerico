from numpy import log2
from math import ceil

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
	#verificando la presenza della radice
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