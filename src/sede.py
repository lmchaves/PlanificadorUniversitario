from dataclasses import dataclass
from pieza import Pieza

@dataclass(frozen=True)
class Ubicacion:
    """"
    Representa una ubicación geográfica como un objeto valor inmutable, con latitud y longitud.
    
    Atributos:
        latitude (float): Latitud de la ubicación
        longitude (float): Longitud de la ubicación
    """
    latitude: float
    longitude: float

    def __post_init__(self):
        # Validación de la ubicación: las coordenadas deben estar en [-90, 90]
        if self.latitude < -90 or self.latitude > 90:
            raise ValueError("La latitud debe estar en [-90, 90].")
        if self.longitude < -180 or self.longitude > 180:
            raise ValueError("La longitud debe estar en [-180, 180].")

@dataclass()
class Sede:
    """"
    Representa una sede del taller, con información de ubicación y detalles del inventario de piezas
    
    Atributos:
        nombre (str): Nombre de la sede
        ubicacion (Ubicacion): Ubicación geográfica de la sede
        inventario (dict): Diccionario inmutable que mapea Pieza a cantidad disponible 
    """
    nombre: str
    ubicacion: Ubicacion
    inventario: dict[Pieza, int]

    def __post_init__(self):
        if not isinstance(self.inventario, dict):
            raise ValueError("El inventario debe ser un diccionario.")

        # Validación de la ubicación
        if not isinstance(self.ubicacion, Ubicacion):
            raise ValueError("La ubicación debe ser un objeto Ubicación.")

        # Validación del inventario: las cantidades deben ser no negativas
        for pieza, cantidad in self.inventario.items():
            if not isinstance(pieza, Pieza):
                raise ValueError("El inventario debe contener solo objetos Pieza como claves.")
            if cantidad < 0:
                raise ValueError("Las cantidades en el inventario no pueden ser negativas.")
