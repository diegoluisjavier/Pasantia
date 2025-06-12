def CalcularMaxMin(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo
    
if __name__ == '__main__':
    lista = []
    cantidad = int(input("ingresar numeros para la tabla: "))
    for i in range(cantidad):
        numero = float(input(f"ingrese el numero{i+1}: "))
        lista.append(numero)
        
    maximo, minimo = CalcularMaxMin(lista)
    print(f"el numero maximo de la tabla es{maximo}: ")
    print(f"el numero minimo de la tabla es{minimo}: ")





