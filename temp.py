def calcular_Temp(temp_max, temp_min):
    return (temp_max + temp_min) / 2
    
if __name__ == '__main__':
    cont = 0
   
    cant_dias=int(input("Ingrese la cantidad de días: "))
   
    for i in range(cant_dias):
        cant_dias=+1
        print(f"Dia {i+1}")
        
        temp_max = float(input(f"Ingrese la temperatura máxima: "))
        temp_min = float(input(f"Ingrese la temperatura mínima: "))  

        temp_media = calcular_Temp(temp_max, temp_min)
        print(f"La temperatura media del día {i+1} fue {temp_media}°")

       