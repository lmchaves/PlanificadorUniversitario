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

    def __post_init__(self):
        if self.tiempo_estimado_llegada <= 0:
            raise ValueError("El tiempo estimado de llegada debe ser mayor que cero.")
        if self.costo_transporte <= 0:
            raise ValueError("El costo del transporte debe ser mayor que cero.")
        if not self.piezas_requeridas:
            raise ValueError("El pedido debe tener al menos una pieza requerida.")
        # Validacion de cantidades
        for pieza, cantidad in self.piezas_requeridas.items():
            if cantidad <= 0:
                raise ValueError(f"La cantidad de la pieza '{pieza}' debe ser mayor que cero.")
            
def realizar_pedido(sede_origen, sede_destino, piezas_requeridas, distancia):
    """
    Realiza un pedido entre dos sedes.

    Args:
        sede_origen (Sede): Sede desde donde se envían las piezas.
        sede_destino (Sede): Sede a la que se envían las piezas.
        piezas_requeridas (dict[str, int]): Diccionario con las piezas requeridas y sus cantidades.
        distancia: la distancia entre una sede origen y destino

    Returns:
        Pedido: Objeto representando el pedido realizado.
    """
    coste_km = 0.5
    velocidad= 80  
    distancia = sede_origen.calcular_distancia(sede_destino)
    
    costo_transporte = distancia * coste_km
    
    pedido = Pedido(
        piezas_requeridas=piezas_requeridas,
        nombre_sede_origen=sede_origen.nombre,
        nombre_sede_destino=sede_destino.nombre,
        tiempo_estimado_llegada=distancia / velocidad,  
        costo_transporte=costo_transporte
    )
    return pedido

            
def seleccionar_sede_optima(piezas_requeridas, sedes, sede_actual):
    pedidos = []
    for pieza, cantidad_requerida in piezas_requeridas.items():
        opciones = []
        for sede in sedes:
            if pieza in sede.inventario and sede.inventario[pieza][0] >= cantidad_requerida:
                distancia = sede_actual.calcular_distancia( sede)
                costo_pieza = sede.inventario[pieza][1] * cantidad_requerida
                costo_transporte = distancia * 0.5  
                opciones.append((sede, costo_pieza + costo_transporte, distancia))
        
        if opciones:
            sede_optima = min(opciones, key=lambda x: x[1])
            pedidos.append({
                "pieza": pieza,
                "cantidad": cantidad_requerida,
                "sede": sede_optima[0].nombre,
                "costo_total": sede_optima[1],
                "distancia": sede_optima[2]
            })
    return pedidos

