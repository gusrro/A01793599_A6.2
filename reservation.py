"""
Ejercicio 3 de programación - Pruebas unitarias
"""
import json
import os
from datetime import datetime
from hotel import Hotel
from tools import Tools


class Reservation:
    """Definiendo la clase Reservación"""

    # Definición de atributos
    obj_id = -1
    customer_id = -1
    hotel_id = -1

    # Definición de métodos
    def __init__(self, obj_id, customer_id, hotel_id, reservation_data):
        """Constructor de la clase"""
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.room = reservation_data.room
        self.entry_date = reservation_data.entry_date
        self.depart_date = reservation_data.depart_date
        reservation_data.imprimir_detalle()
        if -1 == obj_id:
            self.obj_id = self.get_next_id()
        else:
            self.obj_id = obj_id

    def guardar(self):
        """Método para guardar en archivo la información de la clase"""
        with open(f"./data/R{self.obj_id :04d}.txt", "w", encoding='utf-8') \
                as new_file:
            new_file.write(Tools.to_json(self))
        Hotel.create_reservation(self)

    def borrar(self):
        """Método para borrar fisicamente la información de la clase"""
        try:
            os.remove(f"./data/R{self.obj_id :04d}.txt")
            Hotel.cancel_reservation(self)
        except FileNotFoundError:
            print(f"El registro de Reservación {self.obj_id} no existe")

    def load(self, obj_id):
        """Método para cargar desde archivo la información de la clase"""
        filename = f"./data/R{obj_id :04d}.txt"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                reservation = Reservation.from_dict(data)
                f.close()
                return reservation
        except FileNotFoundError:
            print(f"Reservación {obj_id} no encontrada, no se pudo cargar")
            return None

    def get_next_id(self):
        """Método para establecer el siguiente id de hotel"""
        return Tools.get_next_id_from_file("R")

    def imprimir_detalle(self):
        """Método para imprimir la información de Reservación"""
        print(f"Reservación '{self.customer_id}': {self.hotel_id}")
        print(f"Detalle {self.room} - {self.entry_date} - {self.depart_date}")

    @classmethod
    def from_dict(cls, dt):
        """Método para crear un objeto desde un diccionario"""
        return cls(dt['obj_id'], dt['customer_id'], dt['hotel_id'],
                   ReservationData(dt['room'], dt['entry_date'],
                                   dt['depart_date']))


class ReservationData:
    """Definiendo la clase de datos de la reservación"""
    room = -1
    entry_date = "TBD"
    depart_date = "TBD"

    def __init__(self, room,
                 entry_date, depart_date):
        """Constructor de la clase"""
        self.room = room
        self.entry_date = entry_date
        self.depart_date = depart_date

    def imprimir_detalle(self):
        """Método para imprimir la información de Reservación"""
        print(f"Reservación '{self.room} - {self.entry_date} - "
              f"{self.depart_date}, duración {self.obtener_duracion()}")

    def obtener_duracion(self):
        """Método para obtener la duración de la reservación"""
        # convert string to date object
        d1 = datetime.strptime(self.entry_date, "%d/%m/%Y")
        d2 = datetime.strptime(self.depart_date, "%d/%m/%Y")

        return d2 - d1
