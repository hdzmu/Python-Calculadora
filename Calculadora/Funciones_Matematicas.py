'''import numpy as np
numerocadena=eval("np.pi")
print(type(numerocadena))

print(np.sin(numerocadena*(np.pi/180)))'''

#victor ingrese su funcion
import sympy as smp
from sympy import *

def derivarPolinomios(texto, sim, orden):
    x = smp.symbols(sim)
    if orden == 0 or orden == None: orden = 1
    #funcion = sympy.Poly(texto)
    derivada = diff(texto, x, orden)

    return (derivada)

print(type(derivarPolinomios("exp(x**2)","x",1)))

def solosympy(texto, sim):
    x, C = smp.symbols(sim + ' C')
    subtexto = ""
    cantP1=0
    cantP2=0
    funcion = ""
    new = texto
    for i in range(len(texto)):
        #PRIMERO SE SELECCIONA QUE FUNCION VA A HACER
        if(texto[i-1] =="f" and texto[i] == "¡"):
            funcion = "derivar"
        elif(texto[i-1] =="S" and texto[i] == "¡"):
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
                reemplazar = "f¡"+subtexto
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
                reemplazar = "S¡"+subtexto
                new = new.replace(reemplazar,str(integrate(subtexto,x)+C))
                subtexto = ""
    
    return (smp.sympify(new))

    
print(solosympy("(x**2+x+3*x) + f¡(E**(x**2)-(3+8*x))+S¡(2*x)",'x'))

#Jose D:
def mainfuncion():
    import math
    m=0
    F=input("digite la función que quiere realizar: ")
    x=eval(input("argumento de la función: "))
    if F=="secante":
        x1=math.cos(x)
        m=1/x1
        print(m)
    elif F=="cosecante":
        x2=math.sin(x)
        m=1/x2
        print(m)
    elif F=="cotangente":
        x3=math.tan(x)
        m=1/x3
        print(m)
    elif F=="arctangenteh":
        m=math.atanh(x)
        print(m)
    elif F=="arcosenoh":
        m=math.acosh(x)
        print(m)
    elif F=="arcsenoh":
        m=math.asinh(x)
        print(m)
    elif F=="arctangente":
        m=math.atan(x)
        print(m)
    elif F=="arcoseno":
        m=math.acos(x)
        print(m)
    elif F=="arcseno":
        m=math.asin(x)
        print(m)
    elif F=="tangenteh":
        m=math.tanh(x)
        print(m)
    elif F=="cosenoh":
        m=math.cosh(x)
        print(m)
    elif F=="senoh":
        m=math.sinh(x)
        print(m)
    elif F=="tangente":
        m=math.tan(x)
        print(m)
    elif F=="coseno":
        m=math.cos(x)
        print(m)
    elif F=="seno":
        m=math.sin(x)
        print(m)
#mainfuncion()