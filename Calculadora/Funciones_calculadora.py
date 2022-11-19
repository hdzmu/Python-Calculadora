import Funciones_Matematicas as fm

def digitar(display, caracter):
    display.set(display.get() + caracter)

def limpiar(display):
    text=display.get()
    text=text[:-1]
    display.set(text)

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
        print(new)

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