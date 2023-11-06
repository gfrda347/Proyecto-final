from datetime import datetime, timedelta
from modelo.usuario import Usuario
from modelo.habitacion import Habitacion
from modelo.reserva import Reserva
from modelo.hotel import Hotel
from View.interfaz import HotelApp

NUM_HABITACIONES = 100
habitaciones = []

def solicitar_fechas():
    print("Ingresa las fechas de tu estadía en el formato 'YYYY-MM-DD'.")
    fecha_inicio = input("Fecha de ingreso al hotel: ")
    fecha_fin = input("Fecha de salida del hotel: ")
    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
    if fecha_inicio >= fecha_fin:
        raise ValueError("La fecha de inicio debe ser anterior a la fecha de salida.")
    return fecha_inicio, fecha_fin

def mostrar_habitaciones_disponibles(habitaciones):
    print("Habitaciones disponibles:")
    for habitacion in habitaciones:
        print(f"{habitacion.numero}: {habitacion.tipo} - Precio: ${habitacion.precio} por noche")

def elegir_habitacion(habitaciones):
    while True:
        mostrar_habitaciones_disponibles(habitaciones)
        seleccion = input("Elige el número de la habitación que deseas (0 para cancelar): ")
        if not seleccion:
            print("Debes ingresar un número de habitación válido.")
            continue
        try:
            seleccion = int(seleccion)
        except ValueError:
            print("Debes ingresar un número de habitación válido.")
            continue
        if seleccion == 0:
            return None
        habitacion_elegida = next((habitacion for habitacion in habitaciones if habitacion.numero == seleccion), None)
        if habitacion_elegida is None:
            print("Número de habitación no válido. Introduce un número de habitación válido.")
        else:
            return habitacion_elegida

def realizar_reserva(usuario, fecha_inicio, fecha_fin, habitaciones):
    if fecha_inicio > fecha_fin:
        raise ValueError("La fecha de inicio debe ser anterior a la fecha de finalización.")
    for habitacion in habitaciones:
        for fecha in range((fecha_fin - fecha_inicio).days + 1):
            fecha_check = fecha_inicio + timedelta(days=fecha)
            habitacion.fechas_ocupadas.append(fecha_check)
    reserva = Reserva(usuario, fecha_inicio, fecha_fin, habitaciones)
    usuario.reservas.append(reserva)
    print("Reserva realizada exitosamente.")

def mostrar_estado_habitacion(numero_habitacion, habitaciones):
    habitacion = next((h for h in habitaciones if h.numero == numero_habitacion), None)
    if habitacion:
        if habitacion.fechas_ocupadas:
            print(f"Habitación {numero_habitacion} está ocupada en las siguientes fechas:")
            for fecha in habitacion.fechas_ocupadas:
                print(f"- {fecha.strftime('%d/%m/%Y')}")
        else:
            print(f"Habitación {numero_habitacion} está desocupada.")
    else:
        print(f"No se encontró la habitación {numero_habitacion}.")

def cliente_verificar_estado_habitacion():
    numero_habitacion = int(input("Ingresa el número de la habitación que deseas verificar: "))
    mostrar_estado_habitacion(numero_habitacion, habitaciones)

def cliente_cancelar_reserva(usuario):
    if not usuario.reservas:
        print("No tienes reservas para cancelar.")
        return
    print("Tus reservas:")
    for i, reserva in enumerate(usuario.reservas, start=1):
        print(f"{i}. Habitaciones: {', '.join(str(h.numero) for h in reserva.habitaciones)}")
    opcion = int(input("Ingresa el número de la reserva que deseas cancelar (0 para cancelar): "))
    if opcion == 0:
        return
    if opcion > 0 and opcion <= len(usuario.reservas):
        reserva_a_cancelar = usuario.reservas.pop(opcion - 1) 
        print("Reserva cancelada exitosamente.")
    else:
        print("Opción no válida.")
hotel_informacion = Hotel(
    nombre="El Parche de los Sueños",
    ubicacion="Medellín",
    instalaciones=["Piscina", "Gimnasio", "Restaurante"],
    servicios=["Wi-Fi gratuito", "Servicio de habitaciones", "Parqueadero gratuito"]
)
print(hotel_informacion.obtener_informacion_hotel())
usuarios = [
    Usuario("victor", "doble123"),
    Usuario("santiago", "12345"),
    Usuario("gabriel", "profe")
]
habitaciones = [
    Habitacion(1, "Doble", 100),
    Habitacion(2, "Individual", 50),
    Habitacion(3, "Suite", 200)
]

def iniciar_sesion(nombre_usuario, contrasena):
    for usuario in usuarios:
        if usuario.nombre_usuario == nombre_usuario and usuario.contrasena == contrasena:
            return usuario
    return None
nombre_usuario = input("Ingresa tu nombre de usuario: ")
contrasena = input("Ingresa tu contraseña: ")
usuario_actual = iniciar_sesion(nombre_usuario, contrasena)
if usuario_actual:
    print("Sesión iniciada como:")
    print(usuario_actual.nombre_usuario)
else:
    print("Inicio de sesión fallido.")
fecha_inicio, fecha_fin = solicitar_fechas()
duracion_estadia = (fecha_fin - fecha_inicio).days
print(f"Fecha de ingreso: {fecha_inicio.strftime('%d/%m/%Y')}")
print(f"Fecha de salida: {fecha_fin.strftime('%d/%m/%Y')}")
print(f"Duración de la estadía: {duracion_estadia} días")
habitacion_elegida = elegir_habitacion(habitaciones)
if habitacion_elegida:
    print(f"Habitación elegida: {habitacion_elegida.tipo} - Precio: ${habitacion_elegida.precio} por noche")
    costo_total = duracion_estadia * habitacion_elegida.precio
    print(f"Total a pagar por {duracion_estadia} días de hospedaje: ${costo_total}")
while True:
    print("\nMenú de Cliente:")
    print("1. Verificar estado de una habitación")
    print("2. Cancelar una reserva")
    print("3. Salir")
    opcion_cliente = int(input("Ingresa el número de la opción que deseas realizar: "))
    if opcion_cliente == 1:
        cliente_verificar_estado_habitacion()
    elif opcion_cliente == 2:
        if usuario_actual:
            cliente_cancelar_reserva(usuario_actual)
        else:
            print("Debes iniciar sesión para cancelar una reserva.")
    elif opcion_cliente == 3:
        print("¡Gracias por visitar nuestro hotel! Hasta luego.")
        break
    else:
        print("Opción no válida.")