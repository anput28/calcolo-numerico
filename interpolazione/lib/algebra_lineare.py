'''
======================================================
@author Angelo Putignano

@file test_algebra_lineare.py
@version 0.1
======================================================



==================================================================
Libreria che contiene funzioni che riguardano l'algebra lineare

indice libreria:
	- Metodo di eliminazione di Gauss (senza pivoting)
	- Metodo di eliminazione di Gauss (con pivoting)
	- Algoritmo di sostituzione di avanti
	- Algoritmo di sostituzione di indietro
	- Fattorizzazione A = LU (senza pivoting)
	- Fattorizzazione A = LU (con pivoting)
	- Matrice inversa
	- Risoluzione di un sistema di equazioni lineari
===================================================================
'''

import numpy as np


class MatrixDimensionsError(Exception):
	pass

'''
==========================================================
METODO DI ELIMINAZIONE DI GAUSS SENZA PIVOTING
==========================================================
------------------------------INPUT------------------------------
Parametri:
	- A : matrice dei coefficienti
	- b : vettore dei termini noti

Prerequisiti:
	- dim(A) = nxn e dim(b) = m, con n = m
	- A e b devono essere formati da dati in floating point
-----------------------------------------------------------------

------------------------------OUTPUT------------------------------
Parametri:
	- U : matrice triangolare superiore
	- c : nuovo vettore dei termini noti
	
	Se si verificano degli errori vengono restituiti 
	i parametri di input
-----------------------------------------------------------------
'''

def elim_Gauss(A,b):
	np.seterr(all='raise')

	U = np.copy(A)
	c = np.copy(b)

	if len(U) != len(c):
		print("ERRORE: il vettore dei termini noti e la matrice dei coefficienti hanno dimensioni diverse.")
		return A,b 
	else:
		n = len(U)
		for j in range(0, n-1):
			for i in range(j+1, n):
				try:
					m = U[i,j]/U[j,j]
					U[i,j] = 0
					for k in range(j+1, n):
						U[i,k] = U[i,k] - m*U[j,k]
					c[i] = c[i] - m*c[j]
				except ZeroDivisionError:
					print("ERRORE: è stata riscontrata una divisione per zero provocata dall'elemento A[%d, %d]." % (j,j))
					return A,b
				except FloatingPointError:
					print("ERRORE: impossibile applicare il M.E.G agli input ricevuti.")
					return A,b
	return U, c

'''
==========================================================
METODO DI ELIMINAZIONE DI GAUSS CON PIVOTING
==========================================================
------------------------------INPUT------------------------------
Parametri:
	- A : matrice dei coefficienti
	- b : vettore dei termini noti

Prerequisiti:
	- dim(A) = nxn e dim(b) = m, con n = m
	- A e b devono essere formati da dati in floating point
-----------------------------------------------------------------

------------------------------OUTPUT------------------------------
Parametri:
	- U : matrice triangolare superiore
	- c : nuovo vettore dei termini noti
	
	Se si verificano degli errori vengono restituiti 
	i parametri di input
-----------------------------------------------------------------
'''
def elim_Gauss_pivoting(A,b):
	np.seterr(all='raise')

	U = np.copy(A)
	c = np.copy(b)

	if len(U) != len(c):
		print("ERRORE: il vettore dei termini noti e la matrice dei coefficienti hanno dimensioni diverse.")
		return A,b 
	else:
		n = len(U)
		for j in range(0, n-1):
			#individuazione elemento pivot
			pivot = abs(U[j,j])
			i_pivot = j
			for i in range(j+1, n):
				if U[i,j] > pivot:
					pivot = U[i,j]
					i_pivot = i

			#eventuale scambio di riga
			if i_pivot > j:
				for k in range(j, n):
					temp = U[j,k]
					U[j,k] = U[i_pivot, k]
					U[i_pivot, k] = temp
				c_temp = c[j]
				c[j] = c[i_pivot]
				c[i_pivot] = c_temp

			#M.E.G
			for i in range(j+1, n):
				try:
					m = U[i,j]/U[j,j]
					U[i,j] = 0
					for k in range(j+1, n):
						U[i,k] = U[i,k] - m*U[j,k]
					c[i] = c[i] - m*c[j]
				except ZeroDivisionError:
					print("ERRORE: è stata riscontrata una divisione per zero provocata dall'elemento A[%d, %d]." % (j,j))
					return A,b
				except FloatingPointError:
					print("ERRORE: impossibile applicare il M.E.G agli input ricevuti.")
					return A,b
	return U,c


