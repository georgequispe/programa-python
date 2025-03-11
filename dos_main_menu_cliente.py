
lista_huesped=[] #Lista para almacenar clientes.

from colorama import Fore, Style, Back, init
init(autoreset=False)
import json
import time
filehuesped='lista_huesped.json'
filehabi='lista_habitaciones.json'
from cuatro_habitaciones import obtener_habitacion,seleccionar_habitaciones,modificar_estado_habitacion
def carga_huesped():
    with open(filehuesped) as fihu:
        lista_huesped=json.load(fihu)
    return lista_huesped

def guardar_huesped(lista_huesped):
    with open(filehuesped, 'w') as fihu:
        json.dump(lista_huesped,fihu)

def carga_habitaciones():
    with open(filehabi) as fiha:
        lista_habitaciones=json.load(fiha)
    return lista_habitaciones


def confirmacion(mensaje):
    # Matias/ Esta funcion le pregunta al usuario si desea continuar o no .
    # Parámetros: mensaje: cadena de caracteres que se muestra al usuario.
    # Retorno: opcion: dato de tipo cadena de caracteres.

    while True:
        opcion = input(Fore.WHITE + Back.BLUE + f"{mensaje} (s/n): ").lower()
        if opcion in ['s', 'n']:
            print(Fore.WHITE + Back.BLUE + "Datos ingresados de manera exitosa.")
            return opcion == 's'
        print(Fore.WHITE + Back.BLUE + "El dato ingresado no es correcto.")



def obtener_dni(mensaje):
    # Matias/ Solicita al usuario que ingrese un dni, valida si es un dato de tipo entero y que tenga mas de 8 caracteres.
    # Parámetros: mensaje: cadena de caracteres que se muestra al usuario.
    # Retorno: dni: dato de tipo entero.

    while True:
        try:
            dni = int(input(Fore.WHITE + Back.BLUE + mensaje))
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
def validar_dato(nombre):
  # George/ Solicita al usuario que ingrese un dato, y valida si es un dato es un string con mas de tres caracteres.
  # Parámetros: nombre: cadena decaracteres que ingresa el usuario.
  # Retorno: nombre: dato de tipo cadena de caracteres.

    escibir_bien=True
    while escibir_bien:
        if len(nombre)>=3 :
            escibir_bien=False
            return nombre
            
        else:
            print(Fore.WHITE+Back.BLUE+ "El nombre es con letras y sin espacio, ingrese nuevamente ")

def validar_dni(dni):
  # George/ Valida que el parametro ingresado tenga mas de 8 caracteres.
  # Parámetros: dni: dato de tipo entero.
  # Retorno: dni: dato de tipo entero.

    numero_bien=True
    while numero_bien:
        try:#recibe el dni en digitos y lo convieerte en strig
            if 8<=len(str(dni)):
                numero_bien=False
                return dni
                
            else:
                print(Fore.WHITE+Back.BLUE+"el documento es de 8 digitos y sin espacio/punto")
                dni=int(input(Fore.WHITE+Back.BLUE+"ingrese su documento: "))
        except ValueError:
            print(Fore.WHITE+Back.BLUE+"dato incorrecto, ingrese numeros de 8 digitos, sin espacios")


def crear_cliente(lista_huesped):
    # George/ Solicita datos, los guarda en un diccionario y los almacena en la lista de clientes.
               
    print(Fore.WHITE+Back.BLUE+"Ingrese los datos del huesped.")

    nombre=input(Fore.WHITE+Back.BLUE+"Ingrese su nombre: ")
    validar_dato(nombre)
     
    dni=input(Fore.WHITE+Back.BLUE+"Ingrese su documento: ")
    validar_dni(dni)
    dni= int(dni) #convierte el dni en digitos para guardae en el diccionario       
    direccion=input(Fore.WHITE+Back.BLUE+"Ingrese su dirección: ")
    celular=int(input(Fore.WHITE+Back.BLUE+"Ingrese su celular: "))
    cantidad_noches = obtener_entero("Ingrese la cantidad de noches: ")
    habitacion_doble = obtener_habitacion("Ingrese la cantidad de habitaciones dobles que desea utilizar: ")
    habitacion_triple = obtener_habitacion("Ingrese la cantidad de habitaciones triples que desea utilizar: ")
    cantidad_habitaciones = habitacion_doble + habitacion_triple
    lista_habitaciones=carga_habitaciones()
    if habitacion_doble>0:
        tipo="doble"
    else:
        tipo="triple"
    numero_hab=seleccionar_habitaciones(lista_habitaciones,dni, tipo)
    #mando numero de habitacion que elijo y el estado libre, para que ponga en ocupado
    modificar_estado_habitacion(lista_habitaciones,numero_hab,dni,'ocupado')
    
    datos_huesped={
        "nombre":nombre,
        "dni":dni,
        "direccion":direccion,
        "cantidad_noches": cantidad_noches,
        "numero_hab": numero_hab,
        "cantidad_habitaciones": cantidad_habitaciones,
        "cantidad_dobles":habitacion_doble,
        "cantidad_triples":habitacion_triple, 
        "celular":celular,
    }
    
    lista_huesped.append(datos_huesped)
    print (Fore.WHITE+Back.BLUE+ "Huesped creado exitosamente")
    guardar_huesped(lista_huesped)
    return lista_huesped  #retorno una lista con diccionarios de huespedes
    

