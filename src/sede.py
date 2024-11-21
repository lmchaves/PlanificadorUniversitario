from pieza import Pieza

class Sede:
    """"
    Representa una sede del taller, con información de ubicación y detalles del inventario de piezas
    
    Atributos:
      nombre (str): Nombre descriptivo de la sede
      ubicacion (str): Ubicación geográfica de la sede
      inventario (dict): Diccionario inmutable que mapea Pieza a cantidad disponible 
    """
    def __init__(self, nombre: str, direccion: str, inventario: dict):
        if not nombre or not direccion:
            raise ValueError("El nombre y la dirección no pueden estar vacíos.")
        if not isinstance(inventario, dict):
            raise ValueError("El inventario debe ser un diccionario.")

        # Validación del inventario: las cantidades deben ser no negativas
        for pieza, cantidad in inventario.items():
            if not isinstance(pieza, Pieza):
                raise ValueError("El inventario debe contener solo objetos Pieza como claves.")
            if cantidad < 0:
                raise ValueError("Las cantidades en el inventario no pueden ser negativas.")

        self._nombre = nombre
        self._direccion = direccion
        self._inventario = dict(inventario)  # Copia para garantizar inmutabilidad