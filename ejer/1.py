def tablamultiplicar():
    while True:
        try:
            n = int(input("Introduzca un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    # Nombre del archivo
    nombre = f"tabla-{n}.txt"

    # Abrimos el archivo en modo de escritura
    with open(nombre, 'w') as archivo:
        # Escribimos la tabla de multiplicar en el archivo
        for i in range(1, 11):
            archivo.write(f"{n} x {i} = {n * i}\n")

    print(f"La tabla de multiplicar del {n} ha sido guardada en {nombre}")

tablamultiplicar()
