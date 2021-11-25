def filas ():
    fila=" "
    x=input("Dame un numero: ")
    for fil in range(1,x+1):
        fila=""
        if (fil%2==1):
            numero="1"
        else:
            numero="0"
        for col in range(1,x+1):
           fila=fila+numero
        print(fila)
       
filas ()
