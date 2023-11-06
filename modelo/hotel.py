class Hotel:
    def __init__(self, nombre, ubicacion, instalaciones, servicios):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.instalaciones = instalaciones
        self.servicios = servicios

    def obtener_informacion_hotel(self):
        informacion = f"Información del Hotel {self.nombre}:\n"
        informacion += f"Ubicación: {self.ubicacion}\n"
        informacion += "Instalaciones:\n"
        for instalacion in self.instalaciones:
            informacion += f"- {instalacion}\n"
        informacion += "Servicios:\n"
        for servicio in self.servicios:
            informacion += f"- {servicio}\n"
        return informacion
