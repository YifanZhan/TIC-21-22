def tabla () :
    print ("****----------------------------****")
    print ("*              multiplicardor         *")
    print ("****----------------------------****")
    numero = input ("dame un numero  ")
    for cont in range (0 , 21) :
        print ( str(numero)) +("x")+ (str (cont)) +( " = ") +(str(numero*cont))
    print (" Ya tienes los resultados ")

tabla ()



