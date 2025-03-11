from colorama import Fore, Style, Back, init
init(autoreset=False)

import json

filename = 'users.json'

def guardar_usuarios():
    #Pablo/ Modifica un archivo json.

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(users, file)
    pass

def crear_base_de_datos_usuarios():
    #Pablo/ Intenta abrir un archiv json,
    # en caso de no encontraruno crea una lista vacia.
    try:
        with open(filename, encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
            return []

users = crear_base_de_datos_usuarios()

def agregar_usuario():
    #Pablo/ Agrega un nuevo usuario a la base de datos de usuarios.

    print(Fore.WHITE + Back.BLUE + "*"*(60))
    print(Fore.WHITE + Back.BLUE + " "*(60))
    print(Fore.WHITE + Back.BLUE + "Bienvenido a la base de datos de usuarios.".center(60))
    print(Fore.WHITE + Back.BLUE + " "*(60))
    print(Fore.WHITE + Back.BLUE + "*"*(60))
    
    print(Fore.WHITE + Back.BLUE + " "*(90))
    print(Fore.WHITE + Back.BLUE + "-"*(90))
    print(Fore.WHITE + Back.BLUE + "A continuación completar los datos del usuario para registrarlo en la base de datos".center(90))
    print(Fore.WHITE + Back.BLUE + "-"*(90))
    print(Fore.WHITE + Back.BLUE + " "*(90))

    print(Fore.WHITE + Back.BLUE + " "*(90))
    nombre_usuario = input(Fore.WHITE + Back.BLUE + 'Ingresa el nombre y apellido del usuario a registrar: ')
    print(Fore.WHITE + Back.BLUE + " "*(90))
    documento_usuario = input(Fore.WHITE + Back.BLUE + 'Ingresa el documento del usuario: ')
    print(Fore.WHITE + Back.BLUE + " "*(90))
    usuario = input(Fore.WHITE + Back.BLUE + 'Defina un nombre de usuario para ingresar al sistema: ')
    print(Fore.WHITE + Back.BLUE + " "*(90))
    contrasena = input(Fore.WHITE + Back.BLUE + 'Ingresa la contraseña: ')
    print(Fore.WHITE + Back.BLUE + " "*(90))
    # Anexar nuevo usuario a la lista
    users.append({
        "nombre": nombre_usuario.capitalize(),
        "documento": documento_usuario,
        "username": usuario.lower(),
        "password": contrasena
    })
    guardar_usuarios()  
    print(Fore.WHITE + Back.BLUE + "*"*(60))
    print(Fore.WHITE + Back.BLUE + " "*(60))
    print(Fore.WHITE + Back.BLUE + +f"Usuario <{usuario}> agregado con éxito".center(60)+Back.RESET)
    print(Fore.WHITE + Back.BLUE + " "*(60))
    print(Fore.WHITE + Back.BLUE + "*"*(60))

def eliminar_usuario():
    #Pablo/ Solicita que se ingresen valores, para buscarlos en una lista de usuarios y los elimina

    print(Fore.WHITE + Back.BLUE + "Eliminar usuario de la base de datos")

    if not users:
        print(Fore.WHITE + Back.BLUE + "No hay usuarios registrados.")
        return

    for indice, usuario in enumerate(users):
        print(Fore.WHITE + Back.BLUE + f"{indice + 1}. {usuario['nombre']} ({usuario['username']})")

    while True:
        try:
            usuario_a_eliminar = int(input(Fore.WHITE + Back.BLUE + "Ingrese el número del usuario a eliminar: ")) - 1
            if 0 <= usuario_a_eliminar < len(users):
                break
            else:
                print(Fore.WHITE + Back.BLUE + "Número de usuario inválido. Intente nuevamente.")
        except ValueError:
            print(Fore.WHITE + Back.BLUE + "Debe ingresar un número válido.")

    del users[usuario_a_eliminar]

    guardar_usuarios()
    print("Usuario eliminado con éxito.")
def listar_usuarios():
  #Pablo/ Muestra la lista de usuarios

    if not users:
            print(Fore.WHITE + Back.BLUE + "No hay usuarios registrados.")
            return
    else:
        print(Fore.WHITE + Back.BLUE + "Listado de usuarios:")
        for indice, usuario in enumerate(users):
            print(Fore.WHITE + Back.BLUE + f"{indice + 1}. {usuario['nombre']} ({usuario['username']})")

def acceso_sistema():
    # Pablo/ Valida las credenciales del usuario para el acceso al sistema.
    # Parámetros: usuarios: Lista de diccionarios que contienen información del usuario.
    # Cargar usuarios del archivo una sola vez

    with open('users.json', encoding='utf-8') as archivo:
     usuarios = json.load(archivo)

    intentos_restantes = 3
    
    print(Fore.WHITE + Back.BLUE + "")
    print(Fore.WHITE + Back.BLUE + "ACCESO AL SISTEMA")
    print(Fore.WHITE + Back.BLUE + "")
    pass

    while intentos_restantes > 0:
        usuario_ingresado = input(Fore.WHITE + Back.BLUE + "Ingrese su nombre de usuario: ").lower()
        contrasena_ingresada = input(Fore.WHITE + Back.BLUE + "Ingrese su contraseña: ").lower()

        usuario_valido = False
        contrasena_valida = False

        for usuario in usuarios:
            if usuario["username"].lower() == usuario_ingresado and usuario["password"] == contrasena_ingresada:
                usuario_valido = True
                contrasena_valida = True
                break  # Detener la iteración después de una coincidencia

        if usuario_valido and contrasena_valida:
            print(Fore.WHITE + Back.BLUE + "-" * (60))
            print(Fore.WHITE + Back.BLUE + " " * (60))
            print(Fore.WHITE + Back.BLUE + "¡Accediste al sistema!".center(60))
            print(Fore.WHITE + Back.BLUE + " " * (60))
            print(Fore.WHITE + Back.BLUE + "-" * (60))
            break
        else:
            intentos_restantes -= 1
            print(Fore.WHITE + Back.BLUE + f"Usuario o contraseña incorrectos. Te quedan {intentos_restantes} intentos.")

    if intentos_restantes == 0:
        print(Fore.WHITE + Back.BLUE + "x" * (60))
        print(Fore.WHITE + Back.BLUE + " " * (60))
        print(Fore.WHITE + Back.BLUE + "Se excedieron los intentos máximos. Acceso denegado.".center(60))
        print(Fore.WHITE + Back.BLUE + " " * (60))
        print(Fore.WHITE + Back.BLUE + "x" * (60))

def main_menu_usuarios():
    # Pablo/ Main del menu usuarios, muestra las opciones, solicita la eleccion de una,
    # valida que la selección sea un dato válido y ejecuta una accion, según esa opción elegida.

    while True:
        print(Fore.WHITE + Back.BLUE + " Menú Usuarios ".center(50, "-"))
        print(Fore.WHITE + Back.BLUE + "\n1. Agregar Usuario")
        print(Fore.WHITE + Back.BLUE + "2. Listar Usuarios")
        print(Fore.WHITE + Back.BLUE + "3. Eliminar usuario")
        print(Fore.WHITE + Back.BLUE + "4. Volver al menú principal")
        opc = obtener_entero("Elija una de las opciones para continuar: ")
        if opc == 1:
            agregar_usuario()
        elif opc == 2:
            listar_usuarios()
        elif opc == 3:
            eliminar_usuario()
        elif opc == 4:
            break
        else:
            print(Fore.WHITE + Back.BLUE + "Ingrese una opción válida")


