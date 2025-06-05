""" 
num1 = int(input("Ingrese el primer número entero positivo: "))
num2 = int(input("Ingrese el segundo número entero positivo: "))
num3 = int(input("Ingrese el tercer número entero positivo: "))


if num1 > 0 and num2 > 0 and num3 > 0:
    print("el cubo del primero numero es : ",num1**3)
    print("el cubo del segundo numero es : ",num2**3)
    print("el cubo del tercer numero es : ",num3**3)
else:
    print("los números deben ser positivos.")
"""


""" 

import random

num1 = (random.randint(0, 10))
num2 = (random.randint(0, 10))
num3 = (random.(0, 10))
num4 = (random.(0, 10))
num5 = (random.(0, 10))

suma=0 
"""

"""
numeros = input("Ingresa cinco números separados por espacio: ")

lista_numeros = list(map(int, numeros.split()))

if len(lista_numeros) != 5:
    print("Debes ingresar exactamente cinco números.")
else:
    menor = min(lista_numeros)
    mayor = max(lista_numeros)
    print(f"El menor número es el {menor}")
    print(f"El mayor número es el {mayor}")

"""
"""
numeros = []
suma = 0
pares = 0
impares = 0

for i in range (6):
    numero = int(input("ingrese un numero: "))
    numeros.append(numero)
    suma += numero

    if numero % 2 ==0 :
       pares += 1
    else:
       impares += 1
    promedio = suma / 6

print("los numeros pares son: " ,pares)
print("los numeros impares son;: " ,impares)
print("el promedio total es: " ,promedio )

"""