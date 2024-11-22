from dataclasses import dataclass

@dataclass(frozen=True)
class PiezaCaracteristica:
    """
    Representa una pieza específica dentro del inventario de una sede.

    Atributos:
        descripcion (str): Descripción detallada de la pieza.
        categoria_costo (dict): Diccionario que relaciona la categoría con el costo unitario de la pieza.
        tipo_vehiculo (str): Tipo de vehículo al que corresponde la pieza.

    Restricciones:
        - costo debe ser positivo
    """
    descripcion: str
    categoria_costo: dict[str, float]
    tipo_vehiculo: str

    def __post_init__(self):
        if not self.descripcion or not self.categoria_costo or not self.tipo_vehiculo:
            raise ValueError("Descripción, categoría_costo y tipo de vehículo no pueden estar vacíos.")
