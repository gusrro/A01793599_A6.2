"""
Ejercicio 3 de programación - Pruebas unitarias
"""
import unittest
from datetime import date
from hotel import Hotel
from customer import Customer
from reservation import Reservation, ReservationData


class TestHotelMethods(unittest.TestCase):
    """Definición de la clase de pruebas unitarias para Hotel"""

    numbers = []

    def setUp(self):
        """Prueba unitaria - SetUp"""
        for i in range(0, 4):
            self.hotel = Hotel(-1, f"Prueba{i}",
                                   f"Location {i}", 50)
            self.hotel.guardar()
            self.numbers.append(self.hotel.obj_id)

    def tearDown(self):
        """Prueba unitaria - Teardown"""
        for i, _resort_name in enumerate(self.numbers):
            obj_id = self.numbers[i]
            self.hotel = self.hotel.load(obj_id)
            self.hotel.borrar()
        print("Limpiando información de Hoteles")
        self.numbers.clear()
        print("\n")

    def test_save(self):
        """Prueba unitaria - Método Guardar"""
        self.hotel.guardar()

    def test_delete(self):
        """Prueba unitaria - Método Borrar"""
        obj_id = self.numbers[0]
        self.hotel = self.hotel.load(obj_id)
        self.hotel.borrar()
        print(f"Intentando borrar el Hotel {self.hotel.obj_id}")
        self.numbers.remove(obj_id)

    def test_not_delete_error(self):
        """Prueba unitaria - Método Borrar - Error"""
        obj_id = self.numbers[0]
        self.hotel = self.hotel.load(obj_id)
        self.hotel.obj_id = 99999
        self.hotel.borrar()

    def test_print(self):
        """Prueba unitaria - Método Imprimir información"""
        print("Desplegando información de hoteles")
        self.hotel.imprimir_detalle()

    def test_not_load(self):
        """Prueba unitaria Negativa - Método cargar información"""
        self.hotel.load(9999)

    def test_modify(self):
        """Prueba unitaria - Método Modificar información"""
        print("Modificando información de hoteles")
        obj_id = self.numbers[1]
        self.hotel = self.hotel.load(obj_id)
        print("Antes de modificar")
        self.hotel.imprimir_detalle()
        self.hotel.resort_name = "Prueba de modificación"
        print("Después de modificar")
        self.hotel.imprimir_detalle()


class TestCustomerMethods(unittest.TestCase):
    """Definición de la clase de pruebas unitarias para Customer"""

    numbers = []

    def setUp(self):
        """Prueba unitaria - SetUp"""
        for i in range(0, 4):
            self.customer = Customer(-1, f"Nombre {i}",
                                         f"Apellido {i}",
                                         date(2000+i, 3+i, 10+i)
                                         .strftime("%d/%m/%Y"))
            self.customer.guardar()
            self.numbers.append(self.customer.obj_id)

    def tearDown(self):
        """Prueba unitaria - Teardown"""
        for i, _resort_name in enumerate(self.numbers):
            obj_id = self.numbers[i]
            self.customer = self.customer.load(obj_id)
            self.customer.borrar()
        print("Limpiando información de Clientes")
        self.numbers.clear()
        print("\n")

    def test_save(self):
        """Prueba unitaria - Método Guardar"""
        self.customer.guardar()

    def test_delete(self):
        """Prueba unitaria - Método Borrar"""
        obj_id = self.numbers[0]
        self.customer = self.customer.load(obj_id)
        self.customer.borrar()
        print(f"Intentando borrar el Cliente {self.customer.obj_id}")
        self.numbers.remove(obj_id)

    def test_not_delete_error(self):
        """Prueba unitaria - Método Borrar - Error"""
        obj_id = self.numbers[0]
        self.customer = self.customer.load(obj_id)
        self.customer.obj_id = 99999
        self.customer.borrar()

    def test_print(self):
        """Prueba unitaria - Método Imprimir información"""
        self.customer.imprimir_detalle()

    def test_not_load(self):
        """Prueba unitaria Negativa - Método cargar información"""
        self.customer.load(9999)

    def test_modify(self):
        """Prueba unitaria - Método Modificar información"""
        obj_id = self.numbers[1]
        self.customer = self.customer.load(obj_id)
        print("Antes de modificar")
        self.customer.imprimir_detalle()
        self.customer.first_name = "Ahora te llamarás prueba"
        print("Después de modificar")
        self.customer.imprimir_detalle()


