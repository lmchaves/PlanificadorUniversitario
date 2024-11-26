from dataclasses import dataclass
from pieza import PiezaInventario

@dataclass(frozen=True)
class SedeInfo:
    """
    Objeto valor que describe las características de una sede.

    Atributos:
        nombre (str): Nombre descriptivo de la sede
        ubicacion (str): Ubicación geográfica de la sede
    """
    nombre: str
    ubicacion: str

@dataclass()
class Sede:
    """"
    Representa una sede del taller, con información de ubicación y detalles del inventario de piezas
    
    Atributos:
        sedeInfo (SedeInfo): Objeto valor que describe las características de la sede
        inventario (dict): Diccionario inmutable que mapea Pieza a cantidad disponible 
    """
    sede_info: SedeInfo
    inventario: dict[PiezaInventario, int]

    def __post_init__(self):
        if not isinstance(self.inventario, dict):
            raise ValueError("El inventario debe ser un diccionario.")

        # Validación del inventario: las cantidades deben ser no negativas
        for pieza, cantidad in self.inventario.items():
            if not isinstance(pieza, PiezaInventario):
                raise ValueError("El inventario debe contener solo objetos Pieza como claves.")
            if cantidad < 0:
                raise ValueError("Las cantidades en el inventario no pueden ser negativas.")
