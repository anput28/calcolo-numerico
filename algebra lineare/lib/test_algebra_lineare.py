'''
======================================================
@author Angelo Putignano

@file test_algebra_lineare.py
@version 0.1
======================================================
'''

'''
Questa libreria contiene le funzioni per testare funzioni che riguardano l'algebra lineare.

Contiene le routine per testare:
	- algoritmi che implementano il metodo di eliminazione di Gauss (con e senza pivoting);
	- algorimi di sostituzione in avanti e all'indietro;
	- algoritmi che implementano la fattorizzazione A = LU (con e senza pivoting);
	- test di velocità dell'algoritmo di fattorizzazione A=LU in versione normale e ottimizzata;
	- la risoluzione di sistemi di equazioni lineari applicando solo funzioni personali:
		+ risoluzione di sistemi applicando il proprio metodo di Gauss (con e senza pivoting)
		  e il proprio algoritmo di sostituzione all'indietro;
		+ risoluzione di sistemi applicando le proprie funzioni che implementano la
		  fattorizzazione A = LU (con e senza pivoting) e gli algoritmi di sostituzione;
	- algoritmi per il calcolo dell'inversa di una matrice;

Ogni funzione costruisce un sistema di n equazioni lineari, con n indicato dall'utente,
con dati random.
Stampa la soluzione attesa del sistema, la soluzione calcolata e l'errore assoluto e relativo
per verificare quanto la soluzione calcolata dista dalla soluzione attesa.

Nelle funzioni che testano algoritmi che NON restituiscono la soluzione del sistema (per esempio il M.E.G.
che non calcola la soluzione ma permette di trovare un sistema equivalente) il sistema test viene 
risolto con la routine numpy.linalg.solve() che appunto si occupa di risolvere sistemi di equazioni lineari.
'''


import algebra_lineare as al
import numpy as np
import time
import sys

'''
==================================================================
ROUTINE DI TEST PER ALGORITMI DEL METODO DI ELIMINAZIONE DI GAUSS

Breve descrizione:
Questa routine può testare qualsiasi algoritmo che implementi
il metodo di eliminazione di gauss, sia con pivoting che senza.
Costruisce un sistema test di equazioni lineari, applica il M.E.G. 
passato come parametro alla matrice dei coefficienti e al vettore 
dei termini noti costruiti e risolve il sistema con una routine
di python tramite la nuova matrice e il nuovo vettore ottenuti dal
M.E.G.. 
Calcola l'errore assoluto e relativo sulla soluzione ottenuta,
confrontandola con la soluzione attesa.
==================================================================
------------------------INPUT---------------------------
Parametri:
	- dim : dimensione che dovranno avere la matrice dei coefficienti,
			il vettore dei termini noti e il vettore delle soluzioni.
	- elim_Gauss_func : algoritmo del metodo di gauss da testare
---------------------------------------------------------
'''
def test_eliminazione_gauss(dim, elim_Gauss_func):
	#costruzione del problema test
	n = dim
	'''
	A sarà formata da valori compresi tra -10 e 10:
	2*np.random.random((n,n)) - 1 permette di avere positivi e 
	negativi intorno allo zero, quindi si moltiplica per un certo
	numero x per avere valori comrpesi tra -x e x
	'''
	A = (2*np.random.random((n,n)) - 1)*10
	xsol = np.ones(n)
	b = np.dot(A,xsol)

	#applicazione M.E.G.
	U,c = elim_Gauss_func(A,b)

	#risolvo il nuovo sistema con la routine di python
	x = np.linalg.solve(U,c)

	#calcolo errore sulla soluzione
	errore_assoluto = np.linalg.norm(xsol-x)
	errore_relativo = errore_assoluto/np.linalg.norm(xsol)

	print("Soluzione attesa xsol = ", xsol)
	print("\nSoluzione calcolata x = ", x)
	print("\nErrori calcolati sulla soluzione:")
	print("\tErrore assoluto = %e" % errore_assoluto)
	print("\tErrore relativo = %e" % errore_relativo)

