def fechas ():
        
        fechas= raw_input ("introduceme una fecha (dd/mm/aa):  ")
        meses="Enero,Febrero,Marzo,Abril,Mayo,Junio,Julio,Agosto,Septiembre,Octubre,Noviembre,dicciembre"
        numero=int ( fechas [3] ) *10+int ( fechas [4] )
        mes_elegido
        cont=0
        numero_comas=0
        print(numero)
        while (numero_comas<=numero-1) :
                if (meses[cont]==","):
                        numero_comas=numero_comas+1
                cont=cont+1
        print (cont)
                      

fechas ()
