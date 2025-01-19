from dataclasses import dataclass
from math import radians, sin, cos, sqrt, atan2
from typing import NamedTuple

class InventarioItem(NamedTuple):
    cantidad: int
    precio_unitario: float


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
    VELOCIDAD= 80  
    LATIUD=90
    LONGITUD=180
    COSTE_KM=0.5

    def __post_init__(self):
        if not isinstance(self.inventario, dict):
            raise ValueError("El inventario debe ser un diccionario.")

        if self.ubicacion_latitude < -Sede.LATIUD or self.ubicacion_latitude > Sede.LATIUD:
            raise ValueError("La latitud debe estar en el rango [-90, 90].")
        if self.ubicacion_longitude < -Sede.LONGITUD or self.ubicacion_longitude > Sede.LONGITUD:
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
        a = sin(dlat / 2) ** 2 + cos(radians(self.ubicacion_latitude)) * cos(radians(otra_sede.ubicacion_latitude)) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distancia = Sede.RADIO_TIERRA_KM * c

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
    
    def calcular_costo_transporte(self, sede_destino) -> float:
        """
        Calcula el costo de transporte entre la sede actual y otra sede basado en la distancia.

        Args:
            sede_destino (Sede): La sede de destino a la que se enviarán las piezas.
            coste_km (float): Costo por kilómetro de transporte. Por defecto es 0.5.

        Returns:
            float: El costo de transporte calculado.
        """
        coste_km=0.5
        distancia = self.calcular_distancia(sede_destino)  
        return distancia * coste_km
    
    @staticmethod
    def seleccionar_sede_optima(pieza, cantidad, sedes, sede_actual):
        opciones = [
            {
                "sede": sede,
                "costo_total": sede.inventario[pieza].precio_unitario * cantidad + sede_actual.calcular_costo_transporte(sede),
                "distancia": sede_actual.calcular_distancia(sede),
            }
            for sede in sedes
            if sede.verificar_pieza_disponible(pieza, cantidad)
        ]
        return min(opciones, key=lambda x: x["costo_total"], default=None)
    
    @staticmethod
    def generar_pedidos(piezas_requeridas, sedes, sede_actual):
        pedidos = []
        for pieza, cantidad in piezas_requeridas.items():
            mejor_opcion = Sede.seleccionar_sede_optima(pieza, cantidad, sedes, sede_actual)
            if mejor_opcion:
                pedidos.append({
                    "pieza": pieza,
                    "cantidad": cantidad,
                    "sede_origen": mejor_opcion["sede"].nombre,
                    "sede_destino": sede_actual.nombre,
                    "costo_transporte": mejor_opcion["costo_total"] - mejor_opcion["sede"].inventario[pieza].precio_unitario * cantidad,
                    "tiempo_estimado": mejor_opcion["distancia"] / Sede.VELOCIDAD,
                })
        return pedidos
