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
        inventario (dict[Pieza, int]): Diccionario que mapea el objeto pieza y su cantidad.
    """
    nombre: str
    ubicacion_latitude: float
    ubicacion_longitude: float
    inventario: dict[Pieza, int]
    # inventario (dict[str, tuple[int, float]]):

    def __post_init__(self):
        if not isinstance(self.inventario, dict):
            raise ValueError("El inventario debe ser un diccionario.")

        # Validación de la ubicación: las coordenadas deben estar en [-90, 90] para la latitud y [-180, 180] para la longitud.
        if self.ubicacion_latitude < -90 or self.ubicacion_latitude > 90:
            raise ValueError("La latitud debe estar en el rango [-90, 90].")
        if self.ubicacion_longitude < -180 or self.ubicacion_longitude > 180:
            raise ValueError("La longitud debe estar en el rango [-180, 180].")

        # Validación del inventario: las cantidades deben ser no negativas.
        for pieza, (cantidad, _) in self.inventario.items():
            if cantidad < 0:
                raise ValueError("Las cantidades de la pieza " + pieza + " en el inventario no pueden ser negativas.")
