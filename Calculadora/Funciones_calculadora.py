import Funciones_Matematicas as fm
from numpy import matrix
from scipy import linalg
import numpy as np 
def digitar(display, caracter):
    display.set(display.get() + caracter)

def limpiar(display):
    text=display.get()
    text=text[:-1]
    display.set(text)

def lenguajeCodico(display):
    display = display.replace("²","**2")
    display = display.replace("eˆ","exp")
    display = display.replace("ˆ","**")
    display = display.replace("sen","sin")
    display = display.replace("·","*")

def lenguajeUsuario(display):
    display = display.replace("**2","²")
    display = display.replace("exp","eˆ")
    display = display.replace("**","ˆ")
    display = display.replace("sin","sen")
    display = display.replace("*","·")


def operar(display, funcion, operacion):
    import numpy as np
    texto = display.get()
    if(operacion=="ƒ"):
        sim = "x"
        cont = 0
        orden = 0
        for i in range(len(texto)-1):
            if(texto[i]==","):
                cont+=1
                if(cont == 1):
                    sim = texto[i+1]
                elif(cont==2): 
                    orden = texto[i+1]
        result = fm.derivarPolinomios(funcion,sim,orden)
        display.set(result)
        emb = embellecedor(display.get())
        display.set(emb)
        
    else:
        display.set(eval(funcion))


def operacionEspecial(funcion,operacion):
    copiar=False
    new=""
    for i in funcion:
        if(i==operacion):
            copiar=True
            continue
        elif(i=='ˆ'):
            #Arreglar
            new+="**"
            continue
        elif(i=='·'):
            new+="*"
            continue
        elif(i=='²'):
            new+="**2"
            continue
        if(i==')'):
            copiar=False
            new+=i
            break
        if(copiar==True):
            new+=i
    
    if(operacion =='√'):
        new+="**(1/2)"
    elif(operacion == 'e'):
        new="exp"+ new +")"
        #print(new)

    return new

def convertir(display):
    funcion=display.get()
    new=""
    salto=0
    operacion = ""
    especial=False
    for i in funcion:
        if(salto==0):
            if(i=='ₓ'):
                new+='*'
            elif(i=='·'):
                new+='*'
            elif(i=='π'):
                new+="*np.pi"
            elif(i=='²'):
                new+="**2"
            elif(i=='ˆ'):
                new+="**"
            elif(i=='÷'):
                new+="/"
            elif(i=='e'):
                new+=operacionEspecial(funcion,'e')
                salto=len(operacionEspecial(funcion,'e'))
            elif(i=='√'):
                new+=operacionEspecial(funcion,'√')
                salto=len(operacionEspecial(funcion,'√'))
            elif(i=='ƒ' or i== '՚'):
                operacion = "ƒ"
                continue
            elif(i==","):
                break
            else:
                new+=i
        else:
            salto-=1
    operar(display,new, operacion)

def embellecedor(display):
    #print(display)
    new=""
    for i in range(len(display)):
        if(display[i]=='*'):
            if(display[i+1]=='*'):
                new+='ˆ'               
            else:
                if(new[len(new)-1]!='ˆ'):
                    new+='·'

        else:
            new+= display[i]   
    return new

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
