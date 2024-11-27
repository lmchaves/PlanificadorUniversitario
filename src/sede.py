from dataclasses import dataclass
from pieza import Pieza

@dataclass()
class Sede:
    """"
    Representa una sede del taller, con información de ubicación y detalles del inventario de piezas
    
    Atributos:
        nombre (str): Nombre de la sede
        inventario (dict): Diccionario inmutable que mapea Pieza a cantidad disponible 
    """
    nombre: str
    inventario: dict[Pieza, int]

    def __post_init__(self):
        if not isinstance(self.inventario, dict):
            raise ValueError("El inventario debe ser un diccionario.")

        # Validación del inventario: las cantidades deben ser no negativas
        for pieza, cantidad in self.inventario.items():
            if not isinstance(pieza, Pieza):
                raise ValueError("El inventario debe contener solo objetos Pieza como claves.")
            if cantidad < 0:
                raise ValueError("Las cantidades en el inventario no pueden ser negativas.")
