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





# Programación Orientada a Objetos (POO)

class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for dia in range(7):
            temp = float(input(f"Ingresa la temperatura del día {dia + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Ejecución del programa orientado a objetos
def programa_poo():
    print("Programación Orientada a Objetos: Calculo del Promedio Semanal del Clima")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f} grados.")

programa_poo()