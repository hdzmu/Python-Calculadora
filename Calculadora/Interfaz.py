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
#fondo=PhotoImage(file="Imagenes/fondo.png")
#Label(miFrame, image=fondo, bg="black").place(x=0,y=0)

#miLabel=Label(miFrame, text="Calculadora")
#miLabel.place(x=350,y=10) #similar al pack() pero no cambia el frame
#miLabel.config(bg="gray")
#miLabel.config(font=("Comic Sans MS",18), fg="white")
#Label(miFrame, text="Cientifica", bg="black", fg="white", font=("Comic Sans MS",18)).place(x=1,y=10)

#CUADROS DE TEXTO
Label(miFrame, text="Ingrese numeros: ",bg="black", fg="white").grid(row=0,column=0, sticky="w", padx=10, pady=10) #(grid)alinear mediante filas y colomnnas - sticky-> alinear
texto=Entry(miFrame, bg="black", fg="white")                                                       #pad(x-y) distancia de separacion por cada lado 
texto.grid(row=0,column=1, padx=10, pady=10)

Label(miFrame, text="Ingrese 2: ",bg="black", fg="white").grid(row=1,column=0, sticky="w", padx=10, pady=10) #alinear mediante filas y colomnnas
Entry(miFrame, justify="center").grid(row=1,column=1, padx=10, pady=10)

minombre=IntVar()

Label(miFrame, text="Nombre:",bg="black", fg="white").grid(row=2,column=0, sticky="w", padx=10, pady=10) #(grid)alinear mediante filas y colomnnas
Entry(miFrame, textvariable=minombre).grid(row=2,column=1, padx=10, pady=10)

Label(miFrame, text="Password:",bg="black", fg="white").grid(row=3,column=0, sticky="w", padx=10, pady=10) #(grid)alinear mediante filas y colomnnas
Entry(miFrame,show="*").grid(row=3,column=1, padx=10, pady=10)


Label(miFrame, text="Ingrese 3: ",bg="black", fg="white").grid(row=4,column=0, sticky="w", padx=10, pady=10) #alinear mediante filas y colomnnas
ttext=Text(miFrame, width=16, height=5)#text-> cuadro de texto grande
ttext.grid(row=4,column=1, padx=10, pady=10) 
sc=Scrollbar(miFrame, command=ttext.yview)#command direccion del scroll
sc.grid(row=4 , column=2,sticky="nsew") # nsew alinear con ttext
ttext.config(yscrollcommand=sc.set)


#botones
def codigoB():
    minombre.set("Mateo")
boton1=Button(raiz, text="Enviar", command=codigoB)
boton1.config(bg="black", fg="white")
boton1.pack()
#boton1.grid(row=5, column=1)

raiz.mainloop() #bucle infinito


