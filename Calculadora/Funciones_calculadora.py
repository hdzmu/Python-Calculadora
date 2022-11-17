def digitar(display, caracter):
    display.set(display.get() + caracter)

def limpiar(display):
    text=display.get()
    text=text[:-1]
    display.set(text)

def operar(display, funcion):
    import numpy as np
    display.set(eval(funcion))

def operacionEspecial(funcion,operacion):
    copiar=False
    new=""
    for i in funcion:
        if(i==operacion):
            copiar=True
            continue
        if(i==')'):
            copiar=False
            new+=i
            break
        if(copiar==True):
            new+=i
    new+="**(1/2)"
    return new

def convertir(display):
    funcion=display.get()
    new=""
    salto=0
    especial=False
    for i in funcion:
        if(salto==0):
            if(i=='x'):
                new+='*'
            elif(i=='π'):
                new+="*np.pi"
            elif(i=='²'):
                new+="**2"
            elif(i=='ˆ'):
                new+="**"
            elif(i=='÷'):
                new+="/"
            elif(i=='√'):
                new+=operacionEspecial(funcion,'√')
                salto=len(operacionEspecial(funcion,'√'))
            else:
                new+=i
        else:
            salto-=1
    operar(display,new)




