Radio = float (input("ingrese Radio: "))
Altura = float (input("ingrese Altura: "))

pi = 3.14

volumen = pi*(Radio**2)*Altura


if (volumen>300):
    print(volumen)
else: 
    print("valor incorrecto")