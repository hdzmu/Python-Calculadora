from tkinter import *

#creamos interfaz

raiz=Tk() #llamamos la clase Tk

raiz.title("Steel Calculator")

raiz.resizable(True,1) #Paramertros booleanos width - heigh

raiz.iconbitmap("Imagenes/IconCal.ico") #icono

############creamos frame############

miFrame=Frame(raiz, width=800, height=800) #creamos frame

#miFrame.pack(side="left") empaquetamos el frame en la raiz
miFrame.pack(fill="both", expand="True") #empaquetamos en la raiz y rellenamos
miFrame.config(bg="black")
miFrame.config(cursor="hand2")

############Label############
fondo=PhotoImage(file="Imagenes/fondo.png")
Label(miFrame, image=fondo, bg="black").place(x=0,y=0)

miLabel=Label(miFrame, text="Calculadora")
miLabel.place(x=350,y=10) #similar al pack() pero no cambia el frame
miLabel.config(bg="gray")
miLabel.config(font=("Comic Sans MS",18), fg="white")
Label(miFrame, text="Cientifica", bg="black", fg="white", font=("Comic Sans MS",18)).place(x=1,y=10)


raiz.mainloop() #bucle infinito