'''
==================================================================
ROUTINE DI TEST PER ALGORITMI DI SOSTITUZIONE IN AVANTI

Breve descrizione:
Questa routine può testare qualsiasi algoritmo che implementi
l'algoritmo di sostituzione in avanti per la risoluzione di sistemi di 
equazioni lineari che hanno una matrice triangolare inferiore come matrice
dei coefficienti.
La funzione costruisce un sistema test il cui vettore delle soluzioni
è costituito da tutti 1.
Risolve il sistema con la funzione da testare passata come argomento.
Calcola l'errore assoluto e relativo sulla soluzione ottenuta,
confrontandola con la soluzione attesa.
==================================================================
------------------------INPUT---------------------------
Parametri:
	- dim : dimensione che dovranno avere la matrice dei coefficienti,
			il vettore dei termini noti e il vettore delle soluzioni.
	- sost_avanti_func : algoritmo di sostituzione in avanti da testare
---------------------------------------------------------
'''
def test_sostituzione_avanti(dim, sost_avanti_func):
	#costruzione del test
	n = dim
	A = (2*np.random.random((n,n))-1)*10 
	A = np.tril(A)
	xsol = np.ones(n)
	b = np.dot(A,xsol)

	#calcolo la soluzione del sistema tramite l'algoritmo da testare
	x = sost_avanti_func(A,b)

	#calcolo l'errore sulla soluzione calcolata
	errore_assoluto = np.linalg.norm(xsol-x)
	errore_relativo = errore_assoluto/np.linalg.norm(xsol)

	print("Soluzione attesa xsol = ", xsol)
	print("\nSoluzione calcolata x = ", x)
	print("\nErrori calcolati:")
	print("\tErrore assoluto = %e" % errore_assoluto)
	print("\tErrore relativo = %e" % errore_relativo)

'''
==================================================================
ROUTINE DI TEST PER ALGORITMI DI SOSTITUZIONE ALL'INDIETRO

Breve descrizione:
Questa routine può testare qualsiasi algoritmo che implementi
l'algoritmo di sostituzione in avanti per la risoluzione di sistemi di 
equazioni lineari che hanno una matrice triangolare inferiore come matrice
dei coefficienti.
La funzione costruisce un sistema test il cui vettore delle soluzioni
è costituito da tutti 1.
Risolve il sistema con la funzione da testare passata come argomento.
Calcola l'errore assoluto e relativo sulla soluzione ottenuta,
confrontandola con la soluzione attesa.
==================================================================
------------------------INPUT---------------------------
Parametri:
	- dim : dimensione che dovranno avere la matrice dei coefficienti,
			il vettore dei termini noti e il vettore delle soluzioni.
	- sost_indietro_func : algoritmo sostituzione all'indietro da testare
---------------------------------------------------------
'''
def test_sostituzione_indietro(dim, sost_indietro_func):
	#costruzione del test
	n = dim
	A = (2*np.random.random((n,n))-1)*10 
	A = np.triu(A)
	xsol = np.ones(n)
	b = np.dot(A,xsol)

	#calcolo la soluzione del sistema tramite l'algoritmo da testare
	x = sost_indietro_func(A,b)

	#calcolo l'errore sulla soluzione calcolata
	errore_assoluto = np.linalg.norm(xsol-x)
	errore_relativo = errore_assoluto/np.linalg.norm(xsol)

	print("Soluzione attesa xsol = ", xsol)
	print("\nSoluzione calcolata x = ", x)
	print("\nErrori calcolati:")
	print("\tErrore assoluto = %e" % errore_assoluto)
	print("\tErrore relativo = %e" % errore_relativo)

