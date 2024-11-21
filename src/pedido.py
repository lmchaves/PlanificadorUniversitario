"""
Este módulo define las clases relacionadas con los pedidos,
incluyendo sus estados y los detalles del pedido.
"""

from enum import Enum
from pieza import Pieza
from sede import Sede

class EstadoPedido(Enum):
    """
    Representa los posibles estados de un pedido.
    """
    PENDIENTE_DE_ENVIO = 1
    EN_TRANSITO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Pedido:
    """
    Representa un pedido de piezas entre dos sedes como un objeto inmutable.

    Atributos:
        __piezas_requeridas (dict[Pieza, int]): Diccionario de piezas requeridas y sus cantidades.
        __sede_origen (Sede): Sede desde donde se envían las piezas.
        _sede_destino (Sede): Sede a la que se envían las piezas.
        __estado (EstadoPedido): Estado actual del pedido.
        __tiempo_estimado_llegada (float): Tiempo estimado para que la pieza llegue a la sede destino (en horas).
        __costo_transporte (float): Costo del traslado basado en distancia
    """
    def __init__(self, piezas_requeridas: dict[Pieza, int], sede_origen: Sede, sede_destino: Sede, estado: EstadoPedido, tiempo_estimado_llegada: float, costo_transporte: float):
        if tiempo_estimado_llegada <= 0:
            raise ValueError("El tiempo estimado de llegada debe ser mayor que cero.")
        if costo_transporte <= 0:
            raise ValueError("El costo del transporte debe ser mayor que cero.")
        if sede_origen == sede_destino:
            raise ValueError("La sede de origen y la sede de destino deben ser diferentes.")
        if not piezas_requeridas:
            raise ValueError("El pedido debe tener al menos una pieza requerida.")
        # Validacion de cantidades
        for pieza, cantidad in piezas_requeridas.items():
            if cantidad <= 0:
                raise ValueError(f"La cantidad de la pieza '{pieza.descripcion}' debe ser mayor que cero.")
            

        self.__piezas_requeridas = piezas_requeridas
        self.__sede_origen = sede_origen
        self.__sede_destino = sede_destino
        self.__estado = estado
        self.__tiempo_estimado_llegada = tiempo_estimado_llegada
        self.__costo_transporte = costo_transporte
