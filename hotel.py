"""
Ejercicio 3 de programación - Pruebas unitarias
"""
import json

from tools import Tools


class Hotel:
    """Definiendo la clase Hotel"""

    # Definición de atributos
    id = -1
    resort_name = "TBD"
    city = "TBD"
    zip_code = 12345

    # Definición de métodos
    def __init__(self, obj_id, resort_name, city, zip_code):
        """Constructor de la clase"""
        self.resort_name = resort_name
        self.city = city
        self.zip_code = zip_code
        if -1 == obj_id:
            self.obj_id = self.get_next_id()
        else:
            self.obj_id = obj_id

    def to_json(self):
        """Método para imprimir los datos de la clase a Json"""
        return json.dumps(self.__dict__)

    def guardar(self):
        """Método para guardar en archivo la información de la clase"""
        with open(f"./data/H{self.obj_id :04d}.txt", "w", encoding='utf-8') \
                as new_file:
            new_file.write(self.to_json())

    def get_next_id(self):
        """Método para establecer el siguiente id de hotel"""
        return Tools.get_next_id_from_file("hotel")
