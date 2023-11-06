from modelo.usuario import Usuario
from modelo.habitacion import Habitacion

class Reserva:
    reservas = []

    def __init__(self, usuario, fecha_inicio, fecha_fin, habitaciones):
        self.usuario = usuario
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.habitaciones = habitaciones
        Reserva.reservas.append(self)

    def cancelar_reserva(self):
        if self in Reserva.reservas:
            Reserva.reservas.remove(self)
            print("Reserva cancelada exitosamente.")
        else:
            print("No se encontró la reserva para cancelar.")