def eliminar_huesped(lista_huesped,lista_habitaciones):
    # elimina el cliente que se retira del hotel y en la lista habitacion
    # nuevamente se posiciona en 'libre'. 
    print(Fore.WHITE + Back.BLUE + "Eliminar Huesped".center(50))
    sigo=True
    while sigo:
        
        dni = obtener_dni("Ingrese DNI del cliente a eliminar: ")
        esta = buscar_dato_lista_huesped(lista_huesped,dni)
        if esta:            
            for i,huesped in enumerate(lista_huesped):
                print(Fore.WHITE + Back.YELLOW +f"{i}. '{huesped['nombre']}'numero de habi:'{huesped['numero_hab']}'")
                indice = obtener_entero("Introduce el número del huesped a eliminar: ")
                modificar_estado_habitacion(lista_habitaciones,huesped['numero_hab'],dni,"libre")
                break
                        
            
            lista_huesped.remove(lista_huesped[indice])
            print(Fore.WHITE + Back.BLUE + "Cliente Eliminado con Éxito.")
            sigo=False
        else:
            print(Fore.WHITE + Back.BLUE + "huesped no encontrado")
            
            

def buscar_dato_lista_huesped(lista_huesped,valor):
    # Matias/ Busca un valor dentro de los diccionarios en la lista de clientes, te retorna sí se halló y una copia del diccionario relacionado al valor.
    # Parámetros: valor: dato a buscar.
    # Retorno: True/ False: dato de tipo bool. cliente: variable tipo diccionario.

    for cliente in lista_huesped:
        if valor in cliente.values():
            return True
    return False   

def mostrar_cliente(lista_huesped,lista_habitaciones):
    # George/ Muestra la lista de los clientes cargados alojados en el hotel.    
    print(Fore.WHITE + Back.BLUE +"LISTA DE CLIENTES".center(50)) 
    
    for datos in lista_huesped:        
        print(Fore.WHITE + Back.BLUE +"*"*50)                      
        print(Fore.WHITE + Back.BLUE +f"\nNombre: {datos['nombre'].title()}")
        print(Fore.WHITE + Back.BLUE +f"Dni:{datos['dni']}")
        print(Fore.WHITE + Back.BLUE +f"Dirección:{datos['direccion'].capitalize()}")
        print(Fore.WHITE + Back.BLUE +f"Cantidad de noches:{datos['cantidad_noches']}")
        print(Fore.WHITE + Back.BLUE +f"numero de habitacion:{datos['numero_hab']}")
        print(Fore.WHITE + Back.BLUE +f"Cantidad de habitaciones:{datos['cantidad_habitaciones']}")
        print(Fore.WHITE + Back.BLUE +f"Cantidad de dobles:{datos['cantidad_dobles']}")             
        print(Fore.WHITE + Back.BLUE +f"Cantidad de triples:{datos['cantidad_triples']}")
        print(Fore.WHITE + Back.BLUE +f"Celular:{datos['celular']}")
                                        
        
def buscar_huesped(lista_huesped,dni):
    # Geroge/ Busca un dni dentro de los diccionarios en la lista de clientes

    return[huesped for huesped in lista_huesped if huesped['dni']==dni]

def elegir_opcion_modificar():
    # Geroge/ Menú de opciones a elegir, para modificar los datos de los diccionarios de la lista de clientes.
    # Retorno: la opcion elegida.

    print(Fore.WHITE + Back.BLUE + f"¿Que datos desea modificar? ")
    print(Fore.WHITE + Back.BLUE +"Ingrese una opcion para continuar o 'listo' para terminar" )
    new_dato=input(Fore.WHITE + Back.BLUE +"para el nombre ingrese (n)\
                            \npara la dirección ingrese (d)\
                            \npara el celular (l)\
                            \npara el documento ingrese (o)\
                            \npara terminar (listo)\
                            \n: ")
    if new_dato.isalpha():
        encontrado=True
    else:
        print(Fore.WHITE + Back.BLUE +"ingreso dato incorrecto")
    time.sleep(2)
    return new_dato  