'''
==========================================================
ALGORITMO DI SOSTITUZIONE IN AVANTI
==========================================================
------------------------INPUT---------------------------
Parametri:
	- A : matrice dei coefficienti triangolare inferiore
	- b : vettore dei termini noti

Prerequisiti:
	- A deve essere non singolare
	- dim(A) = nxn e dim(b) = n
	- A e b devono essere formati da dati in floating point
---------------------------------------------------------

-----------------------OUTPUT----------------------------
Parametri:
	- x : vettore delle soluzioni
--------------------------------------------------------
'''
def sostituzione_avanti(A,b):

	if len(A) != len(b):
		print("ERRORE: il vettore dei termini noti e la matrice dei coefficienti hanno dimensioni diverse.")
	elif abs(np.prod(np.diag(A))) < 1.0e-14:
		print("ERRORE: la matrice probabilmente è singolare.")
	else:
		n = len(A)
		x = np.zeros(n)

		x[0] = b[0]/A[0,0]
		for i in range(1, n):
			somma = 0
			for j in range(0, i):
				somma = somma + A[i,j]*x[j]

			x[i] = (b[i] - somma)/A[i,i]
	return x


'''
==========================================================
ALGORITMO DI SOSTITUZIONE ALL'INDIETRO
==========================================================
------------------------INPUT---------------------------
Parametri:
	- A : matrice dei coefficienti triangolare superiore
	- b : vettore dei termini noti

Prerequisiti:
	- A deve essere non singolare
	- dim(A) = nxn e dim(b) = n
	- A e b devono essere formati da dati in floating point
---------------------------------------------------------

-----------------------OUTPUT----------------------------
Parametri:
	- x : vettore delle soluzioni
--------------------------------------------------------
'''
def sostituzione_indietro(A,b):

	if len(A) != len(b):
		print("ERRORE: il vettore dei termini noti e la matrice dei coefficienti hanno dimensioni diverse.")
	elif abs(np.prod(np.diag(A))) < 1.0e-14:
		print("ERRORE: la matrice probabilmente è singolare.")
	else:
		n = len(A)
		x = np.zeros(n)
		
		x[n-1] = b[n-1]/A[n-1,n-1]
		for i in range(n-2, -1, -1):
			somma = 0
			for j in range(i+1, n):
				somma = somma + A[i,j]*x[j]
			x[i] = (b[i] - somma)/A[i,i]
	return x


'''
==========================================================
FATTORIZZAZIONE A = LU SENZA PIVOTING 
==========================================================
------------------------INPUT---------------------------
Parametri:
	- A : matrice dei coefficienti

Prerequisiti:
	- A deve essere formata da dati in floating point
---------------------------------------------------------

-----------------------OUTPUT----------------------------
Parametri:
	- U : matrice triangolare superiore
	- L : matrice triangolare inferiore

	Se si verificano errori vengono restituite due
	matrici vuote
--------------------------------------------------------
'''
def fatt_LU(A):
	np.seterr(all='raise')
	
	A = np.copy(A)
	n = len(A)

	for j in range(n-1):
		for i in range(j+1, n):
			try:
				A[i,j] = A[i,j]/A[j,j]
				for k in range(j+1, n):
					A[i,k] = A[i,k] - A[i,j]*A[j,k]
			except FloatingPointError:
				print("ERRORE: impossibile applicare la fattorizzazione A = LU alla matrice di input.")
				U = np.empty(n)
				L = np.empty(n)
	U = np.triu(A)
	L = np.tril(A, -1) + np.eye(n,n)

	return L,U


'''
==========================================================
FATTORIZZAZIONE A = LU SENZA PIVOTING OTTIMIZZATA
==========================================================
------------------------INPUT---------------------------
Parametri:
	- A : matrice dei coefficienti

Prerequisiti:
	- A deve essere formata da dati in floating point
---------------------------------------------------------

-----------------------OUTPUT----------------------------
Parametri:
	- U : matrice triangolare superiore
	- L : matrice triangolare inferiore

	Se si verificano errori vengono restituite due
	matrici vuote
--------------------------------------------------------
'''
def fatt_LU_ottim(A):
	np.seterr(all='raise')
	
	A = np.copy(A)
	n = len(A)

	for j in range(n-1):
		for i in range(j+1, n):
			try:
				A[i,j] = A[i,j]/A[j,j]
				A[i, j+1:n] = A[i, j+1:n] - A[i,j]*A[j, j+1:n]
			except FloatingPointError:
				print("ERRORE: impossibile applicare la fattorizzazione A = LU alla matrice di input.")
				U = np.empty(n)
				L = np.empty(n)
	U = np.triu(A)
	L = np.tril(A, -1) + np.eye(n,n)

	return L,U

