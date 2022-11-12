from random import uniform

#crea un dizionario con i dati che formano l'aritmetica di un calcolatore
def aritmetica(base, cifre_mantissa, min_car, max_car):
    aritmetica = {
        "base" : base,
        "cifre_mantissa" : cifre_mantissa,
        "min_car" : min_car,
        "max_car" : max_car
    }
    return aritmetica

#verifica se un numero è normalizzato
def isNormalizzato(numero):
    risposta = False
    
    num_string = str(numero)
    numero_diviso = num_string.split('.')
    parte_intera = numero_diviso[0]
    mantissa = numero_diviso[1]
    
    if int(parte_intera) == 0:
        if int(mantissa[0]) != 0:
            risposta = True
          
    return risposta

#funzione che restituisce la parte intera di un numero in floating point
def getParteIntera(numero):
    parte_intera = None
    
    if isinstance(numero, float) or isinstance(numero, int):     
        num_string = str(numero)
        numero_diviso = num_string.split('.')
        parte_intera = numero_diviso[0]
    else:
        raise TypeError("L'argomento deve essere un numero intero o decimale")
        
    return int(parte_intera)

#funzione che restituisce la mantissa di un numero sottoforma di stringa
def getMantissa(numero):
    mantissa = None
    
    if isinstance(numero, float):     
        num_string = str(numero)
        numero_diviso = num_string.split('.')
        mantissa = numero_diviso[1]
    else:
        raise TypeError("L'argomento deve essere un numero decimale")
        
    return mantissa

#funzione che normalizza un numero
def normalizzazione(n):
    if isNormalizzato(n):
        return n
    else:
        caratteristica = 0
        parte_intera = getParteIntera(n)
    
        if parte_intera > 0:
            while parte_intera != 0:
                n = n/10
                caratteristica += 1
        
        elif parte_intera == 0:
            mantissa = getMantissa(n)
            while int(mantissa[0]) == 0:
                n = n*10
                caratteristica -= 1
    return n, caratteristica
    
def chopping(numero, cifre_mantissa):
    numero_intero = getParteIntera(numero)
    numero_mantissa = getMantissa(numero)
    
    #tronco il numero al numero massimo di cifre della mantissa
    chop = ''
    for i in range(cifre_mantissa):
        chop += numero_mantissa[i]

    numero_macchina = str(numero_intero) + '.' + chop
    return float(numero_macchina)


#costruzione dell'aritmetica del calcolatore
base = int(input("Inserire la base dell'aritmetica: "))
cifre_mantissa = int(input("Inserire il massimo numero di cifre per rappresentare la mantissa: "))
min_car = int(input("Inserire l'estremo minore della caratteristica: "))
max_car = int(input("Inserire l'estremo maggiore della caratteristica: "))

F = aritmetica(base, cifre_mantissa, min_car, max_car)


#genero un numero random
real_min_F = F["base"]**(-F["min_car"]) #minimo numero rappresentabile in F
real_max_F = (F["base"] - F["base"]**(-F["cifre_mantissa"]))*(F["base"]**F["max_car"])

n = uniform(real_min_F*2, real_max_F*2)
print("numero da verificare: ", n)

#normalizzo il numero
n, caratteristica = normalizzazione(n)
if caratteristica > F["max_car"] or caratteristica < F["min_car"]:
    print("Il numero non è rappresentabile nel calcolatore")
else:
    #chopping del numero
    chop_n = chopping(n, F["cifre_mantissa"])
    
    print("numero esatto: %f" % n)
    print("chop(n): %f", chop_n)
    
    #calcolo errore
