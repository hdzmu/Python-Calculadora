from tkinter import *

ventana=Tk()

ventana.title("Steel Learning")
ventana.iconbitmap("Imagenes/IconCal.ico")
ventana.config(bg="black")

tablero=Frame(ventana, bg="black")
tablero.pack()

miImagen=PhotoImage(file="Imagenes/fondo.png")
fondo=Label(tablero, image=miImagen, bg="black").place(x=0, y=0)

display=Entry(tablero, highlightthickness=1) #highlightthickness grosor de borde
display.grid(row=1, column=1, padx=10, pady=10, columnspan=6)
display.config(bg="black", fg="#12ED3E", highlightbackground = "#12ED3E",highlightcolor= "white",font=("Ink Free",30), justify="right")

#Numeros

bt7=Button(tablero, width=10, height=1 ,text="7")
bt7.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
bt7.grid(row=2, column=1, padx=5 , pady=5)

bt8=Button(tablero, width=10, height=1 ,text="8")
bt8.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
bt8.grid(row=2, column=2, padx=5 , pady=5)

bt9=Button(tablero, width=10, height=1 ,text="9")
bt9.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
bt9.grid(row=2, column=3, padx=5 , pady=5)

bt4=Button(tablero, width=10, height=1 ,text="4")
bt4.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
bt4.grid(row=3, column=1, padx=5 , pady=5)

bt5=Button(tablero, width=10, height=1 ,text="5")
bt5.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
bt5.grid(row=3, column=2, padx=5 , pady=5)

bt6=Button(tablero, width=10, height=1 ,text="6")
bt6.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
bt6.grid(row=3, column=3, padx=5 , pady=5)

bt1=Button(tablero, width=10, height=1 ,text="1")
bt1.config(bg="black", fg="#12ED3E", font=("Ink Free",20))
bt1.grid(row=4, column=1, padx=5 , pady=5)

bt2=Button(tablero, width=10, height=1 ,text="2")
bt2.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
bt2.grid(row=4, column=2, padx=5 , pady=5)

bt3=Button(tablero, width=10, height=1 ,text="3")
bt3.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
bt3.grid(row=4, column=3, padx=5 , pady=5)

bt0=Button(tablero, width=10, height=1 ,text="0")
bt0.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
bt0.grid(row=5, column=1, padx=5 , pady=5)

btpunto=Button(tablero, width=10, height=1 ,text=".")
btpunto.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btpunto.grid(row=5, column=2, padx=5 , pady=5)

btpi=Button(tablero, width=10, height=1 ,text="π")
btpi.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btpi.grid(row=5, column=3, padx=5 , pady=5)

#simbolos de operadores

btborrar=Button(tablero, width=5, height=1 ,text="←")
btborrar.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btborrar.grid(row=2, column=4, padx=5 , pady=5)

btpotencia=Button(tablero, width=5, height=1 ,text="x²")
btpotencia.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btpotencia.grid(row=2, column=5, padx=5 , pady=5)

btpotenciay=Button(tablero, width=5, height=1 ,text="xʸ")
btpotenciay.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btpotenciay.grid(row=2, column=6, padx=5 , pady=5)

btraiz=Button(tablero, width=5, height=1 ,text="√")
btraiz.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btraiz.grid(row=3, column=4, padx=5 , pady=5)

btrporcentaje=Button(tablero, width=5, height=1 ,text="%")
btrporcentaje.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btrporcentaje.grid(row=3, column=5, padx=5 , pady=5)

btdivi=Button(tablero, width=5, height=1 ,text="÷")
btdivi.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btdivi.grid(row=3, column=6, padx=5 , pady=5)

btmulti=Button(tablero, width=5, height=1 ,text="x")
btmulti.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btmulti.grid(row=4, column=4, padx=5 , pady=5)

btsuma=Button(tablero, width=5, height=1 ,text="+")
btsuma.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btsuma.grid(row=4, column=5, padx=5 , pady=5)

btresta=Button(tablero, width=5, height=1 ,text="-")
btresta.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btresta.grid(row=4, column=6, padx=5 , pady=5)

btsigno=Button(tablero, width=5, height=1 ,text="±")
btsigno.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btsigno.grid(row=5, column=4, padx=5 , pady=5)

btexp=Button(tablero, width=5, height=1 ,text="e")
btexp.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btexp.grid(row=5, column=5, padx=5 , pady=5)

btfact=Button(tablero, width=5, height=1 ,text="n!")
btfact.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btfact.grid(row=5, column=6, padx=5 , pady=5)

btlog=Button(tablero, width=5, height=1 ,text="log")
btlog.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btlog.grid(row=6, column=4, padx=5 , pady=5)

btln=Button(tablero, width=5, height=1 ,text="ln")
btln.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btln.grid(row=6, column=5, padx=5 , pady=5)

btigual=Button(tablero, width=5, height=1 ,text="=")
btigual.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btigual.grid(row=6, column=6, padx=5 , pady=5)

btpareni=Button(tablero, width=10, height=1 ,text="(")
btpareni.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btpareni.grid(row=6, column=1, padx=5 , pady=5)

btparend=Button(tablero, width=10, height=1 ,text=")")
btparend.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btparend.grid(row=6, column=2, padx=5 , pady=5)

btexp=Button(tablero, width=10, height=1 ,text="exp")
btexp.config(bg="black", fg="#12ED3E",font=("Ink Free",20))
btexp.grid(row=6, column=3, padx=5 , pady=5)

ventana.mainloop()