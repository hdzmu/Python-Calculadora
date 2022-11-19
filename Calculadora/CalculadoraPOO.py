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

        self.fuente="Ink free"
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
        
    def misFrames(self, texto):
        self.tablero=tk.Frame(self.nb, bg="black")
        self.fondo=tk.Label(self.tablero, image=self.miImagen, bg="black").place(x=0, y=0)
        self.pestana=self.nb.add(self.tablero, text=texto)
        return self.tablero

    def entrada(self,tab):
        self.tx=tk.StringVar()
        self.display=tk.Entry(tab, highlightthickness=1, textvariable=self.tx, width=25)
        self.display.grid(row=1, column=1, padx=10, pady=10, columnspan=6)
        self.display.config(bg="black", fg=self.color, highlightbackground = self.color,highlightcolor= "white",font=(self.fuente,30), justify="right")
        return self.tx

    def escribir(self, num, ent):
        if(num=='←'):
            self.new=ent.get()
            self.new=self.new[:-1]
            ent.set(self.new)
        elif(num=='CE'):
            ent.set("")
        elif(num=='='):
            fc.convertir(ent)
        else:
            ent.set(ent.get()+num)
    
    def Botones(self,i,j,tx, txp, ancho, alto,tab, ent):
        self.boton=tk.Button(tab, width=ancho, height=alto, text=tx,command=lambda:self.escribir(txp,ent))
        self.boton.config(bg="black", fg=self.color,font=(self.fuente,20))
        self.boton.grid(row=i , column=j, padx=5 , pady=5)
       
ventana=Tablero()
frameBasico=ventana.misFrames("Basico")
entBasico=ventana.entrada(frameBasico)

botones=[['7','8','9','←','x²','xʸ'],['4','5','6','√','%','÷'],['1','2','3','x','+','-'],['0','.','π','±','e','n!'],['(',')','10˟','log','ln','=']]
texto=[['7','8','9','←','²','ˆ'],['4','5','6','√(','%','÷'],['1','2','3','x','+','-'],['0','.','π','±','e','!'],['(',')','x10ˆ','log(','ln(','=']]
for i in range(5):
    for j in range(6):
        if(j<3):
            ventana.Botones(i+2,j+1,botones[i][j],texto[i][j],10,1,frameBasico,entBasico)
        else:
            ventana.Botones(i+2,j+1,botones[i][j],texto[i][j],5,1,frameBasico,entBasico)

ventana.Botones(1,6,'CE','CE',5,1,frameBasico,entBasico)

frameAvanzado=ventana.misFrames("Avanzado")
entAvanzada=ventana.entrada(frameAvanzado)
for i in range(5):
    for j in range(6):
        if(j<3):
            ventana.Botones(i+2,j+1,botones[i][j],texto[i][j],10,1,frameAvanzado,entAvanzada)
        else:
            ventana.Botones(i+2,j+1,botones[i][j],texto[i][j],5,1,frameAvanzado,entAvanzada)
ventana.Botones(1,6,'CE','CE',5,1,frameAvanzado,entAvanzada)

ventana.misFrames("Matrices")
ventana.ventana.mainloop()




