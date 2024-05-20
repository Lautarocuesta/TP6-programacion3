import os

def crear_archivo_listin():
    """Crear el archivo listin.txt si no existe."""
    if not os.path.exists("listin.txt"):
        with open("listin.txt", "w") as archivo:
            pass  # Crear el archivo vacío

def consultar_telefono():
    """Consultar el teléfono de un cliente."""
    nombre_cliente = input("Introduce el nombre del cliente: ")
    encontrado = False
    with open("listin.txt", "r") as archivo:
        for linea in archivo:
            nombre, telefono = linea.strip().split(",")
            if nombre.lower() == nombre_cliente.lower():
                print(f"Teléfono de {nombre}: {telefono}")
                encontrado = True
                break
    if not encontrado:
        print(f"Cliente {nombre_cliente} no encontrado.")

def anadir_cliente():
    """Añadir el teléfono de un nuevo cliente."""
    nombre_cliente = input("Introduce el nombre del nuevo cliente: ")
    telefono_cliente = input("Introduce el teléfono del nuevo cliente: ")
    with open("listin.txt", "a") as archivo:
        archivo.write(f"{nombre_cliente},{telefono_cliente}\n")
    print(f"Cliente {nombre_cliente} añadido con éxito.")

def eliminar_cliente():
    """Eliminar el teléfono de un cliente."""
    nombre_cliente = input("Introduce el nombre del cliente a eliminar: ")
    encontrado = False
    with open("listin.txt", "r") as archivo:
        lineas = archivo.readlines()
    with open("listin.txt", "w") as archivo:
        for linea in lineas:
            nombre, telefono = linea.strip().split(",")
            if nombre.lower() == nombre_cliente.lower():
                encontrado = True
            else:
                archivo.write(linea)
    if encontrado:
        print(f"Cliente {nombre_cliente} eliminado con éxito.")
    else:
        print(f"Cliente {nombre_cliente} no encontrado.")

def mostrar_menu():
    """Mostrar el menú de opciones."""
    print("\nGestión del Listín Telefónico")
    print("1. Crear archivo listin.txt")
    print("2. Consultar teléfono de un cliente")
    print("3. Añadir teléfono de un nuevo cliente")
    print("4. Eliminar teléfono de un cliente")
    print("5. Salir")

def main():
    crear_archivo_listin()  # Asegurarse de que el archivo existe
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")
        if opcion == "1":
            crear_archivo_listin()
            print("Archivo listin.txt creado/verificado.")
        elif opcion == "2":
            consultar_telefono()
        elif opcion == "3":
            anadir_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

# Llamamos a la función principal
if __name__ == "__main__":
    main()
