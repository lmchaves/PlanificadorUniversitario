"""
Este módulo define las clases relacionadas con los pedidos,
incluyendo sus estados y los detalles del pedido.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Pedido:
    """
    Representa un pedido de piezas entre dos sedes como un objeto inmutable.

    Atributos:
        piezas_requeridas (dict[str, int]): Diccionario de nombre de piezas requeridas y sus cantidades.
        sede_origen (Sede): Sede desde donde se envían las piezas.
        sede_destino (Sede): Sede a la que se envían las piezas.
        tiempo_estimado_llegada (float): Tiempo estimado para que la pieza llegue a la sede destino (en horas).
        costo_transporte (float): Costo del traslado basado en distancia
    """
    piezas_requeridas: dict[str, int]
    nombre_sede_origen: str
    nombre_sede_destino: str
    tiempo_estimado_llegada: float
    costo_transporte: float
    
    VELOCIDAD= 80  


    def __post_init__(self):
        if self.tiempo_estimado_llegada <= 0:
            raise ValueError("El tiempo estimado de llegada debe ser mayor que cero.")
        if self.costo_transporte <= 0:
            raise ValueError("El costo del transporte debe ser mayor que cero.")
        if not self.piezas_requeridas:
            raise ValueError("El pedido debe tener al menos una pieza requerida.")
        for pieza, cantidad in self.piezas_requeridas.items():
            if cantidad <= 0:
                raise ValueError(f"La cantidad de la pieza '{pieza}' debe ser mayor que cero.")
            

def seleccionar_sede_optima(piezas_requeridas, sedes, sede_actual):
    pedidos = []

    for pieza, cantidad in piezas_requeridas.items():
        opciones = list(
            map(
                lambda sede: {
                    "sede": sede,
                    "costo_total": sede.inventario[pieza][1] * cantidad + sede_actual.calcular_costo_transporte(sede),
                    "distancia": sede_actual.calcular_distancia(sede),
                },
                filter(lambda sede: sede.tiene_pieza_disponible(pieza, cantidad), sedes),
            )
        )

        if opciones:
            mejor_opcion = min(opciones, key=lambda x: x["costo_total"])
            pedidos.append({
                "pieza": pieza,
                "cantidad": cantidad,
                "sede_origen": mejor_opcion["sede"],
                "sede_destino": sede_actual.nombre,
                "costo_transporte": mejor_opcion["costo_total"] - sede_actual.calcular_costo_transporte(mejor_opcion["sede"]),
                "tiempo_estimado": mejor_opcion["distancia"] / Pedido.VELOCIDAD
            })

    return pedidos


