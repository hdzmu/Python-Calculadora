#Caso mio derivar
import sympy as smp
from sympy import *

def derivarPolinomios(texto, sim, orden):
    x = symbols(sim)
    if orden == 0 or orden == None: orden = 1
    #funcion = sympy.Poly(texto)
    derivada = diff(texto, x, orden)

    return (derivada)

def convertir(texto):
    new = ""
    salto = 0
    operacion = ""
    for i in texto:
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
            #elif(i=='e'):
                #new+=operacionEspecial(funcion,'e')
                #salto=len(operacionEspecial(funcion,'e'))
            #elif(i=='√'):
                #new+=operacionEspecial(funcion,'√')
                #salto=len(operacionEspecial(funcion,'√'))
            elif(i=='ƒ' or i== '՚'):
                operacion = "ƒ"
                continue
            elif(i==","):
                break
            else:
                new+=i

def operarParentesis(texto):
    cantP1 = 0
    cantP2 = 0
    posicionP1 = 0
    posicionP2 = 0
    operacion = ""
    activar = True

    #intento = 1
    
    while(activar):
        cantP1 = 0
        cantP2 = 0
        operacion = ""
        print("Texto: ",texto)
        if (len(texto)==1 ): activar =False
        for i in range(len(texto)):
            if(texto[i] =="("):
                cantP1 += 1
                posicionP1 = i
                #Aca identificar la función o la operación
                operacion = identificarOperacion(texto,i)
            elif(texto[i] ==")"):
                cantP2 += 1
                if(cantP2 == 1):
                    posicionP2 = i
        if(cantP1 != cantP2):
            print("Error, cierre parentesis")
            activar = False
        elif (cantP1==0 and cantP2==0):
            activar = False
        else:
            subtexto = ""
            for j in range(posicionP1,posicionP2+1,1):
                subtexto += texto[j]
            print("subtexto: ", subtexto)
            texto = texto.replace(subtexto, operar(subtexto, operacion))
            
            #Comprovar iteraciones
            #if intento == 2:
            #    activar = False
            #intento +=1



def OperarParentesis(texto, posicionP1, posicionP2):
    #OBSOLETO YA SE MEJORÓ ARRIBA
    subtexto = ""
    for i in range(len(posicionP1),0,-1):
        subtexto = ""
        for j in range(posicionP1[i-1],posicionP2[i-1] + 1,1):
            subtexto += texto[j]
        print(subtexto)

def identificarOperacion(texto, posicion):
    operacion = ""  
    if(texto[posicion-3]== "s" and texto[posicion-2]== "e" and texto[posicion-1]== "n"): operacion = "sen"
    elif(texto[posicion-3]== "c" and texto[posicion-2]== "o" and texto[posicion-1]== "s"): operacion = "cos"
    elif(texto[posicion-3]== "t" and texto[posicion-2]== "a" and texto[posicion-1]== "n"): operacion = "tan"
    elif(texto[posicion-3]== "c" and texto[posicion-2]== "s" and texto[posicion-1]== "c"): operacion = "csc"
    elif(texto[posicion-3]== "s" and texto[posicion-2]== "e" and texto[posicion-1]== "c"): operacion = "sec"
    elif(texto[posicion-3]== "c" and texto[posicion-2]== "o" and texto[posicion-1]== "t"): operacion = "cot"
    elif(texto[posicion-2]== "*" and texto[posicion-1]== "*"): operacion = "**"
    elif(texto[posicion-1]== "^"): operacion = "**"
    else:
        operacion = texto[posicion-1]
    return operacion

def operar(subtexto,operacion):
    #Hacer la operación que se desee
    resolver = ""
    for i in subtexto:
        if (i=="x"):
            resolver = smp.Poly(subtexto)
            break
        else:
            #resolver = eval(subtexto)
            continue
    print("operación/funcion: ",operacion)
    print(resolver)
    return resolver

#operarParentesis("1*2^(6*(x+sen(x+3+5)))")
#contarParentesis("2+(6*(x+(x+3)))")

def parentesisInterno(texto):
    posicion = [0,0]
    for i in range(0,len(texto),1):
        if(texto[i] =="("):
            posicion[0] = i
        elif(texto[i] ==")"):
            posicion[1] = i
            break
    return posicion

def solosympy(texto, sim):
    x, C = smp.symbols(sim + ' C')
    subtexto = ""
    arreglo = []
    arreglo.append(texto)
    funcion = ""
    const = False
    posicion = []
    new = texto
    for i in range(len(texto)):
        #PRIMERO SE SELECCIONA QUE FUNCION VA A HACER (SE MODIFICA PARA INTEGRARLO LUEGO)
        if(texto[i-1] =="f" and texto[i] == "¡"):
            funcion = "derivar"
        elif(texto[i-1] =="S" and texto[i] == "¡"):
            funcion = "integrar"
            const = True

        #LUEGO SE OPERA LO SEGÚN LA FUNCIÓN
        if(funcion == "derivar"):
            #print("El texto es: ",texto[i])
            posicion = parentesisInterno(new)
            subtexto = new[posicion[0]:posicion[1]+1]
            new = new.replace("f¡"+subtexto, str(smp.diff(subtexto)))

        if(funcion == "integrar"):
            #print("El texto es: ",texto[i])
            posicion = parentesisInterno(new)
            subtexto = new[posicion[0]:posicion[1]+1]
            new = new.replace("S¡"+subtexto, str(smp.integrate(subtexto,x)))
        
    if(const):
        print(str(smp.simplify(new)+C))
    else:                
        print(str(smp.simplify(new)))
    #return(new)

    #FUNCIONA ESTE SÍ s
    
solosympy("2+f¡(x**2+f¡(x**2+f¡(5*x))+f¡(x**2))+f¡(x)",'x')

def zzz(f):
    pos=[]
    inicio=1
    fin=0
    veces=1
    for i in range(2,len(f)-1,1):
        if f[i] =='¡':
            fin=i
            pos.append([inicio,fin])
            inicio=fin
            veces+=1
    
    if veces>1:
        pos.append([inicio,len(f)-1])
    print(pos)
    print(len(pos))

#zzz("f¡[sin(x)+f¡(cos(x))]+f¡(x)")
#x='x'
#funcion2='3*(x*x)'

#funcion=str("x+x+smp.diff(x**2)")


#print(eval(str("smp.diff(funcion)")))