'''
==================================================================
ROUTINE DI TEST PER LA RISOLUZIONE DI SISTEMI DI EQUAZIONI LINEARI
APPLICANDO ROUTINE PERSONALI DI ELIMINAZIONE DI GAUSS E SOSTITUZIONE 
ALL'INDIETRO 

Breve descrizione:
La funzione costruisce un sistema test il cui vettore delle soluzioni
è costituito da tutti 1.
Applica l'algoritmo del M.E.G. passato come parametro.
Risolve il sistema con l'algoritmo di sostituzione all'indietro
passato come argomento.
Calcola l'errore assoluto e relativo sulla soluzione ottenuta,
confrontandola con la soluzione attesa.
==================================================================
------------------------INPUT---------------------------
Parametri:
	- dim : dimensione che dovranno avere la matrice dei coefficienti,
			il vettore dei termini noti e il vettore delle soluzioni.
	- elim_Gauss_func : algoritmo del metodo di gauss da testare (con o senza pivoting)
	- sost_ind_func : algoritmo sostituzione all'indietro da testare
---------------------------------------------------------
'''
def test_Gauss_sost_ind(dim, elim_Gauss_func, sost_ind_func):
	#costruzione del problema test
	n = dim
	A = (2*np.random.random((n,n)) - 1)*10
	xsol = np.ones(n)
	b = np.dot(A,xsol)

	#applicazione M.E.G.
	U,c = elim_Gauss_func(A,b)

	#risolvo il nuovo sistema con la funzione passata come parametro
	x = sost_ind_func(U,c)

	#calcolo errore sulla soluzione
	errore_assoluto = np.linalg.norm(xsol-x)
	errore_relativo = errore_assoluto/np.linalg.norm(xsol)

	print("Soluzione attesa xsol = ", xsol)
	print("\nSoluzione calcolata x = ", x)
	print("\nErrori calcolati sulla soluzione:")
	print("\tErrore assoluto = %e" % errore_assoluto)
	print("\tErrore relativo = %e" % errore_relativo)

'''
==================================================================
ROUTINE DI TEST PER ALGORITMI DI FATTORIZZAZIONE A = LU SENZA PIVOTING

Breve descrizione:
Questa routine può testare qualsiasi algoritmo che implementi
l'algoritmo della fattorizzazione A = LU senza pivoting.
La funzione costruisce un sistema test il cui vettore delle soluzioni
è costituito da tutti 1.
Applica la fattorizzazione A = LU sulla matrice di test.
Risolve il sistema con la routine np.linalg.solve().
Calcola l'errore assoluto e relativo sulla soluzione ottenuta,
confrontandola con la soluzione attesa.
==================================================================
------------------------INPUT---------------------------
Parametri:
	- dim : dimensione che dovranno avere la matrice dei coefficienti,
			il vettore dei termini noti e il vettore delle soluzioni.
	- fatt_LU_func : algoritmo di fattorizzazione A = LU senza pivoting da testare
---------------------------------------------------------
'''
def test_fatt_LU(dim, fatt_LU_func):
	#costruzione del test
	n = dim
	A = (2*np.random.random((n,n))-1)*10 
	xsol = np.ones(n)
	b = np.dot(A,xsol)

	#applico la fattorizzazione
	L,U = fatt_LU_func(A)

	#risolvo i due sistemi
	y = np.linalg.solve(L, b)
	x = np.linalg.solve(U, y)

	#calcolo l'errore sulla soluzione calcolata
	errore_assoluto = np.linalg.norm(xsol-x)
	errore_relativo = errore_assoluto/np.linalg.norm(xsol)

	print("Soluzione attesa xsol = ", xsol)
	print("\nSoluzione calcolata x = ", x)
	print("\nErrori calcolati:")
	print("\tErrore assoluto = %e" % errore_assoluto)
	print("\tErrore relativo = %e" % errore_relativo)

'''
==================================================================
ROUTINE DI TEST PER ALGORITMI DI FATTORIZZAZIONE A = LU CON PIVOTING

Breve descrizione:
Questa routine può testare qualsiasi algoritmo che implementi
l'algoritmo della fattorizzazione A = LU con pivoting
La funzione costruisce un sistema test il cui vettore delle soluzioni
è costituito da tutti 1.
Applica la fattorizzazione A = LU sulla matrice di test.
Risolve il sistema con la routine np.linalg.solve().
Calcola l'errore assoluto e relativo sulla soluzione ottenuta,
confrontandola con la soluzione attesa.
==================================================================
------------------------INPUT---------------------------
Parametri:
	- dim : dimensione che dovranno avere la matrice dei coefficienti,
			il vettore dei termini noti e il vettore delle soluzioni.
	- fatt_LU_func : algoritmo di fattorizzazione A = LU con pivoting da testare
---------------------------------------------------------
'''
def test_fatt_LU_pivoting(dim, fatt_LU_func):
	#costruzione del test
	n = dim
	A = (2*np.random.random((n,n))-1)*10 
	xsol = np.ones(n)
	b = np.dot(A,xsol)

	#applico la fattorizzazione
	L,U, indice = fatt_LU_func(A)

	#scambio le righe di b secondo li scambi fatti nella fattorizzazione
	b = b[indice]

	#risolvo i due sistemi
	y = np.linalg.solve(L, b)
	x = np.linalg.solve(U, y)

	#calcolo l'errore sulla soluzione calcolata
	errore_assoluto = np.linalg.norm(xsol-x)
	errore_relativo = errore_assoluto/np.linalg.norm(xsol)

	print("Soluzione attesa xsol = ", xsol)
	print("\nSoluzione calcolata x = ", x)
	print("\nErrori calcolati:")
	print("\tErrore assoluto = %e" % errore_assoluto)
	print("\tErrore relativo = %e" % errore_relativo)

