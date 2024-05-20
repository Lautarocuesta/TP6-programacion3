while True:
    try:
        numero = int(input("Introduce un número entero entre 1 y 10: "))
        if numero < 1 or numero > 10:
            raise ValueError
        break
    except ValueError:
        print("Por favor, introduce un número entero válido entre 1 y 10.")

nombre_archivo = f"tabla-{numero}.txt"

try:
    with open(nombre_archivo, "r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print(f"El archivo {nombre_archivo} no se encuentra.")