class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible
        self.precio = precio  # Precio del producto

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_datos()

    def guardar_datos(self):
        with open(self.archivo, "w") as file:
            for producto in self.productos:
                file.write(f"{producto.id_producto} | Nombre: {producto.nombre} | Cantidad: {producto.cantidad} | Precio: ${producto.precio}\n")

    def cargar_datos(self):
        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id_producto, nombre, cantidad, precio = datos
                        self.productos.append(Producto(id_producto, nombre, int(cantidad), float(precio)))
        except FileNotFoundError:
            self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_datos()

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)

    def eliminar_producto(self, id_producto):
        pass


def menu():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (deje en blanco para no cambiar): ")
            nuevo_precio = input("Nuevo precio (deje en blanco para no cambiar): ")

            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()