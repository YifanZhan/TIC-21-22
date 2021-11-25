def palabra_3 ():

    nombre=raw_input("dame su nombre: ")
    apellido=raw_input("dame el apellido:  ")
    print (" buenos dias "  + nombre+"  "+apellido)
    print (" Tu nombre empieza por la letra "+nombre [0])
    print (" voy a deletrear tu nombre ")   
    for cont in range (0, 15):
        print (nombre[cont])
palabra_3 ()
