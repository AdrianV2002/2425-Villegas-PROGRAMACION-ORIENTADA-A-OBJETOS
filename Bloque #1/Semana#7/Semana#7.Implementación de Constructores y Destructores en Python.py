class Persona:
    """
    Clase que representa a una persona.
    Usa un constructor para inicializar su nombre y un destructor para despedirse.
    """

    def __init__(self, nombre):
        """
        Constructor: Se ejecuta al crear una nueva persona.
        :param nombre: Nombre de la persona.
        """
        self.nombre = nombre
        print(f"¡Hola! Mi nombre es {self.nombre}.")

    def __del__(self):
        """
        Destructor: Se ejecuta automáticamente cuando se elimina el objeto.
        """
        print(f"Adiós, {self.nombre}. El objeto ha sido eliminado.")


# Programa principal
if __name__ == "__main__":
    print("Creando una persona...")
    persona1 = Persona("Adrian")  # Aquí se llama al constructor (__init__)

    print("Terminando el programa...")
    # Cuando el programa termina, el destructor (__del__) se ejecutará automáticamente.
