"""
Ejercicio 3 de programación - Pruebas unitarias
"""
from datetime import date


class Customer:
    """Definiendo la clase Cliente"""

    # Definición de atributos
    firstName = "TBD"
    lastName = "TBD"
    birthdate = date.today()
    email = "TBD"
    cellphone = "TBD"

    # Definición de métodos
    def fun(self):
        """Method description"""
        print(f"I'm a {self.firstName}")
