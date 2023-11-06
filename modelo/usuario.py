from modelo.habitacion import Habitacion

class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.reservas = []

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
