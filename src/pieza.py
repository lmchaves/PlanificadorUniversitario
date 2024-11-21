class Pieza:
    """
    Representa una pieza específica dentro del inventario de una sede.

    Atributos:
        pieza_id (int): Identificador único de la pieza.
        descripcion (str): Descripción detallada de la pieza.
        cantidad (int): Cantidad disponible en inventario.
        ubicacion (str): Ubicación actual de la pieza (sede).
        costo (float): Costo unitario de la pieza.
        categoria (str): Categoría a la que pertenece la pieza (e.g., motor, batería).
        tipo_vehiculo (str): Tipo de vehículo al que corresponde la pieza.
        es_urgente (bool): Indica si la pieza es necesaria para reparaciones urgentes.

    Restricciones:
        - cantidad no negativa
        - costo debe ser positivo
    """
    def __init__(self, pieza_id: int, descripcion: str, cantidad: int, ubicacion: str, costo: float, categoria: str, tipo_vehiculo: str, es_urgente: bool):
        # Restricción: cantidad no negativa
        if cantidad <= 0:
            raise ValueError("La cantidad de piezas debe ser mayor que cero.")
        self.pieza_id = pieza_id
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.ubicacion = ubicacion
        self.costo = max(0.01, costo)  # Restricción: costo > 0
        self.categoria = categoria
        self.tipo_vehiculo = tipo_vehiculo
        self.es_urgente = es_urgente
