def mayor10 ():

       x=input("dame una edad: ")
       mayor=x
       suma=0
       for cont in range (1 ,10) :
              x=input("dame una edad:")

              if (x>mayor) :
                  mayor = x
                  suma=suma+x
       print ("el mayor="+str(mayor))

mayor10 ()




