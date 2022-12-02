#victor ingrese su funcion
import sympy as smp
from sympy import *
import numpy as np 

def derivarPolinomios(texto, sim, orden):
    x = smp.symbols(sim)
    if orden == 0 or orden == None: orden = 1
    #funcion = sympy.Poly(texto)
    derivada = diff(texto, x, orden)

    return (derivada)

print(type(derivarPolinomios("exp(x**2)","x",1)))

def fx991(texto, sim):
    x, C = smp.symbols(sim + ' C')
    subtexto = ""
    cantP1=0
    cantP2=0
    funcion = ""
    new = texto
    for i in range(len(texto)):
        #PRIMERO SE SELECCIONA QUE FUNCION VA A HACER
        if(texto[i-1] =="ƒ" and texto[i] == "՚"):
            funcion = "derivar"
        elif(texto[i] =="∫"):
            funcion = "integrar"


        #LUEGO SE OPERA LO SEGÚN LA FUNCIÓN
        elif(funcion == "derivar"):
            if(texto[i]== "("):
                cantP1 += 1
            elif(texto[i]== ")"):
                cantP2 += 1
            subtexto += texto[i]
            if(cantP2 == cantP1):
                funcion = ""
                reemplazar = "ƒ՚"+subtexto
                new = new.replace(reemplazar,str(diff(subtexto,x)))
                subtexto = ""
        elif(funcion == "integrar"):
            if(texto[i]== "("):
                cantP1 += 1
            elif(texto[i]== ")"):
                cantP2 += 1
            subtexto += texto[i]
            if(cantP2 == cantP1):
                funcion = ""
                reemplazar = "∫"+subtexto
                new = new.replace(reemplazar,str(integrate(subtexto,x)+C))
                subtexto = ""
    
    return (smp.sympify(new))

    
#print(solosympy("(x**2+x+3*x) + f¡(E**(x**2)-(3+8*x))+S¡(2*x)",'x'))
#print(type(np.pi))