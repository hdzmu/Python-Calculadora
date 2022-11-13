def digitar(display, caracter):
    display.set(display.get() + caracter)

def limpiar(display):
    text=display.get()
    text=text[:-1]
    display.set(text)

def convertir(display):
    print("")
def operar(display):
    display.set(eval(display.get()))