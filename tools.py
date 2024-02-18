"""
Ejercicio 3 de programación - Pruebas unitarias
"""
import os


class Tools:
    """Definiendo la clase Tools"""

    # Definición de métodos
    @staticmethod
    def get_next_id_from_file(prefix):
        """Método para obtener el siguiente ID para un prefijo dado"""

        files = os.listdir("./data")

        # Obtener los números que ya existen
        numbers = []
        for file in files:
            file_name, _file_extension = os.path.splitext(file)
            part = file_name.replace(prefix, '')
            if part.isdigit():
                numbers.append(int(part))

        # If there are no numeric parts in filenames
        if not numbers:
            return 1
        else:
            return max(numbers)+1
