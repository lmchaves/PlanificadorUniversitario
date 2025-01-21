from dataclasses import dataclass
from math import radians, sin, cos, sqrt, atan2
from typing import NamedTuple

class InventarioItem(NamedTuple):
    cantidad: int
    precio_unitario: float

LATIUD=90
LONGITUD=180

@dataclass()
class Sede:
    """
    Representa una sede del taller, con información de ubicación y detalles del inventario de piezas.

    Atributos:
        nombre (str): Nombre de la sede.
        ubicacion_latitude (float): Latitud de la ubicación de la sede.
        ubicacion_longitude (float): Longitud de la ubicación de la sede.
        inventario (dict[Pieza, int]): Diccionario que mapea el nombre de la pieza pieza 
        (única fuente de verdad) su cantidad y el costo unitario.
    """
    nombre: str
    ubicacion_latitude: float
    ubicacion_longitude: float
    inventario: dict[str, InventarioItem]
    
    RADIO_TIERRA_KM  = 6371.0 
<<<<<<< HEAD
    VELOCIDAD= 80  
    COSTE_KM=0.5
=======
>>>>>>> 58ddb7d (fix #26 #34: eliminamos las funciones estaticas)

    def __post_init__(self):
        if not isinstance(self.inventario, dict):
            raise ValueError("El inventario debe ser un diccionario.")

        if self.ubicacion_latitude < -LATIUD or self.ubicacion_latitude > LATIUD:
            raise ValueError("La latitud debe estar en el rango [-90, 90].")
        if self.ubicacion_longitude < -LONGITUD or self.ubicacion_longitude > LONGITUD:
            raise ValueError("La longitud debe estar en el rango [-180, 180].")

        for pieza, item in self.inventario.items():
            if not isinstance(item, InventarioItem):
                raise ValueError(f"El valor asociado a la pieza {pieza} debe ser un InventarioItem.")
            if item.cantidad < 0:
                raise ValueError(f"La cantidad de la pieza {pieza} no puede ser negativa.")
            

    def calcular_distancia(self, otra_sede: 'Sede') -> float:
        """
        Calcula la distancia entre la sede actual y otra sede utilizando la fórmula del haversine.

        Args:
            otra_sede (Sede): La otra sede.

        Returns:
            float: Distancia en kilómetros.
        """
         

        dlat = radians(otra_sede.ubicacion_latitude - self.ubicacion_latitude)
        dlon = radians(otra_sede.ubicacion_longitude - self.ubicacion_longitude)
        factor_distancia_angular = sin(dlat / 2) ** 2 + cos(radians(self.ubicacion_latitude)) * cos(radians(otra_sede.ubicacion_latitude)) * sin(dlon / 2) ** 2
        angulo_central = 2 * atan2(sqrt(factor_distancia_angular), sqrt(1 - factor_distancia_angular))
        distancia = Sede.RADIO_TIERRA_KM * angulo_central

        return distancia
    
    def verificar_pieza_disponible(self, pieza: str, cantidad_requerida: int) -> bool:
        """
        Verifica si la sede tiene una cantidad suficiente de una pieza específica.

        Args:
            pieza (str): Nombre de la pieza a verificar.
            cantidad_requerida (int): Cantidad requerida de la pieza.

        Returns:
            bool: True si la pieza está disponible en cantidad suficiente, False en caso contrario.
        """
        if pieza in self.inventario:
            item = self.inventario[pieza]
            return item.cantidad >= cantidad_requerida
        return False