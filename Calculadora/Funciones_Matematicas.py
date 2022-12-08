import sympy as smp
from sympy import *
import numpy as np 

def derivarPolinomios(texto, sim, orden):
    x = smp.symbols(sim)
    if orden == 0 or orden == None: orden = 1
    #funcion = sympy.Poly(texto)
    derivada = diff(texto, x, orden)

    return (derivada)

#print(type(derivarPolinomios("exp(x**2)","x",1)))

def parentesisInterno(texto):
    posicion = [0,0]
    contador = 0
    for i in range(len(texto)):
        if(len(texto)>3):
            if(texto[i-3]+texto[i-2]+texto[i-1]+texto[i] == "sin("
                or texto[i-3]+texto[i-2]+texto[i-1]+texto[i] == "cos("
                or texto[i-3]+texto[i-2]+texto[i-1]+texto[i] == "tan("
                or texto[i-3]+texto[i-2]+texto[i-1]+texto[i] == "exp("):
                contador += 1
                continue
            elif(texto[i-2] =="l" and texto[i-1] =="n" and texto[i] =="("):
                contador += 1
                continue          
            elif(texto[i] =="("):
                posicion[0] = i
            elif(texto[i] ==")"):
                posicion[1] = i
                if(contador == 0):
                    break
                contador -= 1
        else:
            if(texto[i] =="("):
                posicion[0] = i
            elif(texto[i] ==")"):
                posicion[1] = i
                if(contador == 0):
                    break
                contador -= 1
    return posicion

def fx991(texto, sim, a, b):
    x, C = smp.symbols(sim + ' C')
    texto = texto.replace("E**","exp")
    subtexto = ""
    funcion = ""
    const = False
    posicion = []
    new = texto
    for i in range(len(texto)):
        #PRIMERO SE SELECCIONA QUE FUNCION VA A HACER (SE MODIFICA PARA INTEGRARLO LUEGO)
        if(texto[i-1] =="ƒ" and texto[i] == "՚"):
            funcion = "derivar"
        elif(texto[i] =="∫"):
            funcion = "integrar"
        #LUEGO SE OPERA LO SEGÚN LA FUNCIÓN
        if(funcion == "derivar"):
            posicion = parentesisInterno(new)
            subtexto = new[posicion[0]:posicion[1]+1]
            new = new.replace("ƒ՚"+subtexto, str(smp.diff(subtexto,x)))

        if(funcion == "integrar"):
            posicion = parentesisInterno(new)
            subtexto = new[posicion[0]:posicion[1]+1]
            if(a != 0 and b != 0):
                new = new.replace("∫"+subtexto, str(smp.integrate(subtexto,(x,a,b))))
            else:
                new = new.replace("∫"+subtexto, str(smp.integrate(subtexto,x)))
                const = True
        
    if(const):
        return(smp.simplify(new) + C)
    else:                
        return(smp.simplify(new))

    
print(fx991("1+1",'x','1','1'))