"""
Ejercicio 3 de programación - Pruebas unitarias
"""
import json
import os
from hotel import Hotel
from tools import Tools


class Reservation:
    """Definiendo la clase Hotel"""

    # Definición de atributos
    obj_id = -1
    customer_id = -1
    hotel_id = -1
    room = -1
    entry_date = "TBD"
    depart_date = "TBD"

    # Definición de métodos
    def __init__(self, obj_id, customer_id, hotel_id, room,
                 entry_date, depart_date):
        """Constructor de la clase"""
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.room = room
        self.entry_date = entry_date
        self.depart_date = depart_date
        if -1 == obj_id:
            self.obj_id = self.get_next_id()
        else:
            self.obj_id = obj_id

    def to_json(self):
        """Método para imprimir los datos de la clase a Json"""
        return json.dumps(self.__dict__)

    def guardar(self):
        """Método para guardar en archivo la información de la clase"""
        with open(f"./data/R{self.obj_id :04d}.txt", "w", encoding='utf-8') \
                as new_file:
            new_file.write(self.to_json())
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

    def get_next_id(self):
        """Método para establecer el siguiente id de hotel"""
        return Tools.get_next_id_from_file("R")

    def imprimir_detalle(self):
        """Método para imprimir la información de Reservación"""
        print(f"Reservación '{self.customer_id}': {self.hotel_id} - "
              f"{self.room} - {self.entry_date} - {self.depart_date}")

    @classmethod
    def from_dict(cls, dt):
        """Método para crear un objeto desde un diccionario"""
        return cls(dt['obj_id'], dt['customer_id'], dt['hotel_id'],
                   dt['room'], dt['entry_date'], dt['depart_date'])