'''
==================================================================
ROUTINE DI TEST PER LA RISOLUZIONE DI SISTEMI DI EQUAZIONI LINEARI
APPLICANDO ROUTINE PERSONALI DI FATTORIZZAZIONE A = LU senza pivoting
E ALGORITMI DI SOSTITUZIONE AVANTI E INDIETRO

Breve descrizione:
La funzione costruisce un sistema test il cui vettore delle soluzioni
è costituito da tutti 1.
Applica l'algoritmo di fattorizzazione A = LU senza pivoting
passato come parametro.
Risolve i sistemi con gli algoritmi di sostituzione passati come argomento.
Calcola l'errore assoluto e relativo sulla soluzione ottenuta,
confrontandola con la soluzione attesa.
==================================================================
------------------------INPUT---------------------------
Parametri:
	- dim : dimensione che dovranno avere la matrice dei coefficienti,
			il vettore dei termini noti e il vettore delle soluzioni.
	- fatt_LU_func : algoritmo di fattorizzazione A = LU senza pivoting da testare
	- sost_avanti_func : algoritmo sostituzione in avanti da testare
	- sost_indietro_func : algoritmo sostituzione all'indietro da testare
---------------------------------------------------------
'''
def test_fatt_LU_alg_sost(dim, fatt_LU_func, sost_avanti_func, sost_indietro_func):
	#costruzione del test
	n = dim
	A = (2*np.random.random((n,n))-1)*10 
	xsol = np.ones(n)
	b = np.dot(A,xsol)

	#applico la fattorizzazione
	L,U = fatt_LU_func(A)

	#risolvo i due sistemi
	y = sost_avanti_func(L, b)
	x = sost_indietro_func(U, y)

	#calcolo l'errore sulla soluzione calcolata
	errore_assoluto = np.linalg.norm(xsol-x)
	errore_relativo = errore_assoluto/np.linalg.norm(xsol)

	print("Soluzione attesa xsol = ", xsol)
	print("\nSoluzione calcolata x = ", x)
	print("\nErrori calcolati:")
	print("\tErrore assoluto = %e" % errore_assoluto)
	print("\tErrore relativo = %e" % errore_relativo)

'''
==================================================================
ROUTINE DI TEST PER LA RISOLUZIONE DI SISTEMI DI EQUAZIONI LINEARI
APPLICANDO ROUTINE PERSONALI DI FATTORIZZAZIONE A = LU con pivoting 
E ALGORITMI DI SOSTITUZIONE AVANTI E INDIETRO

Breve descrizione:
La funzione costruisce un sistema test il cui vettore delle soluzioni
è costituito da tutti 1.
Applica l'algoritmo di fattorizzazione A = LU senza pivoting
passato come parametro.
Risolve i sistemi con gli algoritmi di sostituzione passati come argomento.
Calcola l'errore assoluto e relativo sulla soluzione ottenuta,
confrontandola con la soluzione attesa.
==================================================================
------------------------INPUT---------------------------
Parametri:
	- dim : dimensione che dovranno avere la matrice dei coefficienti,
			il vettore dei termini noti e il vettore delle soluzioni.
	- fatt_LU_pivot_func : algoritmo di fattorizzazione A = LU con pivoting da testare
	- sost_avanti_func : algoritmo sostituzione in avanti da testare
	- sost_indietro_func : algoritmo sostituzione all'indietro da testare
---------------------------------------------------------
'''
def test_fatt_LU_pivoting_alg_sost(dim, fatt_LU_pivot_func, sost_avanti_func, sost_indietro_func):
	#costruzione del test
	n = dim
	A = (2*np.random.random((n,n))-1)*10 
	xsol = np.ones(n)
	b = np.dot(A,xsol)

	#applico la fattorizzazione
	L,U, indice = fatt_LU_pivot_func(A)

	#scambio le righe di b secondo gli scambi fatti nella fattorizzazione 
	b = b[indice]

	#risolvo i due sistemi
	y = sost_avanti_func(L, b)
	x = sost_indietro_func(U, y)

	#calcolo l'errore sulla soluzione calcolata
	errore_assoluto = np.linalg.norm(xsol-x)
	errore_relativo = errore_assoluto/np.linalg.norm(xsol)

	print("Soluzione attesa xsol = ", xsol)
	print("\nSoluzione calcolata x = ", x)
	print("\nErrori calcolati:")
	print("\tErrore assoluto = %e" % errore_assoluto)
	print("\tErrore relativo = %e" % errore_relativo)

