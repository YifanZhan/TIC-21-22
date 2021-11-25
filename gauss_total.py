def Gauss_impares () :

    print ("contador de numeros:  ")

    x = input ("hasta que numero quieres que cuente: ?  ")
    suma_par = 0
    suma_impar = 0
    suma_total = 0
    resto = 0
    for cont in range (1 , x+1):
        resto= cont % 2
    suma_total=suma_total+cont
    if (resto == 0) :
            suma_par=suma_par+cont
    else :
            suma_impar=_impar+cont
            
            
    
    print (str(cont) + " pares= "+ str(suma_par) + " impar=" +str(suma_impar))

    print (" la suma de los pares=  " + str(suma_par))
    print(" la suma de los impares= "+str(suma_impar))
    print (" la suma total= " +str(suma_total))
    
Gauss_impares ()
