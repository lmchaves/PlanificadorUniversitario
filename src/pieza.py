from dataclasses import dataclass
from sede import Sede
from pieza_caracteristica import PiezaCaracteristica


@dataclass
class PiezaInventario:
    """
    Entidad que representa una pieza en el inventario de una sede (entidad).

    Atributos:
        caracteristicas (PiezaCaracteristica): Características de la pieza (objeto valor).
        cantidad (int): Cantidad disponible en el inventario.
        ubicacion (str): Ubicación actual de la pieza.
    """
    caracteristicas: PiezaCaracteristica
    cantidad: int
    ubicacion: Sede

    def __post_init__(self):
        if self.cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        if not self.ubicacion:
            raise ValueError("La ubicación no puede estar vacía.")
