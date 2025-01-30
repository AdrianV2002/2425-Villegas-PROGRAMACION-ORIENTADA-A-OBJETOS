import os
import subprocess
import pyfiglet
from colorama import Fore, Style


def limpiar_consola():
    print("\n" * 100)

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            limpiar_consola()
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        limpiar_consola()
        print(Fore.RED + "El archivo no se encontró.")
        return None
    except Exception as e:
        limpiar_consola()
        print(Fore.RED + f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': 'Bloque #1',
        '2': 'Bloque #2'
    }

    while True:
        textomenu = pyfiglet.figlet_format("Menu Principal", font="cybermedium")
        print(Fore.LIGHTMAGENTA_EX + textomenu)
        print(Fore.GREEN + "Selecciona una Carpeta para ver su contenido." + Style.RESET_ALL)
        print("")
        # Imprime las opciones del menú principal
        for key in unidades:
            print(f"{Fore.CYAN}{key} - {Fore.LIGHTCYAN_EX}{unidades[key]}{Style.RESET_ALL}")
        print(Fore.RED + "0 - " + Fore.LIGHTRED_EX + "Salir" + Style.RESET_ALL)

        eleccion_unidad = input(Fore.RED + "Elige una unidad o '0' para salir: " + Style.RESET_ALL)
        if eleccion_unidad == '0':
            limpiar_consola()
            print(Fore.RED + "Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        limpiar_consola()
        textosubmenu = pyfiglet.figlet_format("SubCarpeta", font="cybermedium")
        print(Fore.LIGHTMAGENTA_EX + textosubmenu)
        print(Fore.GREEN + "Selecciona una SubCarpeta para ver su contenido.")
        print("")
        # Imprime las subcarpetas
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{Fore.CYAN}{i} - {Fore.LIGHTCYAN_EX}{carpeta}{Style.RESET_ALL}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            limpiar_consola()
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        limpiar_consola()
        textoscript = pyfiglet.figlet_format("Scripts", font="cybermedium")
        print(Fore.LIGHTMAGENTA_EX + textoscript)
        print(Fore.GREEN + "Selecciona un Script para ejecutarlo.")
        print("")
        # Imprime los scripts
        for i, script in enumerate(scripts, start=1):
            print(f"{Fore.CYAN}{i} - {Fore.LIGHTCYAN_EX}{script}{Style.RESET_ALL}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == '0':
            limpiar_consola()
            break
        elif eleccion_script == '9':
            limpiar_consola()
            return  # Regresar al menú principal
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()