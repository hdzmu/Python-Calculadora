def digitar(display, caracter):
    display.set(display.get() + caracter)

def limpiar(display):
    text=display.get()
    text=text[:-1]
    display.set(text)

def buscarOp(display):
    operaciones=[]
    for i in display.get():
        if(i=="+" or i=="" or i=="" or i=="" or i=="" or i=="" or i=="" or i=="" or i=="" or i=="" or i=="" or i=="" or i=="" or i=="" or i=="" or i==""):
            operaciones.append(i)