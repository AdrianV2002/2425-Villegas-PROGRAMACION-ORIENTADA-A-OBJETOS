# Sistema de Gestión de Biblioteca Digital
# Autor: [Tu Nombre]
# Descripción: Este programa permite gestionar una biblioteca digital, administrando libros, usuarios y préstamos.

class Libro:
    """
    Clase que representa un libro en la biblioteca.
    Se utilizan tuplas para los atributos inmutables (autor, título).
    """

    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo  # El título del libro (cadena)
        self.autor = autor  # El autor del libro (cadena)
        self.categoria = categoria  # Categoría del libro (cadena)
        self.isbn = isbn  # Código único del libro (cadena)

    def __str__(self):
        return f"{self.titulo} - {self.autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    """
    Clase que representa a un usuario de la biblioteca.
    Cada usuario tiene un nombre, un ID único y una lista de libros prestados.
    """

    def __init__(self, nombre, id_usuario):
        self.nombre = nombre  # Nombre del usuario
        self.id_usuario = id_usuario  # ID único del usuario
        self.libros_prestados = []  # Lista de libros prestados por el usuario

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros Prestados: {len(self.libros_prestados)}"


class Biblioteca:
    """
    Clase principal que gestiona la biblioteca digital.
    Se usa un diccionario para almacenar los libros (ISBN como clave) y un conjunto para los usuarios únicos.
    """

    def __init__(self):
        self.libros_disponibles = {}  # Diccionario de libros disponibles {ISBN: Objeto Libro}
        self.usuarios_registrados = {}  # Diccionario de usuarios {ID: Objeto Usuario}

    def agregar_libro(self, libro):
        """Añade un libro a la biblioteca."""
        if libro.isbn in self.libros_disponibles:
            print("El libro ya existe en la biblioteca.")
        else:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro agregado: {libro}")

    def eliminar_libro(self, isbn):
        """Elimina un libro de la biblioteca si está disponible."""
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario en la biblioteca."""
        if usuario.id_usuario in self.usuarios_registrados:
            print("El usuario ya está registrado.")
        else:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario}")

    def eliminar_usuario(self, id_usuario):
        """Elimina un usuario si no tiene libros prestados."""
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            if usuario.libros_prestados:
                print("El usuario no puede ser eliminado porque tiene libros prestados.")
            else:
                del self.usuarios_registrados[id_usuario]
                print(f"Usuario con ID {id_usuario} eliminado.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        """Presta un libro a un usuario si está disponible."""
        if id_usuario in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.usuarios_registrados[id_usuario]
            libro = self.libros_disponibles.pop(isbn)  # Elimina el libro de la biblioteca
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        """Devuelve un libro prestado a la biblioteca."""
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        """Busca libros por título, autor o categoría."""
        resultados = [libro for libro in self.libros_disponibles.values() if getattr(libro, criterio) == valor]
        if resultados:
            print("Resultados de la búsqueda:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, id_usuario):
        """Muestra los libros prestados a un usuario."""
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print("Usuario no encontrado.")


# Pruebas del sistema
def main():
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("1984", "George Orwell", "Ficción", "123456789")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "987654321")

    # Registrar usuarios
    usuario1 = Usuario("Juan Pérez", "U001")
    usuario2 = Usuario("María López", "U002")

    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Prestar libros
    biblioteca.prestar_libro("U001", "123456789")

    # Listar libros prestados
    biblioteca.listar_libros_prestados("U001")

    # Devolver libros
    biblioteca.devolver_libro("U001", "123456789")

    # Buscar libros por autor
    biblioteca.buscar_libro("autor", "Gabriel García Márquez")


if __name__ == "__main__":
    main()
