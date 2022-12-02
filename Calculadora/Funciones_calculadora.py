import Funciones_Matematicas as fm
from numpy import matrix
from scipy import linalg
import numpy as np 
import math
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
    funcion = funcion.replace("np.pi","π")
    funcion = funcion.replace("/","÷")
    return funcion

def operarBasico(display, funcion):
    funcion = funcion.replace("π","*"+str(np.pi))
    funcion=lenguajeCodigo(funcion)
    funcion=(eval(funcion))
    funcion=lenguajeUsuario(str(funcion))
    display.set(funcion)
    
def operarAvanzado(display, funcion, diferencial):
    funcion = funcion.replace("π","pi")
    funcion=lenguajeCodigo(funcion)
    funcion=fm.fx991(funcion,diferencial)
    funcion=lenguajeUsuario(str(funcion))
    display.set(funcion)


def operacionEspecial(funcion,operacion):
    copiar=False
    new=""
    for i in funcion:
        if(i==operacion):
            copiar=True
            continue
        elif(i==')'):
            copiar=False
            new+=i
            break
        if(copiar==True):
            new+=i
    
    if(operacion =='√'):
        new+="**(1/2)"
    return new

def convertir(display, tipoOperacion, diferencial):
    funcion=display.get()
    new=""
    salto=0
    for i in range(0,len(funcion),1):
        if(salto==0):
            if(funcion[i]=='√'):
                new+=operacionEspecial(funcion,'√')
                salto=len(operacionEspecial(funcion,'√'))
            elif funcion[i]=='s' or funcion[i]=='c' or  funcion[i]=='t':
                if(funcion[i]+funcion[i+1]+funcion[i+2]=="sen" or funcion[i]+funcion[i+1]+funcion[i+2]=="cos" or  funcion[i]+funcion[i+1]+funcion[i+2]=="tan"):
                    new+="math."+funcion[i]+funcion[i+1]+funcion[i+2]
                    salto=2
            else:
                new+=funcion[i]
        else:
            salto-=1
    if tipoOperacion=='B':
        operarBasico(display,new)
    elif tipoOperacion=='A':
        operarAvanzado(display,new, diferencial)
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
##zzz