
from colorama import Fore, Style, Back, init
init(autoreset=False)

import json


filerese='lista_reservas.json'
def carga_reservas():
    with open(filerese) as fire:
        lista_reservas=json.load(fire)
        
    return lista_reservas

def guardar_reservas(lista_reservas):
    with open(filerese, 'w') as fire:
        json.dump(lista_reservas,fire)

def obtener_habitacion(mensaje):
    # Matias/ Solicita que se ingrese una cantidad de habitaciones a utilizar y valida el formato del dato ingresado.
    # Parámetros: mensaje: cadena de caracteres que se muestra al usuario. 
    # Retorno: cantidad : tipo de dato entero.

    while True:
        try:
            cantidad = int(input(Fore.WHITE + Back.BLUE + mensaje))
            if cantidad >= 0:
                print(Fore.WHITE + Back.BLUE + "Datos ingresados de manera exitosa.")
                return cantidad
            else:
                print(Fore.WHITE + Back.BLUE + "Ingrese una cantidad válida")
        except ValueError:
            print(Fore.WHITE + Back.BLUE + "El dato ingresado no es correcto.")


def obtener_dni(mensaje):
    # Matias/ Solicita al usuario que ingrese un dni, valida si es un dato de tipo entero y que tenga mas de 8 caracteres.
    # Parámetros: mensaje: cadena de caracteres que se muestra al usuario.
    # Retorno: dni: dato de tipo entero.

    while True:
        try:
            dni = int(input(Fore.WHITE + Back.GREEN + mensaje))
            if 8 <= len(str(dni)):
                print(Fore.WHITE + Back.BLUE + "Datos ingresados de manera exitosa.")
                return dni
            else:
                print(Fore.WHITE + Back.BLUE + "El DNI debe tener 8 dígitos.")
        except ValueError:
            print(Fore.WHITE + Back.BLUE + "El dato ingresado no es correcto.")

def obtener_entero(mensaje):
    # Matias/ Solicita al usuario que ingrese un dato, y valida si es un dato de tipo entero.
    # Parámetros: mensaje: cadena de caracteres que se muestra al usuario.
    # Retorno: dato: dato de tipo entero.
    while True:
        try:
            dato = int(input(Fore.WHITE + Back.BLUE + mensaje))
            return dato
        except ValueError:
            print(Fore.WHITE + Back.BLUE + "El dato ingresado no es correcto.")

def menu_ver_reserva():
    # Matias/ Imprime las opciones del menú ver reservas.

    print(Fore.WHITE + Back.BLUE + " ")
    print(Fore.WHITE + Back.BLUE + " Menú Ver Reserva ".center(50, "-"))
    print(Fore.WHITE + Back.BLUE + "\n1. Ver todas las reservas")
    print(Fore.WHITE + Back.BLUE + "2. Ver una reserva")
    print(Fore.WHITE + Back.BLUE + "3. Volver al menú anterior")

def ver_todas_reservas(lista_reservas):
    # Matias/ Imprime la lista de reservas completa.
    
    print(Fore.WHITE + Back.BLUE + "Ver todas las reservas".center(50, "-"))
    for reserva in lista_reservas:
        
        print(Fore.WHITE + Back.BLUE + f"\nNombre: {reserva['nombre']}")
        print(Fore.WHITE + Back.BLUE + f"DNI: {reserva['dni']}")
        print(Fore.WHITE + Back.BLUE + f"Fecha de Ingreso: {reserva['fecha_ingreso']}")
        print(Fore.WHITE + Back.BLUE + f"Fecha de Salida: {reserva['fecha_salida']}")
        print(Fore.WHITE + Back.BLUE + f"Cantidad de Noches: {reserva['cantidad_noches']}")
        print(Fore.WHITE + Back.BLUE + f"Cantidad de Huespedes: {reserva['cantidad']}")
        print(Fore.WHITE + Back.BLUE + "Datos de los Huespedes:")
        for huesped in reserva['datos_huespedes']:
            print(Fore.WHITE + Back.BLUE + f"   Nombre: {huesped['nombre']}, DNI: {huesped['dni']}")
                               
        print(Fore.WHITE + Back.BLUE + f"Habitaciones Dobles: {reserva['cantidad_dobles']}")
        print(Fore.WHITE + Back.BLUE + f"Habitaciones Triples: {reserva['cantidad_triples']}")
        print(Fore.WHITE + Back.BLUE + f"Monto Total: ${reserva['monto']}")
    print(Fore.WHITE + Back.BLUE + "-" * 50)

def ver_reserva_unica(lista_reservas):
    # Matias/ Solicita que se ingrese un dni, valida el formato e imprime las reservas de la lista de reservas, que coincidan con el dni.
    encontrado=False
    print(Fore.WHITE + Back.BLUE + "Ver reserva única".center(50, "-"))
    dni = obtener_dni("Ingrese DNI del cliente para ver la reserva: ")
    print(f"el dni es: {dni}")
    for reserva in lista_reservas:
        if reserva["dni"] == dni:
            print(Fore.WHITE + Back.BLUE + f"\nNombre: {reserva["nombre"]}")
            print(Fore.WHITE + Back.BLUE + f"DNI: {reserva["dni"]}")
            print(Fore.WHITE + Back.BLUE + f"Fecha de Ingreso: {reserva['fecha_ingreso']}")
            print(Fore.WHITE + Back.BLUE + f"Fecha de Salida: {reserva['fecha_salida']}")
            print(Fore.WHITE + Back.BLUE + f"Cantidad de Noches: {reserva['cantidad_noches']}")
            print(Fore.WHITE + Back.BLUE + f"Cantidad de Huespedes: {reserva['cantidad']}")
            print(Fore.WHITE + Back.BLUE + "Datos de los Huespedes:")
            for huesped in reserva['datos_huespedes']:
                print(Fore.WHITE + Back.BLUE + f"   Nombre: {huesped['nombre']}, DNI: {huesped['dni']}")
            
            print(Fore.WHITE + Back.BLUE + f"Habitaciones Dobles: {reserva['cantidad_dobles']}")
            print(Fore.WHITE + Back.BLUE + f"Habitaciones Triples: {reserva['cantidad_triples']}")
            print(Fore.WHITE + Back.BLUE + f"Monto Total: ${reserva['monto']}")
            print(Fore.WHITE + Back.BLUE + "-" * 50)
            encontrado=True
            break
    if encontrado:
        print("datos encontrados satisfactoriamente")
    else:
        print(Fore.WHITE + Back.BLUE + "Reserva no encontrada.")
def main_ver_reserva(lista_reservas):
    # Matias/ Main del menu ver reservas, muestra las opciones, solicita la eleccion de una,
    # valida que la selección sea un dato válido y ejecuta una accion, según esa opción elegida.

    while True:
        menu_ver_reserva()
        opc = obtener_entero("Elija una de las opciones para continuar: ")
        lista_reservas=carga_reservas()
        if opc == 1:
            
            ver_todas_reservas(lista_reservas)
        elif opc == 2:
            ver_reserva_unica(lista_reservas)
        elif opc == 3:
            print(Fore.WHITE + Back.BLUE + "Volviendo al menú anterior...")
            break
        else:
            print(Fore.WHITE + Back.BLUE + "Ingrese una opción válida")