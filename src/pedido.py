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
    Representa un pedido de piezas entre dos sedes.

    Atributos:
        pedido_id (int): Identificador único del pedido.
        piezas_requeridas (list[Pieza]): Piezas que se necesitan enviar.
        sede_origen (Sede): Sede desde donde se envían las piezas.
        sede_destino (Sede): Sede a la que se envían las piezas.
        estado (EstadoPedido): Estado actual del pedido.
        tiempo_estimado_llegada (float): Tiempo estimado para que la pieza llegue a la sede destino (en horas).
        costo_transporte (float): Costo del traslado basado en distancia
    """
    def __init__(self, pedido_id: int, piezas_requeridas: list[Pieza], sede_origen: Sede, sede_destino: Sede, estado: EstadoPedido, tiempo_estimado_llegada: float, costo_transporte: float):
        self.pedido_id = pedido_id
        self.piezas_requeridas = piezas_requeridas
        self.sede_origen = sede_origen
        self.sede_destino = sede_destino
        self.estado = estado
        self.tiempo_estimado_llegada = tiempo_estimado_llegada
        self.costo_transporte = costo_transporte
