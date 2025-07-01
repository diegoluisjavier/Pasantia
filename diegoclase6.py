"""
import matplotlib.pyplot as plt
import numpy as np
import random

x=np.random.rand(50)
y=np.random.rand(50)

print(x)
print(y)

plt.scatter(x,y)
plt.xlabel("Eje x")
plt.xlabel("Eje y")
plt.title("GRAFICOS DE PUNTOS")
plt.show()

"""
"""
import matplotlib.pyplot as plt
import random

estaciones = [  

    (
        "nombre": 'primavera', "temperaturas":[]
    ),
    (
        "nombre": 'otoño' , "temperaturas":[]
    ),
    (
        "nombre": 'invierno' , "temperaturas":[]
    ),
    (
        "nombre": 'verano' , "temperaturas":[]
    ),

]
for estacion in estaciones:
    for i in range(1,50):
        estacion("temperatura").append(random.randint(1, 30))

for estacion in estaciones:
    plt.scatter(range(1,30), estacion("temperatura"), label=estacion("nombre"))

plt.xlabel("dia")
plt.ylabel("temperatura")
plt.title("temperaturas")
plt.show()

"""

class Persona:
    def __init__(self, nombre, edad, telefono, domicilio, departamento, direccion, nota):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.domicilio = domicilio
        self.departamento = departamento
        self.direcccion = direccion
        self.nota = nota

    def __str__(self):
        return f'nombre: {self.nombre}, edad: {self.edad}, telefono: {self.telefono}, domicilio: {self.domicilio}, departamento {self.departamento}, direccion {self.direcccion}, nota {self.nota}'

    lista = []


    nombre = print("")
    edad = print("")
    telefono = print("")
    domicilio = print("")
    departamento = print("")
    direccion = print("")
    nota = print("")
    lista.append(Persona(nombre, edad, telefono, domicilio, departamento, direccion, nota))

for persona in lista:
    print(persona)