'''
==========================================================
FATTORIZZAZIONE A = LU CON PIVOTING
==========================================================
------------------------INPUT---------------------------
Parametri:
	- A : matrice dei coefficienti

Prerequisiti:
	- A deve essere formata da dati in floating point
---------------------------------------------------------

-----------------------OUTPUT----------------------------
Parametri:
	- U : matrice triangolare superiore
	- L : matrice triangolare inferiore
	- indice : vettore che registra gli scambi da faare sul vettore dei termini noti

	Se si verificano errori vengono restituite due
	matrici vuote
---------------------------------------------------------
'''
def fatt_LU_pivoting(A):
	np.seterr(all='raise')

	A = np.copy(A)
	n = len(A)
	indice = np.array(range(n))

	for j in range(n-1):
		#individuazione elemento pivot
		pivot = abs(A[j,j])
		i_pivot = j
		for i in range(j+1, n):
			if abs(A[i,j]) > pivot:
				pivot = abs(A[i,j])
				i_pivot = i

		#eventuale scambio di righe
		if i_pivot > j:
			for k in range(n):
				temp = A[i_pivot, k]
				A[i_pivot, k] = A[j, k]
				A[j, k] = temp
			i_temp = indice[j]
			indice[j] = indice[i_pivot]
			indice[i_pivot] = i_temp

		#fattorizzazione A = LU
		for i in range(j+1, n):
			try:
				A[i,j] = A[i,j]/A[j,j]
				for k in range(j+1, n):
					A[i,k] = A[i,k] - A[i,j]*A[j,k]
			except FloatingPointError:
				print("ERRORE: impossibile applicare la fattorizzazione A = LU alla matrice di input.")
				U = np.empty(n)
				L = np.empty(n)
	U = np.triu(A)
	L = np.tril(A, -1) + np.eye(n,n)

	return L,U,indice

'''
==========================================================
FATTORIZZAZIONE A = LU CON PIVOTING OTTIMIZZATA
==========================================================
------------------------INPUT---------------------------
Parametri:
	- A : matrice dei coefficienti

Prerequisiti:
	- A deve essere formata da dati in floating point
---------------------------------------------------------

-----------------------OUTPUT----------------------------
Parametri:
	- U : matrice triangolare superiore
	- L : matrice triangolare inferiore
	- indice : vettore che registra gli scambi da faare sul vettore dei termini noti

	Se si verificano errori vengono restituite due
	matrici vuote
---------------------------------------------------------
'''
def fatt_LU_pivoting_ottim(A):
	A = np.copy(A)
	n = len(A)
	indice = np.array(range(n))
	for j in range(n-1):
		#individuazione elemento pivot
		'''
		Spiegazione istruzione che segue:
			- abs(A[j:n, j]) considera tutti gli elemeti di A in valore assoluto
			  nella sola colonna j e nelle righe da j a n;
			- np.argmax() permette di prendere l'indice dell'elemento massimo;
			- sto trovando l'indice massimo solo sulle righe da j a n della colonna j,
			  quindi se l'elemento massimo si trova all'indice j, argmax darà 0 perchè j
			  è la prima riga che considero perciò devono sommare j;
		'''
		i_pivot = np.argmax(abs(A[j:n, j])) + j

		#eventuale scambio di righe
		if i_pivot > j:
			A[[i_pivot, j], :] = A[[j, i_pivot], :]
			indice[[i_pivot, j]] = indice[[j, i_pivot]]

		#fattorizzazione LU
		for i in range(j+1, n):
			A[i,j] = A[i,j]/A[j,j]
			A[i, j+1:n] = A[i, j+1:n] - A[i,j]*A[j, j+1:n]
	L = np.tril(A, -1) + np.eye(n,n)
	U = np.triu(A)
	return L, U, indice

