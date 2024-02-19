"""
Ejercicio 3 de programación - Pruebas unitarias
"""
import json
import os
from tools import Tools


class Hotel:
    """Definiendo la clase Hotel"""

    # Definición de atributos
    obj_id = -1
    resort_name = "TBD"
    city = "TBD"
    rooms = 12345

    # Definición de métodos
    def __init__(self, obj_id, resort_name, city, rooms):
        """Constructor de la clase"""
        self.resort_name = resort_name
        self.city = city
        self.rooms = rooms
        if -1 == obj_id:
            self.obj_id = self.get_next_id()
        else:
            self.obj_id = obj_id
        print(f"Creando Hotel {self.obj_id} - {self.resort_name}")

    def guardar(self):
        """Método para guardar en archivo la información de la clase"""
        with open(f"./data/H{self.obj_id :04d}.txt", "w", encoding='utf-8') \
                as new_file:
            new_file.write(Tools.to_json(self))

    def borrar(self):
        """Método para borrar fisicamente la información de la clase"""
        try:
            os.remove(f"./data/H{self.obj_id :04d}.txt")
            print(f"Borrando Hotel {self.obj_id} - {self.resort_name}")
        except FileNotFoundError:
            print(f"El registro del Hotel {self.obj_id} no existe")

    def load(self, obj_id):
        """Método para cargar desde archivo la información de la clase"""
        filename = f"./data/H{obj_id :04d}.txt"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                hotel = Hotel.from_dict(data)
                f.close()
                return hotel
        except FileNotFoundError:
            print(f"Hotel {obj_id} no encontrado, no se pudo cargar")
            return None

    def get_next_id(self):
        """Método para establecer el siguiente id de hotel"""
        return Tools.get_next_id_from_file("H")

    def imprimir_detalle(self):
        """Método para imprimir la información del hotel"""
        print(f"Hotel '{self.resort_name}': {self.city} - {self.rooms}")

    @classmethod
    def from_dict(cls, dt):
        """Método para crear un objeto desde un diccionario"""
        return cls(dt['obj_id'], dt['resort_name'], dt['city'], dt['rooms'])

    @classmethod
    def create_reservation(cls, reservation):
        """Método para guardar una reservación"""
        with open(f"./data/Hr{reservation.hotel_id :04d}"
                  f"_{reservation.customer_id}"
                  f"_{reservation.obj_id}.txt", "w", encoding='utf-8') \
                as new_file:
            new_file.write(Tools.to_json(reservation))

    @classmethod
    def cancel_reservation(cls, reservation):
        """Método para cancelar una reservación"""
        try:
            os.remove(f"./data/Hr{reservation.hotel_id :04d}"
                      f"_{reservation.customer_id}"
                      f"_{reservation.obj_id}.txt")
        except FileNotFoundError:
            pass
