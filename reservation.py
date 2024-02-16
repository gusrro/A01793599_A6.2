"""
Ejercicio 3 de programación - Pruebas unitarias
"""
from datetime import date
from customer import Customer
from hotel import Hotel


class Reservation:
    """Definiendo la clase Reservación"""

    # Definición de atributos
    id = -1
    customer = Customer()
    hotel = Hotel()
    entryDate = date.today()
    departDate = date.today()

    # Definición de métodos
    def fun(self):
        """Method description"""
        print(f"I'm a {self.id}")
