"""

ejercicio 1 

lista=[20,10,5,50,18,120,1,99,119,7]
num = 7
if num in lista:
       print("el numero 7 esta en la lista")
        
else:
       print("el numero 7 no esta en la lista")


"""
"""

import math

num=float(input("ingrese un numero: "))
raiz=math.sqrt(num)
print(raiz) 

"""

"""

import math

num=float(input("ingrese un numero : "))
raiz=math.sqrt(num)
divisible = False
for i in range (2, int(raiz)):
    if num%i == 0 :
        divisible=True
        break
if divisible==False :
    print("es primo")
else : 
    print("no es primo")

""" 
""" 

import math

num=int(input("ingrese un numero : "))
factorial=math.factorial(num)

print(f"el numero factorial de {num} es {factorial}")


"""
"""
import math 
 
num=input("ingrese el angulo en grados: ")
num=float(num.replace("°",""))
                      
seno=math.sin(math.radians(num))
coseno=math.cos(math.radians(num))
tangente=math.tan(math.radians(num))
                
print(seno,coseno,tangente)

"""
"""
palabra=str(input("ingrese una palabra: "))
letra=str(input("ingrese una letra: "))

if letra in palabra : 
    print(f"la letra{letra} forma para de la palabra {palabra} :")
    cont=palabra.count(letra)
    print(f"la letra {letra} se repite {cont} veces en la palabra {palabra}")
else:
    print(f"la letra {letra} no forma parte de la palabra {palabra}")

"""

import random
numero=random.randint(0,100)
bandera = False
while bandera != True:
    num=int(input("ingrese un numero del 1-100 "))
    print("verificando numero")
    if num==numero:
        print("felicitaciones lo adivinaste")
        bandera=True
else:
    if num>numero:
        print("el numero que ingresaste es mayor")
    else:
        print("el numero que ingresaste es menor")        