from CalculadoraPOO import *
def pestanaBasica(ventana):
    tableroBasico=ventana.misFrames("Basico")
    displayBasico=ventana.entrada(tableroBasico,25,1,1,6)
    botones=[['7','8','9','←','x²','xʸ'],['4','5','6','√','log','÷'],['1','2','3','ₓ','+','-'],['0','.','π','ln','℮','n!'],['(',')','=','sen','cos','tan']]
    textoBotones=[['7','8','9','←','²','ˆ'],['4','5','6','√(','log(','÷'],['1','2','3','·','+','-'],['0','.','π','ln(','℮ˆ(','!'],['(',')','OperarBasico','sen(','cos(','tan(']]
    for i in range(5):
        for j in range(6):
            if(j<3):
                ventana.Botones(i+2,j+1,botones[i][j],textoBotones[i][j],10,1,tableroBasico,displayBasico[0])
            else:
                ventana.Botones(i+2,j+1,botones[i][j],textoBotones[i][j],5,1,tableroBasico,displayBasico[0])

    ventana.Botones(1,6,'CE','CE',5,1,tableroBasico,displayBasico[0])

def pestanaAvanzada(ventana):
    tableroAvanzado=ventana.misFrames("Avanzado")
    displayAvanzado=ventana.entrada(tableroAvanzado,25,1,1,6)
    botones=[['7','8','9','←','x','y'],['4','5','6','ƒ՚','∫','÷'],['1','2','3','ₓ','+','-'],['0','.','π','ln','e','xʸ'],['(',')','=','sen','cos','tan']]
    textoBotones=[['7','8','9','←','x','y'],['4','5','6','ƒ՚(','∫(','÷'],['1','2','3','·','+','-'],['0','.','π','ln(','eˆ(','ˆ'],['(',')','OperarAvanzado','sen(','cos(','tan(']]
    for i in range(5):
        for j in range(6):
            if(j<3):
                ventana.Botones(i+2,j+1,botones[i][j],textoBotones[i][j],10,1,tableroAvanzado,displayAvanzado[0])
            else:
                ventana.Botones(i+2,j+1,botones[i][j],textoBotones[i][j],5,1,tableroAvanzado,displayAvanzado[0])

    ventana.Botones(1,6,'CE','CE',5,1,tableroAvanzado,displayAvanzado[0])

def pestanaMyV(ventana):
    TableroMatrices=ventana.misFrames("Matrices y Vectores")
    DisplayMatriz=ventana.entrada(TableroMatrices,25,6,1,5)

    ventana.Botones(1,1,'+','Agregar',6,1,TableroMatrices,TableroMatrices)
    ventana.Botones(1,2,'-','Quitar',6,1,TableroMatrices,TableroMatrices)
    ventana.Botones(1,3,'←','Limpiar',6,1,TableroMatrices,TableroMatrices)
    ventana.Botones(1,4,'=','Escalonar',6,1,TableroMatrices,DisplayMatriz[0])

    filas=[]
    filas.append(ventana.entrada(TableroMatrices,4,2,1,1))
    filas.append(ventana.entrada(TableroMatrices,4,2,2,1))
    filas.append(ventana.entrada(TableroMatrices,4,2,3,1))
    ventana.entradasMatriz.append(filas)

    filas=[]
    filas.append(ventana.entrada(TableroMatrices,4,3,1,1))
    filas.append(ventana.entrada(TableroMatrices,4,3,2,1))
    filas.append(ventana.entrada(TableroMatrices,4,3,3,1))
    ventana.entradasMatriz.append(filas)