import Funciones_Matematicas as fm
from numpy import matrix
from scipy import linalg
import numpy as np 
import math
from fractions import Fraction as frac
def digitar(display, caracter):
    display.set(display.get() + caracter)

def limpiar(display):
    text=display.get()
    text=text[:-1]
    display.set(text)

def lenguajeCodigo(funcion):
    funcion = funcion.replace("²","**2")
    funcion = funcion.replace("eˆ","exp")
    funcion = funcion.replace("ˆ","**")
    funcion = funcion.replace("sen","sin") 
    funcion = funcion.replace("·","*")
    funcion = funcion.replace("÷","/")
 

    return funcion
    

def lenguajeUsuario(funcion):
    funcion = funcion.replace("**2","²")
    funcion = funcion.replace("exp","eˆ")
    funcion = funcion.replace("**","ˆ")
    funcion = funcion.replace("sin","sen")
    funcion = funcion.replace("*","·")
    funcion = funcion.replace("log","ln")
    funcion = funcion.replace("pi","π")
    funcion = funcion.replace("/","÷")
    funcion = funcion.replace("I","i")
    return funcion

def operarBasico(display, funcion):
    funcion = funcion.replace("π","*"+str(np.pi))
    if "ln" in funcion:
        funcion = funcion.replace("ln","np.log")
    elif "log" in funcion:
        funcion = funcion.replace("log","np.log10")
    funcion = funcion.replace("℮ˆ","np.exp")
    funcion = funcion.replace("√","np.sqrt")
    funcion=lenguajeCodigo(funcion)
    funcion=(eval(funcion))
    funcion=lenguajeUsuario(str(funcion))
    display.set(funcion)
    
def operarAvanzado(display, funcion, diferencial,a,b):
    try:
        funcion = funcion.replace("π","pi")
        funcion = lenguajeCodigo(funcion)
        funcion = raizExacta(funcion)
        funcion = fm.fx991(funcion,diferencial, a, b)
        funcion = lenguajeUsuario(str(funcion))        
        display.set(funcion)
    except:
        display.set("Syntax Error")

def convertir(display, tipoOperacion, diferencial,a,b):
    funcion=display.get()
    new=""
    salto=0
    ultimoperador=0
    factorial=""
    fac=""
    for i in range(0,len(funcion),1):
        if(salto==0):
            if funcion[i]=='s' or funcion[i]=='c' or  funcion[i]=='t':
                if(funcion[i]+funcion[i+1]+funcion[i+2]=="sen" or funcion[i]+funcion[i+1]+funcion[i+2]=="cos" or  funcion[i]+funcion[i+1]+funcion[i+2]=="tan"):
                    new+="math."+funcion[i]+funcion[i+1]+funcion[i+2]
                    salto=2
            elif(funcion[i]=='!'):
                new+=funcion[i]
                factorial=funcion[ultimoperador:i]
                fac=funcion[ultimoperador:i+1]
                new=new.replace(fac,"")
                new+="math.factorial("+factorial+")"
            else:
                if(funcion[i]=='(' or funcion[i]=='+' or funcion[i]=='-' or funcion[i]=='·' or funcion[i]=='÷'):
                    ultimoperador=i+1
                new+=funcion[i]
        else:
            salto-=1
    if tipoOperacion=='B':
        operarBasico(display,new)
    elif tipoOperacion=='A':
        operarAvanzado(display,new, diferencial,a,b)

def aumentarMatriz(ventana,matriz,tablero,filas,columnas):
    fila=[]
    for i in range(0,len(matriz),1):
        matriz[i].append(ventana.entrada(tablero,4,i+2,columnas,1))
    for i in range(0,columnas,1):
        fila.append(ventana.entrada(tablero,4,filas+1,i+1,1))
    matriz.append(fila)
    fila=[]

def reducirMatriz(matriz,filas,columnas):
    for i in range(0,filas-1,1):
        for j in range(0,columnas,1):
            if j+1==columnas:
                matriz[i][j][1].destroy()
                del matriz[i][j]
    for j in range(0,columnas,1):
        matriz[filas-1][j][1].destroy()
    del matriz[filas-1]

def resolverMatriz(matriz,filas,columnas,ent):
    fila=[]
    mt=[]
    z=[]
    b=[]
    for i in range(0,filas,1):
        for j in range(0,columnas,1):
            if j+1!=columnas:
                fila.append((matriz[i][j][0]).get())
            else:
                z.append((matriz[i][j][0]).get())
        mt.append(fila)
        fila=[]
        b.append(z)
        z=[]
    mt=matrix(mt)
    b=matrix(b)
    sol=linalg.solve(mt,b)
    salida=""
    variables=["x","y","z","w"]
    for i in range(0,len(sol),1):
        sol[i]=round(float(sol[i]),2)
        salida=" "+variables[i]+" = "+str(sol[i])
        ent.set(ent.get()+salida)

def raizExacta(funcion):
    exponenteDecimal=""
    copiar=False
    for j in range(0,len(funcion),1):
        if(funcion[j-2]+funcion[j-1]+funcion[j]=="**("):
            copiar=True
            continue
        if(copiar==True):
            if(funcion[j]!=")"):
                exponenteDecimal+=funcion[j]
            else:
                break
    funcion = funcion.replace(exponenteDecimal,str(frac(exponenteDecimal)))
    return funcion