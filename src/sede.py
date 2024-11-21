from pieza import Pieza

class Sede:
    """"
    Representa una sede del taller, con información de ubicación y detalles del inventario de piezas
    
    Atributos:
      sede_id (int): Identificador único de la sede
      nombre (str): Nombre descriptivo de la sede
      ubicacion (str): Ubicación geográfica de la sede
      inventario (dict): Diccionario que almacena las piezas y sus cantidades
    """
    def __init__(self, sede_id: int, nombre: str , ubicacion: str, inventario: dict[Pieza, int]):
        """Inicializa una nueva instancia de la clase Sede"""
        self.sede_id = sede_id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.inventario = inventario or {}  #  Diccionario donde la clave es la pieza y el valor es la cantidad