def modificar_huesped(lista_huesped):
    # Geroge/ Toma la opcion elegida en otra funcion y modifica los datos de los diccionarios de la lista de clientes, segun esa opcion.    

    dni= int(input(Fore.WHITE + Back.BLUE +"Ingrese el DNI del huesped: ") )

    try:
        new_dato=elegir_opcion_modificar()

    except UnboundLocalError:
        print(Fore.WHITE + Back.BLUE +"Ingresó un dato incorrecto")
    except ValueError:
        print(Fore.WHITE + Back.BLUE +"Ingrese una letra")                                                                                  
    for huesped in lista_huesped:
            if huesped["dni"]==dni:               
                print  (Fore.WHITE + Back.BLUE +"Huesped hallado")                                      
                if new_dato=="n":#en el caso que el cliente cambie por otro que va a venir en su reemplazo
                        name_0=input(Fore.WHITE + Back.BLUE +"ingrese el nuevo nombre: ")
                        nombre=validar_dato(name_0)                            
                        print(Fore.WHITE + Back.BLUE + f"Nombre anterior {huesped['nombre'].title()} y su nuevo nombre es:{nombre.title()}")
                        huesped['nombre']=nombre                        
                        break
                elif new_dato=="d":
                        dir=input(Fore.WHITE + Back.BLUE +"ingrese la nueva dirección: ")
                        print(Fore.WHITE + Back.BLUE +f"Dirección anterior: {huesped['direccion']} y su nueva dirección es:{dir}")
                        huesped['direccion']=dir
                        break                 
                elif new_dato=="l":
                        cellphone=input(Fore.WHITE + Back.BLUE +"ingrese el nuevo numero de telefono: ")                
                        huesped['celular']=cellphone
                        print(Fore.WHITE + Back.BLUE +f"Su nuevo número {cellphone} fue agregado")
                        break                       
                elif new_dato=="o":
                        
                         document=int(input(Fore.WHITE + Back.BLUE +"ingrese el nuevo documento: "))                        
                         validar_dni(document)
                         huesped['dni']=document
                         print(Fore.WHITE + Back.BLUE +f"{Fore.GREEN}Su dni {document} fue modificado")
                         break                                                                                                                  
                elif new_dato=="listo":
                        break
                else:
                        print(Fore.WHITE + Back.BLUE +"ingreso un opcion invalida")
                                                 
            
            else:
                print(Fore.WHITE + Back.BLUE +"Cliente no encontrado")
        
    time.sleep(2)                            
    
    return lista_huesped
    
def main_menu_cliente():
    # Geroge/ Main del menu cliente, muestra las opciones, solicita la eleccion de una,
    # valida que la selección sea un dato válido y ejecuta una accion, según esa opción elegida.

    print()    
    lista_huesped=carga_huesped()
    lista_habitaciones=carga_habitaciones()
    while True:
        print(Fore.WHITE + Back.BLUE + " Menú Clientes ".center(50, "-"))
        print(Fore.WHITE + Back.BLUE + "\n1. Agregar Cliente")
        print(Fore.WHITE + Back.BLUE + "2. Modificar Cliente")
        print(Fore.WHITE + Back.BLUE + "3. Mostrar Clientes")
        print(Fore.WHITE + Back.BLUE + "4. Eliminar Cliente")
        print(Fore.WHITE + Back.BLUE + "5. Volver al Menú Principal")
        opcion = obtener_entero("Elija una de las opciones para continuar: ")
        
        if opcion== 1:
            lista_huesped=crear_cliente(lista_huesped)
            guardar_huesped(lista_huesped)      
        elif opcion== 2:
            modificar_huesped(lista_huesped)    
            guardar_huesped(lista_huesped)
        elif opcion== 3:
            lista_huesped=carga_huesped()
            mostrar_cliente(lista_huesped,lista_habitaciones)
        elif opcion== 4:
            eliminar_huesped(lista_huesped,lista_habitaciones)
            guardar_huesped(lista_huesped)           
        elif opcion== 5:
            print(Fore.WHITE + Back.BLUE + "Volviendo al menú principal...")
            break
        else:
            print(Fore.WHITE + Back.BLUE + "Ingresó una opción incorrecta")              
    guardar_huesped(lista_huesped)
