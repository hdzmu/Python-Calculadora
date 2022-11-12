from tkinter import *
import Funciones_calculadora as fc 

ventana=Tk()

ventana.title("Steel Learning")
ventana.iconbitmap("Imagenes/IconCal.ico")
ventana.config(bg="black")

tablero=Frame(ventana, bg="black")
tablero.pack()

miImagen=PhotoImage(file="Imagenes/fondo.png")
fondo=Label(tablero, image=miImagen, bg="black").place(x=0, y=0)

textoDisplay=StringVar()
fuente="Times new roman"

display=Entry(tablero, highlightthickness=1, textvariable=textoDisplay) #highlightthickness grosor de borde
display.grid(row=1, column=1, padx=10, pady=10, columnspan=6)
display.config(bg="black", fg="#12ED3E", highlightbackground = "#12ED3E",highlightcolor= "white",font=(fuente,30), justify="right")


#Numeros

bt7=Button(tablero, width=10, height=1 ,text="7", command=lambda:fc.digitar(textoDisplay,"7"))
bt7.config(bg="black", fg="#12ED3E",font=(fuente,20))
bt7.grid(row=2, column=1, padx=5 , pady=5)

bt8=Button(tablero, width=10, height=1 ,text="8", command=lambda:fc.digitar(textoDisplay,"8"))
bt8.config(bg="black", fg="#12ED3E",font=(fuente,20))
bt8.grid(row=2, column=2, padx=5 , pady=5)

bt9=Button(tablero, width=10, height=1 ,text="9", command=lambda:fc.digitar(textoDisplay,"9"))
bt9.config(bg="black", fg="#12ED3E",font=(fuente,20))
bt9.grid(row=2, column=3, padx=5 , pady=5)

bt4=Button(tablero, width=10, height=1 ,text="4", command=lambda:fc.digitar(textoDisplay,"4"))
bt4.config(bg="black", fg="#12ED3E",font=(fuente,20))
bt4.grid(row=3, column=1, padx=5 , pady=5)

bt5=Button(tablero, width=10, height=1 ,text="5", command=lambda:fc.digitar(textoDisplay,"5"))
bt5.config(bg="black", fg="#12ED3E",font=(fuente,20))
bt5.grid(row=3, column=2, padx=5 , pady=5)

bt6=Button(tablero, width=10, height=1 ,text="6", command=lambda:fc.digitar(textoDisplay,"6"))
bt6.config(bg="black", fg="#12ED3E",font=(fuente,20))
bt6.grid(row=3, column=3, padx=5 , pady=5)

bt1=Button(tablero, width=10, height=1 ,text="1", command=lambda:fc.digitar(textoDisplay,"1"))
bt1.config(bg="black", fg="#12ED3E", font=(fuente,20))
bt1.grid(row=4, column=1, padx=5 , pady=5)

bt2=Button(tablero, width=10, height=1 ,text="2", command=lambda:fc.digitar(textoDisplay,"2"))
bt2.config(bg="black", fg="#12ED3E",font=(fuente,20))
bt2.grid(row=4, column=2, padx=5 , pady=5)

bt3=Button(tablero, width=10, height=1 ,text="3")
bt3.config(bg="black", fg="#12ED3E",font=(fuente,20), command=lambda:fc.digitar(textoDisplay,"3"))
bt3.grid(row=4, column=3, padx=5 , pady=5)

bt0=Button(tablero, width=10, height=1 ,text="0", command=lambda:fc.digitar(textoDisplay,"0"))
bt0.config(bg="black", fg="#12ED3E",font=(fuente,20))
bt0.grid(row=5, column=1, padx=5 , pady=5)

btpunto=Button(tablero, width=10, height=1 ,text=".", command=lambda:fc.digitar(textoDisplay,"."))
btpunto.config(bg="black", fg="#12ED3E",font=(fuente,20))
btpunto.grid(row=5, column=2, padx=5 , pady=5)

btpi=Button(tablero, width=10, height=1 ,text="π", command=lambda:fc.digitar(textoDisplay,"π"))
btpi.config(bg="black", fg="#12ED3E",font=(fuente,20))
btpi.grid(row=5, column=3, padx=5 , pady=5)

#simbolos de operadores

btborrar=Button(tablero, width=5, height=1 ,text="←", command=lambda:fc.limpiar(textoDisplay))
btborrar.config(bg="black", fg="#12ED3E",font=(fuente,20))
btborrar.grid(row=2, column=4, padx=5 , pady=5)

btpotencia=Button(tablero, width=5, height=1 ,text="x²", command=lambda:fc.digitar(textoDisplay,"²"))
btpotencia.config(bg="black", fg="#12ED3E",font=(fuente,20))
btpotencia.grid(row=2, column=5, padx=5 , pady=5)

