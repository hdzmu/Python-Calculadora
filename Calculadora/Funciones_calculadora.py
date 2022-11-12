def digitar(display, caracter):
    display.set(display.get() + caracter)

def limpiar(display):
    text=display.get()
    text=text[:-1]
    display.set(text)

def buscarOp(display):
    operaciones=[]
    especial=""
    num=""
    for i in display.get():
        if(i=="²" or i=="ˆ" or i=="√" or i=="%" or i=="÷" or i=="*" or i=="+" or i=="-" or i=="±" or i=="!" or i=="(" or i==")"):
            operaciones.append(i)
        elif(i=="l" or i=="o" or i=="g" or i=="l" or i=="n" or i=="e" or i=="x" or i=="p"):
            especial+=i
        elif(ord(i)>47 and ord(i)<58 or i=="." or i=="π" or i=="e"):
            num+=i
        if(especial=="log" or especial=="ln" or especial=="exp"):
            operaciones.append(especial)
            especial=""
        
    print(operaciones)
    print(num)
