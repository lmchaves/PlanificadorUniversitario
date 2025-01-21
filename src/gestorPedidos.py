from dataclasses import dataclass
from pedido import Pedido

@dataclass
class GestorDePedidos:
    sedes: list

    VELOCIDAD = 80
    COSTE_KM = 0.5

    def __init__(self, sedes):
        if not sedes:
            raise ValueError("Debe proporcionarse al menos una sede.")
        self.sedes = sedes

    def calcular_costos_y_tiempos(self, pieza, cantidad, sede_actual):
        """
        Calcula los costos y tiempos para todas las sedes disponibles para una pieza.
        """
        return [
            {
                "sede": sede,
                "costo_total": sede.inventario[pieza].precio_unitario * cantidad +
                               (sede_actual.calcular_distancia(sede) * self.COSTE_KM),
                "tiempo_estimado": sede_actual.calcular_distancia(sede) / self.VELOCIDAD,
            }
            for sede in self.sedes
            if sede.verificar_pieza_disponible(pieza, cantidad)
        ]

    def seleccionar_sedes_optimas(self, piezas_requeridas, sede_actual):
        """
        Selecciona las sedes óptimas para todas las piezas requeridas.

        Args:
            piezas_requeridas (dict): Diccionario con piezas y cantidades.
            sede_actual (Sede): Sede desde donde se hace la solicitud.

        Returns:
            dict: Diccionario donde la clave es la pieza y el valor es la mejor opción para esa pieza.
        """
        sedes_optimas = {}
        for pieza, cantidad in piezas_requeridas.items():
            opciones = self.calcular_costos_y_tiempos(pieza, cantidad, sede_actual)
            mejor_opcion = min(opciones, key=lambda x: x["costo_total"], default=None)
            if mejor_opcion:
                sedes_optimas[pieza] = mejor_opcion
        return sedes_optimas

    def generar_pedidos(self, piezas_requeridas, sede_origen, sedes_optimas):
        """
        Genera una lista de pedidos a partir de las piezas requeridas y sus sedes óptimas.

        Args:
            piezas_requeridas (dict): Piezas y cantidades requeridas.
            sede_origen (Sede): Sede que hace la solicitud.
            sedes_optimas (dict): Sedes seleccionadas previamente como óptimas para cada pieza.

        Returns:
            list: Lista de objetos Pedido con detalles de los pedidos generados.
        """
        pedidos = []
        for pieza, cantidad in piezas_requeridas.items():
            if pieza in sedes_optimas:
                mejor_opcion = sedes_optimas[pieza]
                pedidos.append(Pedido(
                    piezas_requeridas={pieza: cantidad},
                    nombre_sede_origen=sede_origen.nombre,
                    nombre_sede_destino=mejor_opcion["sede"].nombre,
                    tiempo_estimado_llegada=mejor_opcion["tiempo_estimado"],
                    costo_total=mejor_opcion["costo_total"]
                ))
        return pedidos
