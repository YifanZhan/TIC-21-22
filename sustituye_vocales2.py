def sustituye_vocales2 ():

        palabra=raw_input ("dame una palabra: ")
        letra = raw_input ("que  vocal quieres cambiar. " )
        cont=0
        yes= raw_input (" ")
        len (palabra)
        while (cont<len(palabra)):
                if(palabra[cont]== "a"):
                        print (letra)
                else:
                     if (palabra[cont]=="e"):
                                print (letra)
                     else:
                            if (palabra[cont]=="i"):
                                       print (letra)
                            else:
                                if (palabra[cont]=="o"):
                                        print (letra)
                                else:
                                        if(palabra[cont]=="u"):
                                                print(letra)
                                        else:  
                                               print(palabra[cont])
                cont=cont+1
        print ("has escrito: "+ palabra)




sustituye_vocales2 ()
