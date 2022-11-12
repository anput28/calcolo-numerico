import numpy as np

def isSingolare(matrice):
	ok = False
	righe = matrice.shape[0]
	colonne = matrice.shape[1]

	for i in range(righe):
		for j in range(colonne):
			if i == j:
				if matrice[i,j] == 0:
					ok = True
					break

	return ok

def algoritmo_sostituzione_indietro(matrice_coeff, array_noti):
	#creo il vettore delle soluzioni vuoto
	dim = len(matrice_coeff)
	x = np.empty(dim)

	'''
	il for principale va dall'ultima riga fino alla prima riga,
	nella realtà va da n a 1 ma nel calcolatore gli array partono da 0
	quindi deve andare da n-1 a 0.
	Il terzo parametro della funzione range permette di iterare al contrario,
	ma per esempio range(4,1, -1) itera nel seguente modo: 4,3,2, cioè si ferma
	al numero appena più grande del numero indicato nel secondo parametro, quindi
	per considerare anche l'indice 0 indico come secondo parametro -1
	'''
	for i in range(dim-1, -1, -1):
		somma = 0

		'''
		il for si deve fermare quando si raggiunge l'indice n-1 quindi scrivo
		for j in range(i+1, n) che è uguale a dire for(j=i+1; j<n; j++)
		'''
		for j in range(i+1, dim):
			somma += (matrice_coeff[i,j]*x[j])
		x[i] = (array_noti[i] - somma)/matrice_coeff[i,i]

	return x


#-------------------------costruzione di un problema test--------------------------
#dimensione della matrice 
n = 3

'''
#A = np.random.random((n,n) crea una matrice n*n con numeri casuali da 0 a 1,
mentre la seguente istruzione costruisce una matrice con numeri reali casuali tra -10 e 10
'''

A = (2*np.random.random((n,n))-1)*10 
print("A prima della trasformazione A =\n"+str(A)+"\n")

'''
mette a 0 tutti gli elementi della matrice A che stanno sotto la diagonale, 
cioè costruisce una matrice triangolare superiore
'''
A = np.triu(A) 
print("A dopo della trasformazione A =\n"+str(A)+"\n")

#verifico se la matrice A è singolare, se è così il sistema non ha soluzioni
if isSingolare(A):
	print("Il sistema non ha soluzione")
else:
	#crea il vettore soluzione fatto di tutti 1
	#xsol = np.ones((n,1))

	#creo il vettore soluzione fatto con numeri random tra -10 e 10 
	xsol = (2*np.random.random((n))-1)*10 

	'''
	fa la moltiplicazione tra due array, incluse le matrici, cioè può fare:
		-prodotto tra vettori;
		-prodotto tra matrici;
		-prodotto tra vettori e matrici;
		-prodotto tra scalari e vettori;
		-prodotto tra scalari e matrici;
	Nel rispetto delle regole aritmetiche
	'''
	b = np.dot(A, xsol)
	print("b = \n"+str(b))

	#risolvo il sistema Ax=b tramite numpy
	x = algoritmo_sostituzione_indietro(A,b)
	ErrAss = np.linalg.norm(xsol-x)
	ErrRel = ErrAss/np.linalg.norm(xsol)

	print("\n\n\n\nSoluzione del sistema calcolata x = "+str(x))
	print("Soluzione del sistema attesa x-sol =\n"+str(xsol)+"\n")
	print('Alg. sost. indietro con matrice %d x %d' %(n,n))
	print("Errore assoluto = %e " % ErrAss)
	print("Errore relativo = %e " % ErrRel)

