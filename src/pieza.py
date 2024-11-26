from dataclasses import dataclass

@dataclass(frozen=True)
class PiezaCaracteristica:
    """
    Representa una pieza específica dentro del inventario de una sede.

    Atributos:
        descripcion (str): Descripción detallada de la pieza.
        categoria_costo (dict): Diccionario que relaciona la categoría con el costo unitario de la pieza.

    Restricciones:
        - costo debe ser positivo
    """
    descripcion: str
    categoria_costo: dict[str, float]

    def __post_init__(self):
        if not self.descripcion or not self.categoria_costo:
            raise ValueError("Descripción, categoría_costo y tipo de vehículo no pueden estar vacíos.")

@dataclass
class PiezaInventario:
    """
    Entidad que representa una pieza en el inventario de una sede (entidad).

    Atributos:
        caracteristicas (PiezaCaracteristica): Características de la pieza (objeto valor).
        cantidad (int): Cantidad disponible en el inventario.
        nomnbre_sede (str): Ubicación actual de la pieza.
    """
    caracteristicas: PiezaCaracteristica
    cantidad: int
    nombre_sede: str

    def __post_init__(self):
        if self.cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        if not self.nombre_sede:
            raise ValueError("La ubicación no puede estar vacía.")
