"""
Ejercicio 3 de programación - Pruebas unitarias
"""
import json
import os

from tools import Tools


class Customer:
    """Definiendo la clase Hotel"""

    # Definición de atributos
    obj_id = -1
    first_name = "TBD"
    last_name = "TBD"
    birthdate = "TBD"
    email = "TBD"
    cellphone = "TBD"

    # Definición de métodos
    def __init__(self, obj_id, first_name, last_name, birthdate,
                 email, cellphone):
        """Constructor de la clase"""
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.email = email
        self.cellphone = cellphone
        if -1 == obj_id:
            self.obj_id = self.get_next_id()
        else:
            self.obj_id = obj_id

    def to_json(self):
        """Método para imprimir los datos de la clase a Json"""
        return json.dumps(self.__dict__)

    def guardar(self):
        """Método para guardar en archivo la información de la clase"""
        with open(f"./data/C{self.obj_id :04d}.txt", "w", encoding='utf-8') \
                as new_file:
            new_file.write(self.to_json())

    def borrar(self):
        """Método para borrar fisicamente la información de la clase"""
        try:
            os.remove(f"./data/C{self.obj_id :04d}.txt")
        except FileNotFoundError:
            print(f"El registro del Cliente {self.obj_id} no existe")

    def load(self, obj_id):
        """Método para cargar desde archivo la información de la clase"""
        filename = f"./data/C{obj_id :04d}.txt"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                customer = Customer.from_dict(data)
                f.close()
                return customer
        except FileNotFoundError:
            print(f"Cliente {obj_id} no encontrado, no se pudo cargar")

    def get_next_id(self):
        """Método para establecer el siguiente id de hotel"""
        return Tools.get_next_id_from_file("C")

    def imprimir_detalle(self):
        """Método para imprimir la información del Cliente"""
        print(f"Cliente '{self.first_name}': {self.last_name} "
              f"- {self.birthdate} - {self.email} - {self.cellphone}")

    @classmethod
    def from_dict(cls, dt):
        """Método para crear un objeto desde un diccionario"""
        return cls(dt['obj_id'], dt['first_name'], dt['last_name'],
                   dt['birthdate'], dt['email'], dt['cellphone'])
