import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.fechas_ocupadas = []

class Reserva:
    def __init__(self, usuario, fecha_inicio, fecha_fin, habitaciones):
        self.usuario = usuario
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.habitaciones = habitaciones

class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.reservas = []

class HotelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Reservas de Hotel")
        self.root.attributes('-fullscreen', True)  

        self.usuario_actual = None
        self.fecha_ingreso = None
        self.fecha_salida = None

        self.habitaciones = [
            Habitacion(1, "Doble", 100),
            Habitacion(2, "Individual", 50),
            Habitacion(3, "Suite", 200)
        ]

        self.root.configure(bg="#E6E6FA")

        self.label_info_hotel = tk.Label(root, text="Información del Hotel El Parche de los Sueños:", font=("Helvetica", 25, "bold"))
        self.label_info_hotel.pack(pady=20)

        info_hotel = "Ubicación: Medellín\nInstalaciones:\n- Piscina\n- Gimnasio\n- Restaurante\nServicios:\n- Wi-Fi gratuito\n- Servicio de habitaciones\n- Parqueadero gratuito"
        self.label_info = tk.Label(root, text=info_hotel, font=("Helvetica", 20))
        self.label_info.pack(pady=20)

        self.label_nombre_usuario = tk.Label(root, text="Nombre de Usuario:", font=("Helvetica", 14))
        self.label_nombre_usuario.pack()
        self.entry_nombre_usuario = tk.Entry(root, font=("Helvetica", 14))
        self.entry_nombre_usuario.pack()

        self.label_contrasena = tk.Label(root, text="Contraseña:", font=("Helvetica", 14))
        self.label_contrasena.pack()
        self.entry_contrasena = tk.Entry(root, show="*", font=("Helvetica", 14))
        self.entry_contrasena.pack()

        self.iniciar_sesion_button = tk.Button(root, text="Iniciar Sesión", command=self.iniciar_sesion, font=("Helvetica", 14), borderwidth=2, relief="solid")
        self.iniciar_sesion_button.pack()

    def iniciar_sesion(self):
        nombre_usuario = self.entry_nombre_usuario.get()
        contrasena = self.entry_contrasena.get()

        if nombre_usuario == "santiago" and contrasena == "12345":
            self.usuario_actual = Usuario(nombre_usuario, contrasena)
            self.solicitar_fechas()
        else:
            messagebox.showerror("Error", "Inicio de sesión fallido. Verifica tus credenciales.")

    def solicitar_fechas(self):
        if self.usuario_actual:
            self.label_nombre_usuario.destroy()
            self.entry_nombre_usuario.destroy()
            self.label_contrasena.destroy()
            self.entry_contrasena.destroy()
            self.iniciar_sesion_button.destroy()

            self.label_fecha_ingreso = tk.Label(self.root, text="Ingresa la fecha de ingreso al hotel (formato: DD/MM/YYYY):", font=("Helvetica", 14))
            self.label_fecha_ingreso.pack()
            self.entry_fecha_ingreso = tk.Entry(self.root, font=("Helvetica", 14))
            self.entry_fecha_ingreso.pack()

            self.label_fecha_salida = tk.Label(self.root, text="Ingresa la fecha de salida del hotel (formato: DD/MM/YYYY):", font=("Helvetica", 14))
            self.label_fecha_salida.pack()
            self.entry_fecha_salida = tk.Entry(self.root, font=("Helvetica", 14))
            self.entry_fecha_salida.pack()

            self.reserva_button = tk.Button(self.root, text="Continuar", command=self.validar_fechas, font=("Helvetica", 14), borderwidth=2, relief="solid")
            self.reserva_button.pack()
        else:
            messagebox.showerror("Error", "Debes iniciar sesión para continuar.")

    def validar_fechas(self):
        fecha_ingreso = self.entry_fecha_ingreso.get()
        fecha_salida = self.entry_fecha_salida.get()

        if self.validar_fechas_ingresadas(fecha_ingreso, fecha_salida):
            self.fecha_ingreso = datetime.strptime(fecha_ingreso, "%d/%m/%Y").date()
            self.fecha_salida = datetime.strptime(fecha_salida, "%d/%m/%Y").date()
            self.mostrar_habitaciones()
        else:
            messagebox.showerror("Error", "Fechas no válidas. Ingresa las fechas en formato DD/MM/YYYY.")

    def validar_fechas_ingresadas(self, fecha_ingreso, fecha_salida):
        try:
            fecha_ingreso = datetime.strptime(fecha_ingreso, "%d/%m/%Y")
            fecha_salida = datetime.strptime(fecha_salida, "%d/%m/%Y")

            if fecha_ingreso < fecha_salida:
                return True
            else:
                return False
        except ValueError:
            return False

    def mostrar_habitaciones(self):
        if self.usuario_actual and self.fecha_ingreso and self.fecha_salida:
            self.label_fecha_ingreso.destroy()
            self.entry_fecha_ingreso.destroy()
            self.label_fecha_salida.destroy()
            self.entry_fecha_salida.destroy()
            self.reserva_button.destroy()

            habitaciones_disponibles = self.obtener_habitaciones_disponibles()

            if habitaciones_disponibles:
                self.label_habitaciones_disponibles = tk.Label(self.root, text="Habitaciones disponibles:", font=("Helvetica", 18, "bold"))
                self.label_habitaciones_disponibles.pack()

                for habitacion in habitaciones_disponibles:
                    label_habitacion = tk.Label(self.root, text=f"Habitación {habitacion.numero}: {habitacion.tipo} - Precio: ${habitacion.precio} por noche", font=("Helvetica", 14))
                    label_habitacion.pack()

                self.label_elegir_habitacion = tk.Label(self.root, text="Elige el número de la habitación que deseas (0 para cancelar):", font=("Helvetica", 14))
                self.label_elegir_habitacion.pack()

                self.entry_elegir_habitacion = tk.Entry(self.root, font=("Helvetica", 14))
                self.entry_elegir_habitacion.pack()

                self.reservar_button = tk.Button(self.root, text="Reservar", command=self.realizar_reserva, font=("Helvetica", 14), borderwidth=2, relief="solid")
                self.reservar_button.pack()
            else:
                messagebox.showinfo("Información", "No hay habitaciones disponibles para las fechas seleccionadas.")
        else:
            messagebox.showerror("Error", "Debes iniciar sesión y seleccionar fechas para continuar.")

    def obtener_habitaciones_disponibles(self):
        habitaciones_disponibles = []
        for habitacion in self.habitaciones:
            disponible = self.verificar_disponibilidad(habitacion)
            if disponible:
                habitaciones_disponibles.append(habitacion)
        return habitaciones_disponibles

    def verificar_disponibilidad(self, habitacion):
        for reserva in self.usuario_actual.reservas:
            if self.fecha_ingreso <= reserva.fecha_fin and self.fecha_salida >= reserva.fecha_inicio:
                for habitacion_reservada in reserva.habitaciones:
                    if habitacion.numero == habitacion_reservada.numero:
                        return False
        return True

    def realizar_reserva(self):
        numero_habitacion = self.entry_elegir_habitacion.get()
        if numero_habitacion == "0":
            messagebox.showinfo("Información", "Reserva cancelada.")
            return

        habitacion_seleccionada = None
        for habitacion in self.habitaciones:
            if str(habitacion.numero) == numero_habitacion:
                habitacion_seleccionada = habitacion
                break

        if habitacion_seleccionada:
            disponibilidad = self.verificar_disponibilidad(habitacion_seleccionada)

            if disponibilidad:
                if self.usuario_actual:
                    habitacion_seleccionada.fechas_ocupadas.append(self.fecha_ingreso)
                    fecha_fin = self.fecha_ingreso
                    while fecha_fin < self.fecha_salida:
                        fecha_fin += timedelta(days=1)
                        habitacion_seleccionada.fechas_ocupadas.append(fecha_fin)

                    if self.usuario_actual.reservas is None:
                        self.usuario_actual.reservas = []

                    self.usuario_actual.reservas.append(Reserva(self.usuario_actual, self.fecha_ingreso, self.fecha_salida, [habitacion_seleccionada]))
                    self.mostrar_confirmacion_reserva(habitacion_seleccionada)
                else:
                    messagebox.showerror("Error", "Debes iniciar sesión para realizar una reserva.")
            else:
                messagebox.showerror("Error", "La habitación seleccionada no está disponible para las fechas ingresadas.")
        else:
            messagebox.showerror("Error", "Número de habitación no válido. Introduce un número de habitación válido.")

    def mostrar_confirmacion_reserva(self, habitacion):
        mensaje = f"Reserva realizada.\nHabitación: {habitacion.tipo}\nFecha de ingreso: {self.fecha_ingreso}\nFecha de salida: {self.fecha_salida}\nPrecio total: ${len(habitacion.fechas_ocupadas) * habitacion.precio}"
        respuesta = messagebox.askquestion("Confirmación de Reserva", mensaje + "\n\n¿Desea cancelar la reserva?")

        if respuesta == "yes":
            self.usuario_actual.reservas.pop() 
            messagebox.showinfo("Información", "Reserva cancelada.")
        else:
            messagebox.showinfo("Información", "Reserva confirmada. ¡Disfruta de tu estancia!")

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()
