def mtabla():
    while True:
        try:
            n = int(input("Introduzca un número entero entre 1 y 10 para la tabla de multiplicar: "))
            if 1 <= n <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")

    while True:
        try:
            m = int(input("Introduce un número entero entre 1 y 10 para la línea de la tabla: "))
            if 1 <= m <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")

    # Nombre del archivo
    nombre_archivo = f"tabla-{n}.txt"

    try:
        # Abrir el archivo en modo de lectura
        with open(nombre_archivo, "r") as archivo:
            # Leer todas las líneas del archivo
            lineas = archivo.readlines()
            # Mostrar la línea m-1 (porque las listas empiezan en 0)
            if 1 <= m <= len(lineas):
                print(lineas[m-1].strip())
            else:
                print(f"El archivo {nombre_archivo} no tiene {m} líneas.")
    except FileNotFoundError:
        # Si el archivo no existe, mostramos un mensaje
        print(f"El archivo {nombre_archivo} no existe.")
    except Exception as e:
        # Cualquier otra excepción
        print(f"Ha ocurrido un error: {e}")

# Llamamos a la función
mtabla()
