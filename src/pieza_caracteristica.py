from dataclasses import dataclass

@dataclass(frozen=True)
class PiezaCaracteristica:
    """
    Representa una pieza específica dentro del inventario de una sede.

    Atributos:
        _descripcion (str): Descripción detallada de la pieza.
        _costo (float): Costo unitario de la pieza.
        _categoria (str): Categoría a la que pertenece la pieza (e.g., motor, batería).
        _tipo_vehiculo (str): Tipo de vehículo al que corresponde la pieza.

    Restricciones:
        - costo debe ser positivo
    """
    _descripcion: str
    _costo: float
    _categoria: str
    _tipo_vehiculo: str

    def __post_init__(self):
        if self._costo <= 0:
            raise ValueError("El costo debe ser mayor que 0.")
        if not self._descripcion or not self._categoria or not self._tipo_vehiculo:
            raise ValueError("Descripción, categoría y tipo de vehículo no pueden estar vacíos.")
