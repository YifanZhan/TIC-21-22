# -*- coding: cp1252 -*-
def  bucles_while1 ():
    suma =0
    continuar="s"
    while (continuar=="s"):
        x=input (" introduce un numero: ")
        suma=suma+x
        continuar=raw_input ("quieres leer un numero más?: ")
    print("suma= " + str(suma))
            
bucles_while1  ()