'''
==========================================================
CALCOLO DELLA MATRICE INVERSA

Questo algoritmo utilizza una fattorizzazione A=LU senza pivoting
==========================================================
------------------------INPUT---------------------------
Parametri:
	- A : matrice quadrata

Prerequisiti:
	- A deve essere formata da dati in floating point
---------------------------------------------------------

-----------------------OUTPUT----------------------------
Parametri:
	- X : matrice inversa di A
---------------------------------------------------------
'''
def matrice_inversa(A):
	np.seterr(all='raise')

	if len(A.shape) != 2:
		raise MatrixDimensionsError()
	elif A.shape[0] != A.shape[1]:
		raise MatrixDimensionsError()
	else:
		A = np.copy(A)
		n = len(A)
		I = np.eye(n,n)

		#applico fattorizzazione A = LU 
		L,U = fatt_LU_ottim(A)

		X = np.empty((n,n))
		
		for j in range(n):
			y = sostituzione_avanti(L, I[:, j])
			X[:, j] = sostituzione_indietro(U, y)
	return X

'''
==========================================================
CALCOLO DELLA MATRICE INVERSA

Questo algoritmo utilizza una fattorizzazione A=LU con pivoting
==========================================================
------------------------INPUT---------------------------
Parametri:
	- A : matrice quadrata

Prerequisiti:
	- A deve essere formata da dati in floating point
---------------------------------------------------------

-----------------------OUTPUT----------------------------
Parametri:
	- X : matrice inversa di A
---------------------------------------------------------
'''
def matrice_inversa_pivoting(A):
	np.seterr(all='raise')

	if len(A.shape) != 2:
		raise MatrixDimensionsError()
	elif A.shape[0] != A.shape[1]:
		raise MatrixDimensionsError()
	else:
		A = np.copy(A)
		n = len(A)
		I = np.eye(n,n)

		#applico fattorizzazione A = LU 
		L,U,indice = fatt_LU_pivoting_ottim(A)

		#scambio le righe di I in base agli scambi della fattorizzazione
		I = I[indice]

		X = np.empty((n,n))
		
		for j in range(n):
			y = sostituzione_avanti(L, I[:, j])
			X[:, j] = sostituzione_indietro(U, y)
	return X

'''
==========================================================
RISOLUZIONE DI UN SISTEMA DI EQUAZIONI LINEARI

Questo algoritmo utilizza una fattorizzazione A=LU con pivoting
ottimizzata e poi usa gli algoritmi di sostituzione per trovare
la soluzione del sistema
==========================================================
------------------------INPUT---------------------------
Parametri:
	- A : matrice dei coefficienti
	- b : vettore dei termini noti

Prerequisiti:
	- A e b devono essere formati da dati in floating point
---------------------------------------------------------

-----------------------OUTPUT----------------------------
Parametri:
	- x : vettore delle soluzioni del sistema
---------------------------------------------------------
'''
def risoluzione_sistema(A,b):
	A = np.copy(A)
	b = np.copy(b)

	L, U, indice = fatt_LU_pivoting_ottim(A)
	b = b[indice]

	y = sostituzione_avanti(L, b)
	x = sostituzione_indietro(U, y)

	return x


def metodo_iterativo_jacobi(A, b, x0, accuratezza, kmax):
	A = np.copy(A)
	b = np.copy(b)
	n = len(A)

	#array dei termini noti del sistema Mx = c
	c = np.empty(n)

	#array delle soluzioni del sistema Mx = c
	x1 = np.empty(n)

	#contatore delle iterazioni
	k = 0
	stop = False
	while not(stop) and k < kmax:
		#metodo di Jacobi
		for i in range(n):
			c[i] = b[i]
			for j in range(n):
				if j != i:
					c[i] = c[i] - A[i,j]*x0[j]
			x1[i] = c[i]/A[i,i]
		residuo = b - np.dot(A, x1)
		criterio_residui = np.linalg.norm(residuo) < accuratezza*np.linalg.norm(b)
		criterio_sottrazioni = np.linalg.norm(x1-x0) < accuratezza*np.linalg.norm(x1)
		stop = (criterio_residui) and (criterio_sottrazioni)
		k += 1
		x0 = x1

	if not(stop):
		print("Attenzione: accuratezza %e non raggiunta in %d operazioni." % (accuratezza, kmax))

	return x1