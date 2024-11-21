from enum import Enum

class TipoTransporte(Enum):
    """
    Representa los tipos de transporte disponibles para el traslado de piezas.

    Atributos:
      URGENTE: Tipo de transporte urgente
      ESTANDAR: Tipo de transporte estandar
      ECONOMICO: Tipo de transporte economico 
    """
    URGENTE = 1
    ESTANDAR = 2
    ECONOMICO = 3

class Transporte:
    """
    Representa los tipos de transporte disponibles para el traslado de piezas.

    Atributos:
      __tipo (TipoTransporte): Tipo de transporte
      __costo_por_km (float): Costo en euros por kilómetro de transporte
      __tiempo_por_km (float): Tiempo en horas por kilómetro de transporte
        
    Restricciones:
      - costo_por_km debe ser mayor que cero
      - tiempo_por_km debe ser mayor que cero
    """
    def __init__(self, tipo: TipoTransporte, costo_por_km: float, tiempo_por_km: float):
        """
        Inicializa una nueva instancia de la clase Transporte
        """
        self.__tipo = tipo
        self.__costo_por_km = max(0.01, costo_por_km)  # Restricción: costo > 0
        self.__tiempo_por_km = max(0.01, tiempo_por_km)  # Restricción: tiempo por km > cero
