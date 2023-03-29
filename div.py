#Programa para deducir cuando un numero es divisible entre 5

print("--------------------------------------")
print("-----------BIENVENIDO-----------------")
print("--------------------------------------")

#INPUT

A= int(input("Ingrese el valor: "))

import math

A % 5 == 0

#PROCESSING

if A % 5 == 0:
    rta=A, "El numero es divisible entre 5"
    rt= A/5
else:
    rta="El numero no es divisible entre 5"

#OUTPUT

print("------------------------------------")
print(rta)
print("Su resultado es: "+str(rt))
print("---------------FIN------------------")