class TestReservationMethods(unittest.TestCase):
    """Definición de la clase de pruebas unitarias para Reservation"""

    numbersH = []
    numbersC = []
    numbersR = []

    def setUp(self):
        """Prueba unitaria - SetUp"""
        currenth = 0
        currentc = 0
        for i in range(0, 4):
            # Setting hotels
            self.hotel = Hotel(-1, f"Prueba{i}",
                                   f"Location {i}", 50)
            self.hotel.guardar()
            self.numbersH.append(self.hotel.obj_id)
            currenth = self.hotel.obj_id

            # Setting customers
            self.customer = Customer(-1, f"Nombre {i}",
                                         f"Apellido {i}",
                                         date(2000+i, 3+i, 10+i)
                                         .strftime("%d/%m/%Y"))
            self.customer.guardar()
            self.numbersC.append(self.customer.obj_id)
            currentc = self.customer.obj_id

            # Setting reservations
            self.reservation = Reservation(-1, currentc,
                                           currenth,
                                           ReservationData((500+i),
                                                           date(2024, 3+i, 5+i)
                                                           .strftime("%d/"
                                                                     "%m/%Y"),
                                                           date(2024, 3+i, 8+i)
                                                           .strftime("%d/"
                                                                     "%m/%Y")))
            self.reservation.guardar()
            self.numbersR.append(self.reservation.obj_id)

    def tearDown(self):
        """Prueba unitaria - Teardown"""
        for i, _nonusedvar in enumerate(self.numbersC):
            obj_id = self.numbersC[i]
            self.customer = self.customer.load(obj_id)
            self.customer.borrar()
        print("Limpiando información de Clientes")
        self.numbersC.clear()
        for i, _nonusedvar in enumerate(self.numbersH):
            obj_id = self.numbersH[i]
            self.hotel = self.hotel.load(obj_id)
            self.hotel.borrar()
        print("Limpiando información de Hoteles")
        self.numbersH.clear()
        for i, _nonusedvar in enumerate(self.numbersR):
            obj_id = self.numbersR[i]
            self.reservation = self.reservation.load(obj_id)
            self.reservation.borrar()
        print("Limpiando información de Reservaciones")
        self.numbersR.clear()

        print("\n")

    def test_save(self):
        """Prueba unitaria - Método Guardar"""
        self.reservation.guardar()

    def test_delete(self):
        """Prueba unitaria - Método Borrar"""
        obj_id = self.numbersR[0]
        self.reservation = self.reservation.load(obj_id)
        self.reservation.borrar()
        print(f"Intentando borrar/cancelar la Res {self.reservation.obj_id}")
        self.numbersR.remove(obj_id)

    def test_not_delete_error(self):
        """Prueba unitaria - Método Borrar - Error"""
        obj_id = self.numbersR[0]
        self.reservation = self.reservation.load(obj_id)
        self.reservation.obj_id = 99999
        self.reservation.borrar()
        Hotel.cancel_reservation(self.reservation)

    def test_print(self):
        """Prueba unitaria - Método Imprimir información"""
        self.reservation.imprimir_detalle()

    def test_not_load(self):
        """Prueba unitaria Negativa - Método cargar información"""
        self.reservation.load(9999)

    def test_modify(self):
        """Prueba unitaria - Método Modificar información"""
        obj_id = self.numbersR[0]
        self.reservation = self.reservation.load(obj_id)
        print("Antes de modificar")
        self.reservation.imprimir_detalle()
        self.reservation.room = 824
        print("Después de modificar")
        self.reservation.imprimir_detalle()
