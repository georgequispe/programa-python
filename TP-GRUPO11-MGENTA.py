
from colorama import Fore, Style, Back, init
init(autoreset=False)
disponibles = []
lista_habitaciones = []#Lista pars almacenar las habitaciones

import json
filehabi='lista_habitaciones.json'
filerese='lista_reservas.json'
filehuesped='lista_huesped.json'
def guardar_habitaciones(lista_habitaciones):
    with open(filehabi, 'w') as fiha:
        json.dump(lista_habitaciones,fiha)
    return lista_habitaciones

def carga_habitaciones():
    with open(filehabi) as fiha:
        lista_habitaciones=json.load(fiha)
    return lista_habitaciones

def carga_reservas():
    with open(filerese) as fire:
        lista_reservas=json.load(fire)
    return lista_reservas

def guardar_huesped(lista_huesped):
    with open(filehuesped, 'w') as fihu:
        json.dump(lista_huesped,fihu)

def guardar_reservas(lista_reservas):
    with open(filerese, 'w') as fire:
        json.dump(lista_reservas,fire)

def buscar_dato_lista_huesped(lista_huesped,valor):
    # Matias/ Busca un valor dentro de los diccionarios en la lista de clientes, te retorna sí se halló y una copia del diccionario relacionado al valor.
    # Parámetros: valor: dato a buscar.
    # Retorno: True/ False: dato de tipo bool. cliente: variable tipo diccionario.

    encontre=False
      
    for hue in range(0,len(lista_huesped)):                
        if valor==lista_huesped[hue]['dni']:        
            print(f"encontre a : {lista_huesped[hue]['nombre']}")            
            encontre=True
            break
    if not encontre:
        return encontre

# def eliminar_huesped(lista_huesped,dni):
#     # Matias/ Solicita que se ingrese un dni (dato entero), lo busca en la lista de huespedes y elimina el cliente (diccionario con datos de cliente),
#     # en caso de no hallarlo imprime un mensaje.
#     # Parámetros: lista_huesped : lista de diccionarios donde se almacenan los datos de los clientes.
#     esta=False
    
#     print(Fore.WHITE + Back.BLUE + "Eliminar Huesped".center(50))
#     while True:
#         if dni==0:
#             dni = obtener_dni("Ingrese DNI del cliente a eliminar: ")
#             esta = buscar_dato_lista_huesped(lista_huesped,dni)#aqui errrrrrrrror
#         if esta:
#             print(Fore.WHITE + Back.BLUE + "Cliente hallado.")
#             lista_huesped.remove(dni)
#             lista_reservas.remove(dni)
#             print(Fore.WHITE + Back.BLUE + "Cliente Eliminado con Éxito.")
#             break
#         else:
#             print(Fore.WHITE + Back.BLUE + "Cliente no hallado.")
#             break

def buscar_dato_lista_reservas(lista_reservas,valor):
  # Matias/ Toma como parámetro un dato y lo busca en los diccionarios de la lista de reservas,
    encontre=False
      
    for res in range(0,len(lista_reservas)):                
        if valor==lista_reservas[res]['dni']:        
            print(f"encontre a : {lista_reservas[res]['nombre']}")            
            encontre=True
            break
        
                
    if encontre:
        return True
    else:
        return False

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

def crear_habitaciones():
    #Pablo/ Crea una lista de 20 habitaciones, 10 dobles y 10 triples, con estado inicial "libre".

    for num_habitacion in range(1, 21):
        # Determina el tipo de habitación (Doble o Triple)
        if num_habitacion <= 10:
            tipo_habitacion = "doble"
        else:
            tipo_habitacion = "triple"
        # Crea el diccionario de las habitaciones.
        habitacion = {
            "numero": num_habitacion,
            "tipo": tipo_habitacion,
            "dni": 0,
            "estado": "libre"
            }
        lista_habitaciones.append(habitacion)  #Agrega las habitaciones al diccionario. 
    guardar_habitaciones(lista_habitaciones)        
    return lista_habitaciones

   

