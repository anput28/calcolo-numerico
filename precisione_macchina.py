from math import log2, log10

#determino l'epsilon machine
u = 1
while 1+u > 1:
    u_temp = u
    u = u/2

epsilon_machine = u_temp
print("L'epsilon machine vale: %e" % epsilon_machine)

#calcolo la precisione del calcolatore
p = -log2(epsilon_machine)
print("La precisione del calcolatore vale %f senza il bit nascosto." % p)

#calcolo il numero di cifre significative in base 10
q = p*log10(2)
print("Il numero di cifre significative in base 10 è: %f" % q)

