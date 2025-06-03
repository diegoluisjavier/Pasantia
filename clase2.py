lado1 =float (input("ingrese el lado1 "))
lado2 =float (input("ingrese el lado2 "))
lado3 =float (input("ingrese el lado3 "))


if lado1==lado2==lado3:
   print("el triangulo  es equilatero")
elif lado1 ==lado2 or lado1==lado3 or lado2 == lado3:
   print("el triangulo es isoceles")
else :
    print("el triangulo es escaleno")
 