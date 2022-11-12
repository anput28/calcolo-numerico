"""
Test da eseguire per la presentazione:
    - radice quadrata
    - esponenziale
    - x^3

"""
from math import log
from random import random
from scipy.misc import derivative

def fun(x):
    y = log(x)
    return y

#inserimento dato esatto
x = float(input("Inserire il dato x: "))

#creazione dato perturbato
x_pert = x + x*random()*1.0e-8
print("x perturbato = %.15f\n" % x_pert)

#calcolo della funzione
fx = fun(x)
fx_pert = fun(x_pert)
print("f(x) = %.15f" % fx)
print("f(x_pert) = %.15f" % fx_pert)

#calcolo del fattore di amplificazione dell'errore
dx = derivative(fun, x)
fattore_amplificazione = abs(x*dx)/abs(fx)

#calcolo errori
err_input = abs(x-x_pert)/abs(x)
err_output = abs(fx-fx_pert)/abs(fx)
print("\n-----------------Errore in input-----------------")
print("Errore su x : %e" % err_input)

print("\n-----------------Errore in output-----------------")
print("Errore su f(x) : %e" % err_output)
print("Fattore di amplificazione dell'errore: %f" % fattore_amplificazione)