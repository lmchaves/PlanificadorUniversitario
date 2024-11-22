from dataclasses import dataclass

@dataclass()
class Transporte:
    """
    Representa los tipos de transporte disponibles para el traslado de piezas.

    Atributos:
      costo_por_km (float): Costo en euros por kilómetro de transporte
      tiempo_por_km (float): Tiempo en horas por kilómetro de transporte
        
    Restricciones:
      - costo_por_km debe ser mayor que cero
      - tiempo_por_km debe ser mayor que cero
    """

    costo_por_km: float
    tiempo_por_km: float

    def __post_init__(self):
        if self.costo_por_km <= 0:
            raise ValueError("El costo por kilómetro debe ser mayor que cero.")
        if self.tiempo_por_km <= 0:
            raise ValueError("El tiempo por kilómetro debe ser mayor que cero.")
