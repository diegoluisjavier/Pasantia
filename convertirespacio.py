def convertirespaciado(texto):
    resultado = ""
    for letra in texto:
        resultado += letra + " "
    return resultado
if __name__ == '__main__':
    texto = (input("escribe el texto: "))
    texto_espaciado=convertirespaciado(texto)
    print(f"el texto espaciado es :{texto_espaciado}")
