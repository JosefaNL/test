import os
from datetime import datetime

# Lista global para almacenar los asientos ocupados y sus datos
asientos_ocupados = {}
asientos_pasajeros = {}

# Función para imprimir el menú
def mostrar_menu():
    print("\n------- Menú de Vuelos-Duoc -------")
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")
    print("----------------------------------")

# Función para mostrar los asientos disponibles
def mostrar_asientos():
    asientos = []
    for num in range(1, 43):
        if str(num) in asientos_ocupados:
            asientos.append("X")
        else:
            asientos.append(str(num))

    print("\n-------- Asientos disponibles --------")
    for i in range(0, len(asientos), 6):
        fila = asientos[i:i+6]
        print(" | ".join(fila))
    print("------------------------------------")

# Función para comprar un asiento
def comprar_asiento():
    global asientos_ocupados

    mostrar_asientos()
    asiento_seleccionado = input("Ingrese el número de asiento que desea comprar: ")

    if asiento_seleccionado in asientos_ocupados:
        print("El asiento seleccionado ya está ocupado. Por favor, elija otro asiento.")
        return

    nombre_pasajero = input("Ingrese el nombre del pasajero: ")
    rut_pasajero = input("Ingrese el RUT del pasajero: ")
    telefono_pasajero = input("Ingrese el teléfono del pasajero: ")
    banco_pasajero = input("Ingrese el banco del pasajero: ")

    if int(asiento_seleccionado) >= 31 and int(asiento_seleccionado) <= 42:
        precio_pasaje = 250000
    else:
        precio_pasaje = 80200

    if banco_pasajero.lower() == "banco duoc":
        precio_pasaje *= 0.85  # Aplicar 15% de descuento

    print(f"\nDatos del pasajero:")
    print(f"Nombre: {nombre_pasajero}")
    print(f"RUT: {rut_pasajero}")
    print(f"Teléfono: {telefono_pasajero}")
    print(f"Banco: {banco_pasajero}")
    print(f"Asiento seleccionado: {asiento_seleccionado}")
    print(f"Precio del pasaje: ${precio_pasaje:.2f}")

    while True:
        confirmar = input("¿Desea confirmar la compra? (s/n): ")
        if confirmar.lower() == "s":
            asientos_ocupados[asiento_seleccionado] = {
                "nombre": nombre_pasajero,
                "rut": rut_pasajero,
                "telefono": telefono_pasajero,
                "banco": banco_pasajero
            }
            print("¡Compra realizada con éxito!")
            break
        elif confirmar.lower() == "n":
            print("Compra cancelada.")
            break
        else:
            print("Respuesta inválida. Por favor, ingrese 's' o 'n'.")

# Función para anular un vuelo
def anular_vuelo():
    global asientos_ocupados

    mostrar_asientos()
    asiento_a_anular = input("Ingrese el número de asiento que desea anular: ")
    rut_pasajero = input("Ingrese el RUT del pasajero: ")

    if asiento_a_anular in asientos_ocupados and asientos_ocupados[asiento_a_anular]["rut"] == rut_pasajero:
        del asientos_ocupados[asiento_a_anular]
        print(f"El vuelo del pasajero con RUT {rut_pasajero} en el asiento {asiento_a_anular} ha sido anulado.")
    else:
        print("El asiento ingresado no está ocupado o el RUT del pasajero es incorrecto.")

# Función para modificar datos de pasajero
def modificar_datos_pasajero():
    global asientos_ocupados

    mostrar_asientos()
    asiento_a_modificar = input("Ingrese el número de asiento del pasajero: ")
    rut_pasajero = input("Ingrese el RUT del pasajero: ")

    if asiento_a_modificar in asientos_ocupados and asientos_ocupados[asiento_a_modificar]["rut"] == rut_pasajero:
        print("\n------- Modificar datos de pasajero -------")
        print("1. Modificar nombre del pasajero")
        print("2. Modificar teléfono del pasajero")
        print("3. Salir")
        print("------------------------------------------")

        opcion = input("Ingrese la opción que desea realizar: ")

        if opcion == "1":
            nuevo_nombre = input("Ingrese el nuevo nombre del pasajero: ")
            asientos_ocupados[asiento_a_modificar]["nombre"] = nuevo_nombre
            print(f"El nombre del pasajero en el asiento {asiento_a_modificar} ha sido modificado a {nuevo_nombre}.")
        elif opcion == "2":
            nuevo_telefono = input("Ingrese el nuevo teléfono del pasajero: ")
            asientos_ocupados[asiento_a_modificar]["telefono"] = nuevo_telefono
            print(f"El teléfono del pasajero en el asiento {asiento_a_modificar} ha sido modificado a {nuevo_telefono}.")
        elif opcion == "3":
            print("Saliendo del menú de modificación de datos...")
        else:
            print("Opción inválida. Intente nuevamente.")
    else:
        print("El asiento ingresado no está ocupado o el RUT del pasajero es incorrecto.")

# Función principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción que desea realizar: ")

        if opcion == "1":
            mostrar_asientos()
        elif opcion == "2":
            comprar_asiento()
        elif opcion == "3":
            anular_vuelo()
        elif opcion == "4":
            modificar_datos_pasajero()
        elif opcion == "5":
            print("\nSaliendo del sistema...")
            print(f"Nombre: Asistente Vuelos-Duoc")
            print(f"Fecha: {datetime.now().strftime('%Y-%m-%d')}")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
