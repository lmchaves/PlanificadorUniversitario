class Sede:
    """"
    Representa una sede del taller, con información de ubicación y detalles del inventario de piezas
    
    Atributos:
      sede_id (int): Identificador único de la sede
      ubicacion (str): Ubicación geográfica de la sede
      inventario (list): Lista de piezas disponibles en la sede
    """
    def __init__(self, sede_id: int, ubicacion: str, inventario: list):
        """Inicializa una nueva instancia de la clase Sede"""
        self.sede_id = sede_id
        self.ubicacion = ubicacion
        self.inventario = inventario

