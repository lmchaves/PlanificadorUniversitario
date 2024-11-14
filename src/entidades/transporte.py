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
    def __init__(self, costo_por_km: float, tiempo_por_km: float):
        """
        Inicializa una nueva instancia de la clase Transporte
        """
        self.costo_por_km = max(0.01, costo_por_km)  # Restricción: costo > 0
        self.tiempo_por_km = max(0.01, tiempo_por_km)  # Restricción: tiempo por km > cero
