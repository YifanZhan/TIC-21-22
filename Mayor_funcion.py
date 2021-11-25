def delvolver_el_mayor2 (num1,num2,num3):

       if(num1>num2):
              mayor=num1

       if(num2>num1):
              mayor=num2

       if(num2>num3):
              mayor=num2

       if(num3>num2):
              mayor=num3

       if(num1>num3):
              mayor=num1

       if(num3>num1):
              mayor=num3

       print (mayor)

def numero6 ():
       num1=input ("dame un numero: ")
       num2=input ("dame el segundo numero: ")
       num3=input ("dame el tercer numero: ")
       return(delvolver_el_mayor2(num1,num2,num3))

numero6 ()
