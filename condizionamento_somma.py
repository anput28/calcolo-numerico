from random import random

#inserimento dati esatti 
x = float(input("Inserire dato x: "))
y = float(input("Inserire dato y: "))

#costruzione dati perturbati
x_pert = x + x*random()*1.0e-8
y_pert = y+ y*random()*1.0e-8

#calcolo la somma esatta e somma perturbata
s = x + y
s_pert = x_pert + y_pert
print("\nSomma sui dati esatti:\n%.20f + %.20f = %.20f" % (x, y, s))
print("Somma sui dati perturbati:\n%.20f + %.20f = %.20f" % (x_pert, y_pert, s_pert))

#calcolo degli errori relativi
err_x = abs(x-x_pert)/abs(x)
err_y = abs(y-y_pert)/abs(y)
err_s = abs(s-s_pert)/abs(s)

#calcolo i fattori di amplificazione della somma
ampl_x = abs(x)/abs(x+y)
ampl_y = abs(y)/abs(x+y)

#stampo i risultati
print("\n-------------Errori in input-------------")
print("Errore su x = %e" % err_x)
print("Errore su y = %e" % err_y)
print("\n-------------Errori in output-------------")
print("Fattore di amplificazione |x|/|x+y|: %e" % ampl_x)
print("Fattore di amplificazione |y|/|x+y|: %e" % ampl_y)
print("Errore sulla somma = %e" % err_s)

