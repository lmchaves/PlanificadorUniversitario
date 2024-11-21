from typing import Any


class Pieza:
    """
    Representa una pieza específica dentro del inventario de una sede.

    Atributos:
        _descripcion (str): Descripción detallada de la pieza.
        _cantidad (int): Cantidad disponible en inventario.
        _ubicacion (str): Ubicación actual de la pieza (sede).
        _costo (float): Costo unitario de la pieza.
        _categoria (str): Categoría a la que pertenece la pieza (e.g., motor, batería).
        _tipo_vehiculo (str): Tipo de vehículo al que corresponde la pieza.
        _es_urgente (bool): Indica si la pieza es necesaria para reparaciones urgentes.

    Restricciones:
        - cantidad no negativa
        - costo debe ser positivo
    """
    def __init__(self, descripcion: str, cantidad: int, ubicacion: str, costo: float, categoria: str, tipo_vehiculo: str, es_urgente: bool):
        # Validaciones para las restricciones
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        if costo <= 0:
            raise ValueError("El costo debe ser mayor que 0.")
        if not descripcion or not categoria or not tipo_vehiculo:
            raise ValueError("Descripción, categoría y tipo de vehículo no pueden estar vacíos.")
        if not ubicacion:
            raise ValueError("La ubicación no puede estar vacía.")

        # Atributos inmutables
        self.__descripcion = descripcion
        self.__cantidad = cantidad
        self.__ubicacion = ubicacion
        self.__costo = costo
        self.__categoria = categoria
        self.__tipo_vehiculo = tipo_vehiculo
        self.__es_urgente = es_urgente
