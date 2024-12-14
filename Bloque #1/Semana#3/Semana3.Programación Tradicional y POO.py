# Programación Tradicional
def ingresar_temperaturas():
    temperaturas = []
    for dia in range(7):
        temp = float(input(f"Ingresa la temperatura del día {dia + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Ejecución del programa tradicional
def programa_tradicional():
    print("Programación Tradicional: Calculo del Promedio Semanal del Clima")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f} grados.")

programa_tradicional()
