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
        
        self.notebook=ttk.Notebook(self.ventana)
        self.notebook.pack(fill='both', expand='yes')

        self.filas=2
        self.columnas=3
        self.entradasMatriz=[]

        self.diferencial='x'
        self.a=0
        self.b=0
        self.integrar=False

    def misFrames(self, textoMenu):
        self.tablero=tk.Frame(self.notebook, bg="black")
        self.fondo=tk.Label(self.tablero, image=self.miImagen, bg="black").place(x=0, y=0)
        self.pestana=self.notebook.add(self.tablero, text=textoMenu)
        return self.tablero

    def entrada(self,tablero,ancho,i,j,ncolumnas):
        self.textoDisplay=tk.StringVar()
        self.display=tk.Entry(tablero, highlightthickness=1, textvariable=self.textoDisplay, width=ancho)
        self.display.grid(row=i, column=j, padx=10, pady=10, columnspan=ncolumnas)
        self.display.config(bg="black", fg=self.color, highlightbackground = self.color,highlightcolor= "white",font=(self.fuente,30), justify="right")
        return [self.textoDisplay,self.display]

    def funcionBoton(self, textoFuncion, display):
        if(textoFuncion=='←'):
            self.new=display.get()
            self.new=self.new[:-1]
            display.set(self.new)
        elif(textoFuncion=='CE'):
            self.integrar=False
            display.set("")
        elif(textoFuncion=='OperarBasico'):
            fc.convertir(display,'B', self.diferencial, self.a, self.b)
        elif(textoFuncion=='∫('):
            display.set(display.get()+textoFuncion)
            self.integrar=True
        elif(textoFuncion=='OperarAvanzado'):
            if(self.integrar==True):
                self.a=0
                self.b=0
                self.ventanaLimites(display)
            else:
                if 'y' in display.get():
                    self.dxdzdy(display)
                else:
                    fc.convertir(display,'A', self.diferencial,self.a,self.b)
        elif(textoFuncion=="Agregar"):
            if self.filas<4:
                self.filas+=1
                self.columnas+=1
                fc.aumentarMatriz(self,self.entradasMatriz,display,self.filas,self.columnas)
        elif(textoFuncion=="Quitar"):
            if self.filas>2:
                fc.reducirMatriz(self.entradasMatriz,self.filas,self.columnas)
                self.filas-=1
                self.columnas-=1
        elif(textoFuncion=='Escalonar'):
            fc.resolverMatriz(self.entradasMatriz,self.filas,self.columnas,display)
        elif(textoFuncion=='Aceptar_L'):
            if self.a_L[0].get()!="" or self.b_L[0].get()!="":
                self.a=self.a_L[0].get()
                self.b=self.b_L[0].get()
            self.integrar=False
            self.ventana_L.destroy()
            fc.convertir(display,'A', self.diferencial,self.a,self.b)
        elif(textoFuncion=='Aceptar_D'):
            self.diferencial=self.D[0].get()
            self.ventana_D.destroy()
            fc.convertir(display,'A', self.diferencial,self.a,self.b)
        else:
            display.set(display.get()+textoFuncion)
    
    def Botones(self,i,j,textoBoton, textoFuncion, ancho, alto,tablero, display):
        self.boton=tk.Button(tablero, width=ancho, height=alto, text=textoBoton,command=lambda:self.funcionBoton(textoFuncion,display))
        self.boton.config(bg="black", fg=self.color,font=(self.fuente,20))
        self.boton.grid(row=i , column=j, padx=5 , pady=5)

    def textos(self,i,j,tablero, texto):
        self.textoLabel=tk.StringVar()
        self.textoLabel.set(texto)
        self.textoLabel=tk.Label(tablero, text=self.textoLabel.get())
        self.textoLabel.config(bg="black", fg=self.color, font=(self.fuente,30))
        self.textoLabel.grid(row=i, column=j, padx=10, pady=10)

    def ventanaLimites(self,display):
        self.ventana_L=tk.Toplevel()
        self.ventana_L.title("Limites de Integracion")
        self.ventana_L.iconbitmap("Icono.ico")
        self.ventana_L.config(bg="black")
        self.ventana_L.resizable(0,0)
        self.tablero_L=tk.Frame(self.ventana_L, bg="black")
        self.fondo_L=tk.Label(self.tablero_L, image=self.miImagen, bg="black").place(x=0, y=0)
        self.tablero_L.pack()
        self.textos(1,1,self.tablero_L,"a: ")
        self.a_L=self.entrada(self.tablero_L,4,1,2,1)
        self.textos(2,1,self.tablero_L,"b: ")
        self.b_L=self.entrada(self.tablero_L,4,2,2,1)
        self.Botones(3,2,"Aceptar", "Aceptar_L", 10, 1,self.tablero_L, display)
    
    def dxdzdy(self,display):
        self.ventana_D=tk.Toplevel()
        self.ventana_D.title("Diferencial")
        self.ventana_D.iconbitmap("Icono.ico")
        self.ventana_D.config(bg="black")
        self.ventana_D.resizable(0,0)
        self.tablero_D=tk.Frame(self.ventana_D, bg="black")
        self.fondo_D=tk.Label(self.tablero_D, image=self.miImagen, bg="black").place(x=0, y=0)
        self.tablero_D.pack()
        self.textos(1,1,self.tablero_D,"Ingrese diferencial: ")
        self.D=self.entrada(self.tablero_D,4,1,2,1)
        self.Botones(3,1,"Aceptar", "Aceptar_D", 10, 1,self.tablero_D, display)