'''
==================================================================
ROUTINE DI TEST PER IL CONFRONTO DELLE PERFORMANCE TRA LE ROUTINE
DI FATTORIZZAZIONE A=LU, SENZA PIVOTING, non OTTIMIZZATA E OTTIMIZZATA

Breve descrizione:
La funzione costruisce un sistema test il cui vettore delle soluzioni
è costituito da tutti 1.
Applica l'algoritmo di fattorizzazione A = LU senza pivoting NON ottimizzato
passato come parametro, calcolando il tempo di computazione.
Fa la stessa cosa con la versione ottimizzata.
Stampa i tempi riscontrati.
==================================================================
------------------------INPUT---------------------------
Parametri:
	- dim : dimensione che dovranno avere la matrice dei coefficienti,
			il vettore dei termini noti e il vettore delle soluzioni.
	- fatt_LU_func : algoritmo di fattorizzazione A = LU senza pivoting
	- fatt_LU_func_ottim : algoritmo di fattorizzazione A = LU senza pivoting ottimizzato
---------------------------------------------------------
'''
def test_performance_fatt_LU(dim, fatt_LU_func, fatt_LU_func_ottim):
	#costruzione del test
	n = dim
	A = (2*np.random.random((n,n))-1)*10 
	xsol = np.ones(n)
	b = np.dot(A,xsol)

	tempo_iniziale = time.time()
	L,U = fatt_LU_func(A)
	tempo_finale = time.time()

	#calcolo del tempo fattorizzazione normale
	tempo_fatt_normale = tempo_finale - tempo_iniziale
	print("Tempo fattorizzazione LU non ottimizzata = %f" % tempo_fatt_normale)

	tempo_iniziale = time.time()
	L,U = fatt_LU_func_ottim(A)
	tempo_finale = time.time()

	#calcolo del tempo fattorizzazione normale
	tempo_fatt_ottim = tempo_finale - tempo_iniziale
	print("Tempo fattorizzazione LU ottimizzata = %f" % tempo_fatt_ottim)

'''
==================================================================
ROUTINE DI TEST PER IL CONFRONTO DELLE PERFORMANCE TRA LE ROUTINE
DI FATTORIZZAZIONE A=LU, CON PIVOTING, non OTTIMIZZATA E OTTIMIZZATA

Breve descrizione:
La funzione costruisce un sistema test il cui vettore delle soluzioni
è costituito da tutti 1.
Applica l'algoritmo di fattorizzazione A = LU con pivoting NON ottimizzato
passato come parametro, calcolando il tempo di computazione.
Fa la stessa cosa con la versione ottimizzata.
Stampa i tempi riscontrati.
==================================================================
------------------------INPUT---------------------------
Parametri:
	- dim : dimensione che dovranno avere la matrice dei coefficienti,
			il vettore dei termini noti e il vettore delle soluzioni.
	- fatt_LU_func : algoritmo di fattorizzazione A = LU con pivoting
	- fatt_LU_func_ottim : algoritmo di fattorizzazione A = LU con pivoting ottimizzato
---------------------------------------------------------
'''
def test_performance_fatt_LU_pivoting(dim, fatt_LU_func, fatt_LU_func_ottim):
	#costruzione del test
	n = dim
	A = (2*np.random.random((n,n))-1)*10 
	xsol = np.ones(n)
	b = np.dot(A,xsol)

	tempo_iniziale = time.time()
	L,U,indice = fatt_LU_func(A)
	tempo_finale = time.time()

	#calcolo del tempo fattorizzazione normale
	tempo_fatt_normale = tempo_finale - tempo_iniziale
	print("Tempo fattorizzazione LU non ottimizzata = %f" % tempo_fatt_normale)

	tempo_iniziale = time.time()
	L,U,indice = fatt_LU_func_ottim(A)
	tempo_finale = time.time()

	#calcolo del tempo fattorizzazione normale
	tempo_fatt_ottim = tempo_finale - tempo_iniziale
	print("Tempo fattorizzazione LU ottimizzata = %f" % tempo_fatt_ottim)


