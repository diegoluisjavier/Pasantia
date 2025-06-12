def contar_pares_impares(lista):
    cantidad_pares = 0
    cantidad_impares = 0
    for numero in lista:
        if numero % 2 == 0:
            cantidad_pares += 1
        else:
            cantidad_impares += 1
    return cantidad_pares, cantidad_impares

if __name__ == '__main__':
    
    numeros_de_ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares, impares = contar_pares_impares(numeros_de_ejemplo)
    
    print("cantidad de numeros pares:", pares)
    print("cantidad de numeros impares:", impares)
