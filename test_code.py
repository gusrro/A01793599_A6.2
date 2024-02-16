"""
Ejercicio 3 de programación - Pruebas unitarias
"""
import unittest
import os
from hotel import Hotel


class TestHotelMethods(unittest.TestCase):
    """Definición de la clase de pruebas unitarias para Hotel"""

    def setUp(self):
        """Prueba unitaria - SetUp"""
        self.hotel = Hotel(1, "Test Another Try", "Test Location", 50)

    def tearDown(self):
        """Prueba unitaria - Teardown - No hace sentido borrar el objeto"""
        print("All objects must be destroyed, nothing to do yet")

    def test_save(self):
        """Prueba unitaria - Método Guardar"""
        self.hotel.guardar()

    def test_save_another(self):
        """Prueba unitaria - Método Guardar"""
        self.hotel = Hotel(-1, "Prueba random", "Test Location", 500)
        self.hotel.guardar()


if __name__ == '__main__':
    unittest.main()
