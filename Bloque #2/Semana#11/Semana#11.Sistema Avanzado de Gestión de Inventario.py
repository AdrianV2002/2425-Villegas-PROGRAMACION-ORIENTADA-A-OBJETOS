import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        self.precio = precio

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(data["id_producto"], data["nombre"], data["cantidad"], data["precio"])


class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_datos()

    def guardar_datos(self):
        try:
            with open(self.archivo, "w") as file:
                json.dump({id_p: p.to_dict() for id_p, p in self.productos.items()}, file, indent=4)
            print("Datos guardados exitosamente.")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def cargar_datos(self):
        try:
            with open(self.archivo, "r") as file:
                datos = json.load(file)
                self.productos = {id_p: Producto.from_dict(p) for id_p, p in datos.items()}
            print("Datos cargados exitosamente.")
        except (FileNotFoundError, json.JSONDecodeError):
            print("No se encontró el archivo o está vacío. Se creará uno nuevo al guardar.")

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_datos()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_datos()
            print(f"Producto {id_producto} eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].actualizar_precio(nuevo_precio)
            self.guardar_datos()
            print("Producto actualizado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(f"ID: {producto.id_producto} | Nombre: {producto.nombre} | Cantidad: {producto.cantidad} | Precio: ${producto.precio:.2f}")


def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario ---")
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
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for producto in resultados:
                    print(f"ID: {producto.id_producto} | Nombre: {producto.nombre} | Cantidad: {producto.cantidad} | Precio: ${producto.precio:.2f}")
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