'''
==================================================================
ROUTINE DI TEST PER ALGORITMI DI CALCOLO DELLA MATRICE INVERSA

Breve descrizione:
La routine costruisce una matrice quadrata A di dimensione indicata
dall'utente.
Applica l'algoritmo del calcolo della matrice inversa ed effettua
il prodotto tra la matrice A e la matrice inversa calcolata.
Calcola quanto il prodotto calcolato è distante dalla matrice identità
in termini di errore assoluto e errore relativo.
==================================================================
------------------------INPUT---------------------------
Parametri:
	- dim : dimensione che dovranno avere la matrice di test,
			la matrice inversa da calcolare e la matrice identità.
	- inversa_func : funzione per il calcolo dell'inversa da testare;
---------------------------------------------------------
'''
def test_matrice_inversa(dim, inversa_func):
	n = dim
	A = (2*np.random.random((n,n))-1)*10

	X = inversa_func(A)
	
	#costruisco la matrice identità
	I = np.eye(n,n)

	#calcolo la matrice identità tramite A e X
	I2 = np.dot(A,X)

	#calcolo gli errori sulla matrice identità ottenuta
	errore_assoluto = np.linalg.norm(I-I2)
	errore_relativo = errore_assoluto/np.linalg.norm(I)
	print("I = ", I)
	print("\nI2 = ", I2)
	print("\nErrore assoluto: %e" % errore_assoluto)
	print("Errore relativo: %e" % errore_relativo)

def test_metodo_iterativo(dim, metodo_iter_func, x0, accuratezza, kmax):
	if dim != len(x0):
		print("ERRORE: la dimensione di x0 deve essere uguale al valore del parametro dim.")
	else:
		n = dim

		A = (2*np.random.random((n,n))-1)*3
		xsol = np.ones(n)
		b = np.dot(A,xsol)

		#applico il metodo iterativo
		x = metodo_iter_func(A, b, x0, accuratezza, kmax)

		#calcolo la distanza tra la soluzione ottenuta e quella attesa
		errore_assoluto = np.linalg.norm(xsol-x)
		errore_relativo = errore_assoluto/np.linalg.norm(xsol)

		print("Soluzione attesa xsol = ", xsol)
		print("\nSoluzione calcolata x = ", x)
		print("\nErrori calcolati:")
		print("\tErrore assoluto = %e" % errore_assoluto)
		print("\tErrore relativo = %e" % errore_relativo)

if __name__ == "__main__":
	
	A = (2*np.random.random((30,30)) - 1)*10
	L = np.tril(A, -1)
	U = np.triu(A, +1)
	D = np.diag(np.diag(A)) 

	N = np.array(-(L+U))

	#verifico che M non sia singolare
	if np.prod(np.diag(A)) < 1.0e-14:
		print("M potrebbe essere singolare")
		sys.exit()
	else:
		print("M non è singolare")

	#verifico la convergenza del metodo iterativo
	#M_inversa = al.matrice_inversa(D)
	M_inversa = np.linalg.inv(D)
	

	norma_P = np.linalg.norm(np.dot(M_inversa,N))
	print("||P|| = ", norma_P)
	if  norma_P < 1:
		print("Il metodo converge")
	else:
		print("Il metodo non converge")
	'''
	n = 5
	x_iniziale = np.repeat(-5., n)
	test_metodo_iterativo(n, al.metodo_iterativo_jacobi, x_iniziale, 0.05, 200)
	'''
