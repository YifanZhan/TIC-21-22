def analizador () :

        suma=0
        a=input ("dame un numero " )
        mayor=a
        menor=a
        suma=suma+a
        for cont in range ( 1 , 4 ) :
            a = input ("dame un numero " )
            if (a>mayor):
                mayor = a

            if (a<menor):
                menor= a
                suma=suma+a   
        media=suma/4.0
        print ("mayor= "+  str(mayor))
        print ("menor= " + str(menor))
        print ("media= " +str(media))

analizador( )