def modificar_estado_habitacion(lista_habitaciones,numero,dni, estado):
  # Matias/ Modifica la lista de habitaciones del programa segun el estado de la lista de habitaciones
  # seleccionadas para la reserva.
  # Parámetros: habitaciones_reserva: lista de diccionarios donde cada uno representa una habitación
  # seleccionada, estado: dato tipo cadena de caracteres que representa el nuevo estado
      
          
    if estado=='libre':
        for hab in range(0,len(lista_habitaciones)):
            print(f"numero de habitacion que pase: {numero}")
            print(estado)
            #aqui esta el problema con el ingresi del huesped y crear cliente
            if lista_habitaciones[hab]['numero']==numero:
                
                print(lista_habitaciones[hab]['estado'])
                lista_habitaciones[hab]["dni"] = 0
                lista_habitaciones[hab]["estado"] = 'libre'
                print(" puso en cero el dni")
                break
            
    if estado=='ocupado':
        for hab in range(0,len(lista_habitaciones)):
            
            if lista_habitaciones[hab]['numero']==numero:

                lista_habitaciones[hab]['dni']=dni
                print("ingrese en ocupado")
                print(lista_habitaciones[hab]['dni'])
                lista_habitaciones[hab]['estado']='ocupado'
                break
    print("Estado de habitaciónes modificado con éxito")
    lista_habitaciones=guardar_habitaciones(lista_habitaciones)
    return lista_habitaciones

def ver_habitaciones(lista_habitaciones):
   #muestra las habitaciones libres y las ocupadas
    
    print(Fore.WHITE + Back.BLUE + "Lista de habitaciones disponibles: ")   
    lista_habitaciones=carga_habitaciones()
    for hab in range(0,len(lista_habitaciones)):            
        if lista_habitaciones[hab]['estado']=='libre':
            
            print(Fore.GREEN + f"\nhabitación: {lista_habitaciones[hab]['numero']}")            
            print(Fore.GREEN + f"Estado: {lista_habitaciones[hab]['estado']}")
            print(Fore.GREEN + f"Tipo: {lista_habitaciones[hab]['tipo']}")
        else:
            print(Fore.RED + Back.WHITE+ f"\nhabitación: {lista_habitaciones[hab]['numero']}")            
            print(Fore.RED + Back.WHITE+ f"Estado: {lista_habitaciones[hab]['estado']}")
            print(Fore.RED +Back.WHITE+ f"Tipo: {lista_habitaciones[hab]['tipo']}")
    if not lista_habitaciones:
        print(Fore.WHITE + Back.BLUE + "No hay habitaciones disponibles.")

def seleccionar_habitaciones(lista_habitaciones,dni, tipo):   
        #habitaciones = crear_habitaciones()    
    #disponibles = [hab for hab in lista_habitaciones if hab["tipo"] == tipo and hab["estado"] == "libre"]
    #disponible solo tiene una lista con las habitaciones dobles y el numero
    #for habi in lista_habitaciones:                     
    for hab in range(0,20): 
                  
        if lista_habitaciones[hab]['tipo']==tipo and lista_habitaciones[hab]['estado']=="libre":
                print(Fore.WHITE + Back.GREEN + f"Número: {lista_habitaciones[hab]['numero']}")              
                        
    while True:
        try:
            numero = int(input(Fore.WHITE + Back.BLUE + "Ingrese el número de habitación: "))
                                
            if 0<numero<21:
                lista_habitaciones=modificar_estado_habitacion(lista_habitaciones,numero,dni, "ocupado")
                lista_habitaciones=guardar_habitaciones(lista_habitaciones) 
                
                print(Fore.WHITE + Back.BLUE + "Habitación seleccionada con éxito.")
                return numero
                break
            else:
                print(Fore.WHITE + Back.BLUE + "Número de habitación no válido.")
            
        except ValueError:
            print(Fore.WHITE + Back.BLUE + "El dato ingresado no es correcto.")
    return lista_habitaciones    
    
     
    
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

