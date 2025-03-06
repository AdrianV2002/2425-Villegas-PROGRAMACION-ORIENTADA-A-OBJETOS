import math

# Programa para calcular el área de un círculo
def calcular_area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo dado su radio.
    :param radio: Radio del círculo (float)
    :return: Área del círculo (float)
    """
    return math.pi * radio ** 2

# Solicitar al usuario el radio del círculo
radio_usuario = float(input("Ingrese el radio del círculo: "))

# Calcular el área
area = calcular_area_circulo(radio_usuario)

# Mostrar el resultado
print(f"El área del círculo con radio {radio_usuario} es: {area:.2f}")

# Variable booleana para verificar si el área es mayor a un valor específico
es_area_grande = area > 50
print(f"¿El área es mayor a 50? {es_area_grande}")
