#############################################################
#                       Clase Base                          #
#############################################################
class Persona:
    def __init__(self, nombre, edad):
        # Atributos encapsulados
        self._nombre = nombre  # Encapsulamos el nombre con un guion bajo
        self._edad = edad      # Encapsulamos la edad con un guion bajo

    def mostrar_detalles(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}"

    def saludar(self):
        return f"Hola, soy {self._nombre}."


#############################################################
#                     Clase Derivada 1                      #
#############################################################
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera  # Atributo exclusivo de Estudiante

    def mostrar_detalles(self):
        # Sobrescribir el método para incluir la carrera
        return f"{super().mostrar_detalles()}, Carrera: {self.carrera}"


#############################################################
#                     Clase Derivada 2                      #
#############################################################
class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura  # Atributo exclusivo de Profesor

    def saludar(self):
        # Sobrescribir el método saludar para profesores
        return f"Hola, soy {self._nombre} y soy profesor de {self.asignatura}."


#############################################################
#                  Programa Principal                       #
#############################################################
def main():
    # Crear instancias
    persona = Persona("Carlos", 40)
    estudiante = Estudiante("Mariana", 20, "Ingeniería Informática")
    profesor = Profesor("Laura", 35, "Matemáticas")

    # Mostrar detalles de cada objeto
    print("Detalles:")
    print(persona.mostrar_detalles())
    print(estudiante.mostrar_detalles())
    print(profesor.mostrar_detalles())

    # Ejemplo de polimorfismo
    print("\nSaludos:")
    print(persona.saludar())
    print(estudiante.saludar())
    print(profesor.saludar())


if __name__ == "__main__":
    main()