def pasar_reserva_a_huesped(lista_reservas,lista_huesped,indice,dni,num_hab):
    #cuando la personas de reserva, llegan al hotel y pasan a ser cliente-huesped.
    #tambien se modifican las habitaciones a ocupado.
    dir=input("ingrese una dirección: ")
    cel=input("ingrese su numero de celular: ")
    datos_huesped={
        "nombre":(lista_reservas[indice]['nombre']),
        "dni":(lista_reservas[indice]['dni']),
        "direccion":dir,
        "cantidad_noches":(lista_reservas[indice]['cantidad_noches']) ,
        "numero_hab":num_hab ,
        "cantidad_habitaciones": lista_reservas[indice]['cantidad_habitaciones'],
        "cantidad_dobles":lista_reservas[indice]['cantidad_dobles'],
        "cantidad_triples":lista_reservas[indice]['cantidad_triples'], 
        "celular":cel,
    }
    lista_huesped.append(datos_huesped)
    guardar_huesped(lista_huesped)
                

def ingreso_huesped(lista_reservas,lista_habitaciones,lista_huesped):
    # Solicita que se ingrese un dni, valida el formato y si encuentra una coincidencia 
    # muestra todas las reservas con un indice y modifica en la lista de habitaciones el estado
    # de libre a ocupado
    print(Fore.WHITE + Back.BLUE + "Marcar ingreso".center(50, "-"))
    dni = obtener_dni("Ingrese DNI del cliente para buscar la reserva: ")
    esta = buscar_dato_lista_reservas(lista_reservas,dni)
    indice=0
    if esta == True:
      
        print(Fore.WHITE + Back.BLUE + "Se ha encontrado la reserva para ese cliente: ")
        for i, reserva in enumerate(lista_reservas):
          print(Fore.WHITE + Back.BLUE +f"{i}. '{reserva['nombre']}' Del '{reserva['fecha_ingreso']}' al '{reserva['fecha_salida']}'")
        indice = obtener_entero("Introduce el número de la reserva a seleccionar: ")
        if lista_reservas[indice]['cantidad_dobles']>0:
                
                print(Fore.WHITE + Back.GREEN +"Seleccione las habitaciones dobles a utilizar: ")
                
                num_hab=seleccionar_habitaciones(lista_habitaciones,dni,"doble")
                pasar_reserva_a_huesped(lista_reservas,lista_huesped,indice,dni,num_hab)
                lista_reservas.remove(lista_reservas[indice])
                guardar_huesped(lista_huesped)#revisar no me muestra la lista de clientes
                guardar_reservas(lista_reservas)
        else:
            if lista_reservas[indice]['cantidad_triples']>0:
                print(Fore.WHITE + Back.GREEN +"Seleccione las habitaciones triples a utilizar: ")
                lista_habitaciones=seleccionar_habitaciones(lista_habitaciones,lista_reservas[indice]['cantidad_triples'], "triple")
                pasar_reserva_a_huesped(lista_reservas,lista_huesped,indice,dni)
                lista_reservas.remove(lista_reservas[indice])
                
        print(Fore.WHITE + Back.BLUE + "Ingreso marcado con éxito.")
        return lista_habitaciones
    else:     
      print(Fore.WHITE + Back.BLUE + "Reserva no encontrada.")


def modificar_precios():
    # Matias/ Solicita al usuario que ingrese los nuevos precios para las habitaciones,
    # y valida que los datos ingresados sean correctos.

    print(Fore.WHITE + Back.BLUE + "Modificar precios de habitaciones".center(50, "-"))
    precio_dobles = obtener_cantidad("Ingrese el nuevo precio para las habitaciones dobles: ")
    precio_triples = obtener_cantidad("Ingrese el nuevo precio para las habitaciones triples: ")
    print(Fore.WHITE + Back.BLUE + "Precios actualizados con éxito.")

