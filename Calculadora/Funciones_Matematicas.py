'''import numpy as np
numerocadena=eval("np.pi")
print(type(numerocadena))

print(np.sin(numerocadena*(np.pi/180)))'''

#victor ingrese su funcion
import sympy
from sympy import *

def derivarPolinomios(texto, sim,orden):
    x = symbols(sim)
    if orden == 0 or orden == None: orden = 1
    #funcion = sympy.Poly(texto)
    derivada = diff(texto, x, orden)

    return (derivada)

