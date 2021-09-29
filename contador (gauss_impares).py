def Gauss_impares () :

    print ("contador de numeros  ")

    x = input ("hasta que numero quieres que cuente?  ")
    acum = 0
    z = 0   
    for cont in range (1 , x+1):
        resto=cont % 2

        if(resto == 0) :
            acum=acum+cont
        print (str(cont) + "acum= "+ str(acum))



Gauss_impares ()