btpotenciay=Button(tablero, width=5, height=1 ,text="xʸ", command=lambda:fc.digitar(textoDisplay,"ˆ["))
btpotenciay.config(bg="black", fg="#12ED3E",font=(fuente,20))
btpotenciay.grid(row=2, column=6, padx=5 , pady=5)

btraiz=Button(tablero, width=5, height=1 ,text="√", command=lambda:fc.digitar(textoDisplay,"√["))
btraiz.config(bg="black", fg="#12ED3E",font=(fuente,20))
btraiz.grid(row=3, column=4, padx=5 , pady=5)

btrporcentaje=Button(tablero, width=5, height=1 ,text="%", command=lambda:fc.digitar(textoDisplay,"%"))
btrporcentaje.config(bg="black", fg="#12ED3E",font=(fuente,20))
btrporcentaje.grid(row=3, column=5, padx=5 , pady=5)

btdivi=Button(tablero, width=5, height=1 ,text="÷", command=lambda:fc.digitar(textoDisplay,"÷"))
btdivi.config(bg="black", fg="#12ED3E",font=(fuente,20))
btdivi.grid(row=3, column=6, padx=5 , pady=5)

btmulti=Button(tablero, width=5, height=1 ,text="x", command=lambda:fc.digitar(textoDisplay,"*"))
btmulti.config(bg="black", fg="#12ED3E",font=(fuente,20))
btmulti.grid(row=4, column=4, padx=5 , pady=5)

btsuma=Button(tablero, width=5, height=1 ,text="+", command=lambda:fc.digitar(textoDisplay,"+"))
btsuma.config(bg="black", fg="#12ED3E",font=(fuente,20))
btsuma.grid(row=4, column=5, padx=5 , pady=5)

btresta=Button(tablero, width=5, height=1 ,text="-", command=lambda:fc.digitar(textoDisplay,"-"))
btresta.config(bg="black", fg="#12ED3E",font=(fuente,20))
btresta.grid(row=4, column=6, padx=5 , pady=5)

btsigno=Button(tablero, width=5, height=1 ,text="±", command=lambda:fc.digitar(textoDisplay,"±"))
btsigno.config(bg="black", fg="#12ED3E",font=(fuente,20))
btsigno.grid(row=5, column=4, padx=5 , pady=5)

btexp=Button(tablero, width=5, height=1 ,text="e", command=lambda:fc.digitar(textoDisplay,"e"))
btexp.config(bg="black", fg="#12ED3E",font=(fuente,20))
btexp.grid(row=5, column=5, padx=5 , pady=5)

btfact=Button(tablero, width=5, height=1 ,text="n!", command=lambda:fc.digitar(textoDisplay,"!"))
btfact.config(bg="black", fg="#12ED3E",font=(fuente,20))
btfact.grid(row=5, column=6, padx=5 , pady=5)

btlog=Button(tablero, width=5, height=1 ,text="log", command=lambda:fc.digitar(textoDisplay,"log["))
btlog.config(bg="black", fg="#12ED3E",font=(fuente,20))
btlog.grid(row=6, column=4, padx=5 , pady=5)

btln=Button(tablero, width=5, height=1 ,text="ln", command=lambda:fc.digitar(textoDisplay,"ln["))
btln.config(bg="black", fg="#12ED3E",font=(fuente,20))
btln.grid(row=6, column=5, padx=5 , pady=5)

btigual=Button(tablero, width=5, height=1 ,text="=", command=lambda:fc.buscarOp(textoDisplay))
btigual.config(bg="black", fg="#12ED3E",font=(fuente,20))
btigual.grid(row=6, column=6, padx=5 , pady=5)

btpareni=Button(tablero, width=10, height=1 ,text="(", command=lambda:fc.digitar(textoDisplay,"("))
btpareni.config(bg="black", fg="#12ED3E",font=(fuente,20))
btpareni.grid(row=6, column=1, padx=5 , pady=5)

btparend=Button(tablero, width=10, height=1 ,text=")", command=lambda:fc.digitar(textoDisplay,")"))
btparend.config(bg="black", fg="#12ED3E",font=(fuente,20))
btparend.grid(row=6, column=2, padx=5 , pady=5)

btexp=Button(tablero, width=10, height=1 ,text="exp", command=lambda:fc.digitar(textoDisplay,"exp["))
btexp.config(bg="black", fg="#12ED3E",font=(fuente,20))
btexp.grid(row=6, column=3, padx=5 , pady=5)

ventana.mainloop()