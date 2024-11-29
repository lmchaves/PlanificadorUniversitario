from dataclasses import dataclass
from pieza import Pieza

@dataclass()
class Sede:
    """
    Representa una sede del taller, con información de ubicación y detalles del inventario de piezas.
    
    Atributos:
        nombre (str): Nombre de la sede.
        ubicacion_latitude (float): Latitud de la ubicación de la sede.
        ubicacion_longitude (float): Longitud de la ubicación de la sede.
        catalogo (list[Pieza]): Catálogo de piezas que se pueden solicitar en esta sede.
        inventario (dict[str, int]): Diccionario que mapea nombres de piezas a sus cantidades disponibles.
    """
    nombre: str
    ubicacion_latitude: float
    ubicacion_longitude: float
    catalogo: list[Pieza]
    inventario: dict[str, int]

    def __post_init__(self):
        if not isinstance(self.inventario, dict):
            raise ValueError("El inventario debe ser un diccionario.")

        # Validación de la ubicación: las coordenadas deben estar en [-90, 90] para la latitud y [-180, 180] para la longitud.
        if self.ubicacion_latitude < -90 or self.ubicacion_latitude > 90:
            raise ValueError("La latitud debe estar en el rango [-90, 90].")
        if self.ubicacion_longitude < -180 or self.ubicacion_longitude > 180:
            raise ValueError("La longitud debe estar en el rango [-180, 180].")

        # Validación del inventario: las cantidades deben ser no negativas.
        for pieza, cantidad in self.inventario.items():
            if not isinstance(pieza, Pieza):
                raise ValueError("El inventario debe contener solo nombres de pieza como claves.")
            if cantidad < 0:
                raise ValueError("Las cantidades en el inventario no pueden ser negativas.")

