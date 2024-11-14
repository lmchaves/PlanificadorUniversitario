class Pieza:
    """
    Representa una pieza específica dentro del inventario de una sede.

    Atributos:
        pieza_id (int): Identificador único de la pieza.
        nombre (str): Nombre descriptivo de la pieza.
        cantidad (int): Cantidad disponible en inventario. Debe ser no negativa.
        ubicacion_en_sede (str): Ubicación física dentro de la sede.
        costo (float): Costo unitario de la pieza. Debe ser positivo.

    Restricciones:
        - cantidad no negativa
        - costo debe ser positivo
    """
    def __init__(self, pieza_id: int, nombre: str, cantidad: int, ubicacion_en_sede: str, costo: float):
        """
        Inicializa una nueva instancia de la clase Pieza.
        """
        self.pieza_id = pieza_id
        self.nombre = nombre
        self.cantidad = max(0, cantidad)  # Restricción: cantidad no negativa
        self.ubicacion_en_sede = ubicacion_en_sede
        self.costo = max(0.01, costo)  # Restricción: costo debe ser positivo

    