import tkinter as tk
from tkinter import ttk
import Funciones_calculadora as fc
class Tablero:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Steel Learning")
        self.ventana.iconbitmap("Icono.ico")
        self.ventana.config(bg="black")
        self.ventana.resizable(0,0)

        self.fuente="Arial"
        self.color="#12ED3E"
        self.miEstilo = ttk.Style()
        self.miEstilo.theme_use('default')
        #print(self.miEstilo.theme_names())
        self.miEstilo.configure('TNotebook', background="black")
        self.miEstilo.configure('TNotebook.Tab', background="black",foreground=self.color, font=(self.fuente,20))
        self.miEstilo.map("TNotebook.Tab", background= [("selected", self.color)], foreground= [("selected", "black")])
        self.miImagen=tk.PhotoImage(file="Fondo.png")

        self.nb=ttk.Notebook(self.ventana)
        self.nb.pack(fill='both', expand='yes')

        self.filas=2
        self.columnas=3
        self.entradasMatriz=[]
        
    def misFrames(self, texto):
        self.tablero=tk.Frame(self.nb, bg="black")
        self.fondo=tk.Label(self.tablero, image=self.miImagen, bg="black").place(x=0, y=0)
        self.pestana=self.nb.add(self.tablero, text=texto)
        return self.tablero

    def entrada(self,tab,w,x,y,cl):
        self.tx=tk.StringVar()
        self.display=tk.Entry(tab, highlightthickness=1, textvariable=self.tx, width=w)
        self.display.grid(row=x, column=y, padx=10, pady=10, columnspan=cl)
        self.display.config(bg="black", fg=self.color, highlightbackground = self.color,highlightcolor= "white",font=(self.fuente,30), justify="right")
        return [self.tx,self.display]

    def tipoBoton(self, num, ent):
        if(num=='←'):
            self.new=ent.get()
            self.new=self.new[:-1]
            ent.set(self.new)
        elif(num=='CE'):
            ent.set("")
        elif(num=='='):
            fc.convertir(ent)
        elif(num=="Agregar"):
            if self.filas<4:
                self.filas+=1
                self.columnas+=1
                fc.aumentarMatriz(self,self.entradasMatriz,ent,self.filas,self.columnas)
        elif(num=="Quitar"):
            if self.filas>2:
                fc.reducirMatriz(self.entradasMatriz,self.filas,self.columnas)
                self.filas-=1
                self.columnas-=1
        elif(num=='Escalonar'):
            fc.resolverMatriz(self.entradasMatriz,self.filas,self.columnas,ent)
        else:
            ent.set(ent.get()+num)
    
    def Botones(self,i,j,tx, txp, ancho, alto,tab, ent):
        self.boton=tk.Button(tab, width=ancho, height=alto, text=tx,command=lambda:self.tipoBoton(txp,ent))
        self.boton.config(bg="black", fg=self.color,font=(self.fuente,20))
        self.boton.grid(row=i , column=j, padx=5 , pady=5)

    def textos(self,fila,columna,tab):
        self.txl=tk.StringVar()
        self.lb=tk.Label(tab, text=self.txl.get())
        self.lb.config(bg="black", fg=self.color, font=(self.fuente,30))
        self.lb.grid(row=fila, column=columna, padx=10, pady=10)
        return self.txl


       
ventana=Tablero()

# Interfaz Básica
frameBasico=ventana.misFrames("Basico")
entBasico=ventana.entrada(frameBasico,25,1,1,6)
botones=[['7','8','9','←','x²','xʸ'],['4','5','6','√','log','÷'],['1','2','3','ₓ','+','-'],['0','.','π','ln','e','n!'],['(',')','=','sen','cos','tan']]
texto=[['7','8','9','←','²','ˆ'],['4','5','6','√(','log(','÷'],['1','2','3','·','+','-'],['0','.','π','ln(','e','!'],['(',')','=','sen(','cos(','tan(']]
for i in range(5):
    for j in range(6):
        if(j<3):
            ventana.Botones(i+2,j+1,botones[i][j],texto[i][j],10,1,frameBasico,entBasico[0])
        else:
            ventana.Botones(i+2,j+1,botones[i][j],texto[i][j],5,1,frameBasico,entBasico[0])

ventana.Botones(1,6,'CE','CE',5,1,frameBasico,entBasico[0])

# Interfaz Avanzada
frameAvanzado=ventana.misFrames("Avanzado")
entAvanzada=ventana.entrada(frameAvanzado,25,1,1,6)
botones=[['7','8','9','←','x²','xʸ'],['4','5','6','ƒ՚','log','÷'],['1','2','3','x','+','-'],['0','.','π','ln','e','n!'],['(',')','=','sen','cos','tan']]
texto=[['7','8','9','←','²','ˆ'],['4','5','6','ƒ՚(','log(','÷'],['1','2','3','x','+','-'],['0','.','π','ln(','e','!'],['(',')','=','sin(','cos(','tan(']]
for i in range(5):
    for j in range(6):
        if(j<3):
            ventana.Botones(i+2,j+1,botones[i][j],texto[i][j],10,1,frameAvanzado,entAvanzada[0])
        else:
            ventana.Botones(i+2,j+1,botones[i][j],texto[i][j],5,1,frameAvanzado,entAvanzada[0])

ventana.Botones(1,7,"ₓ","·",5,1,frameAvanzado,entAvanzada[0])
ventana.Botones(2,7,",",",",5,1,frameAvanzado,entAvanzada[0])

ventana.Botones(1,6,'CE','CE',5,1,frameAvanzado,entAvanzada[0])

frMatrices=ventana.misFrames("Matrices")
entMatriz=ventana.entrada(frMatrices,25,6,1,5)

ventana.Botones(1,1,'+','Agregar',6,1,frMatrices,frMatrices)
ventana.Botones(1,2,'-','Quitar',6,1,frMatrices,frMatrices)
ventana.Botones(1,3,'←','Limpiar',6,1,frMatrices,frMatrices)
ventana.Botones(1,4,'=','Escalonar',6,1,frMatrices,entMatriz[0])

filas=[]
filas.append(ventana.entrada(frMatrices,4,2,1,1))
filas.append(ventana.entrada(frMatrices,4,2,2,1))
filas.append(ventana.entrada(frMatrices,4,2,3,1))
ventana.entradasMatriz.append(filas)

filas=[]
filas.append(ventana.entrada(frMatrices,4,3,1,1))
filas.append(ventana.entrada(frMatrices,4,3,2,1))
filas.append(ventana.entrada(frMatrices,4,3,3,1))
ventana.entradasMatriz.append(filas)


ventana.ventana.mainloop()




