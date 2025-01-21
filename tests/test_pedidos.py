import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from sede import Sede, InventarioItem  # Ahora debería funcionar
from gestorPedidos import GestorDePedidos


@pytest.fixture
def setup_data():
    inventario_malaga = {
        "Motor": InventarioItem(cantidad=5, precio_unitario=3100.0),
        "Correa de distribución": InventarioItem(cantidad=3, precio_unitario=75.0),
    }
    
    inventario_cordoba = {
        "Motor": InventarioItem(cantidad=10, precio_unitario=3050.0),
        "Alternador": InventarioItem(cantidad=4, precio_unitario=240.0),
    }

    inventario_jaen = {
        "Alternador ": InventarioItem(cantidad=5, precio_unitario=230.0),
        "Correa de distribución": InventarioItem(cantidad=2, precio_unitario=70.0),
    }

    inventario_principal = {}

    sede_malaga = Sede(
        nombre="Málaga",
        ubicacion_latitude=36.721,
        ubicacion_longitude=-4.421,
        inventario=inventario_malaga,
    )
    sede_cordoba = Sede(
        nombre="Córdoba",
        ubicacion_latitude=37.888,
        ubicacion_longitude=-4.779,
        inventario=inventario_cordoba,
    )
    sede_jaen = Sede(
        nombre="Jaén",
        ubicacion_latitude=37.779,
        ubicacion_longitude=-3.784,
        inventario=inventario_jaen,
    )
    sede_principal = Sede(
        nombre="Lopez Rodriguez Manuel",
        ubicacion_latitude=37.000,
        ubicacion_longitude=-4.500,
        inventario=inventario_principal,
    )

    piezas_requeridas = {
        "Motor": 3,
        "Alternador": 2,
        "Correa de distribución": 1,
    }

    return [sede_malaga, sede_cordoba, sede_jaen], sede_principal, piezas_requeridas

def test_seleccionar_sede_optima(setup_data):
    sedes, sede_principal, piezas_requeridas = setup_data
    
    gestor = GestorDePedidos(sedes)

    sedes_optimas = gestor.seleccionar_sedes_optimas(piezas_requeridas, sede_principal)

    assert "Motor" in sedes_optimas, "No se encontró una sede óptima para 'Motor'"
    assert sedes_optimas["Motor"]["sede"].nombre == "Córdoba", f"Se esperaba 'Córdoba' para 'Motor', pero fue {sedes_optimas['Motor']['sede'].nombre}"

    assert "Alternador" in sedes_optimas, "No se encontró una sede óptima para 'Alternador'"
    assert sedes_optimas["Alternador"]["sede"].nombre == "Córdoba", f"Se esperaba 'Córdoba' para 'Alternador', pero fue {sedes_optimas['Alternador']['sede'].nombre}"

    assert "Correa de distribución" in sedes_optimas, "No se encontró una sede óptima para 'Correa de distribución'"
    assert sedes_optimas["Correa de distribución"]["sede"].nombre == "Málaga", f"Se esperaba 'Málaga' para 'Correa de distribución', pero fue {sedes_optimas['Correa de distribución']['sede'].nombre}"
    
def test_generar_pedidos(setup_data):
    sedes, sede_principal, piezas_requeridas = setup_data

    gestor = GestorDePedidos(sedes)

    sedes_optimas = gestor.seleccionar_sedes_optimas(piezas_requeridas, sede_principal)

    resultado = gestor.generar_pedidos(piezas_requeridas, sede_principal, sedes_optimas)

    pedido_motor = next((p for p in resultado if "Motor" in p.piezas_requeridas), None)
    assert pedido_motor is not None, "No se encontró el pedido para 'Motor'"
    assert pedido_motor.piezas_requeridas["Motor"] == 3, f"Se esperaba 3 motores, pero se obtuvo {pedido_motor.piezas_requeridas['Motor']}"
    assert pedido_motor.nombre_sede_destino == "Córdoba", f"Se esperaba que la sede destino fuera 'Córdoba', pero fue {pedido_motor.nombre_sede_destino}"

    pedido_alternador = next((p for p in resultado if "Alternador" in p.piezas_requeridas), None)
    assert pedido_alternador is not None, "No se encontró el pedido para 'Alternador'"
    assert pedido_alternador.piezas_requeridas["Alternador"] == 2, f"Se esperaba 2 alternadores, pero se obtuvo {pedido_alternador.piezas_requeridas['Alternador']}"
    assert pedido_alternador.nombre_sede_destino == "Córdoba", f"Se esperaba que la sede destino fuera 'Córdoba', pero fue {pedido_alternador.nombre_sede_destino}"

    pedido_correa = next((p for p in resultado if "Correa de distribución" in p.piezas_requeridas), None)
    assert pedido_correa is not None, "No se encontró el pedido para 'Correa de distribución'"
    assert pedido_correa.piezas_requeridas["Correa de distribución"] == 1, f"Se esperaba 1 correa de distribución, pero se obtuvo {pedido_correa.piezas_requeridas['Correa de distribución']}"
    assert pedido_correa.nombre_sede_destino == "Málaga", f"Se esperaba que la sede destino fuera 'Málaga', pero fue {pedido_correa.nombre_sede_destino}"

def test_calcular_costos_hora(setup_data):
    sedes, sede_principal, piezas_requeridas = setup_data
    gestor = GestorDePedidos(sedes)
    
    sedes_optimas = gestor.seleccionar_sedes_optimas(piezas_requeridas, sede_principal)

    resultado = gestor.generar_pedidos(piezas_requeridas, sede_principal, sedes_optimas)

    for pedido in resultado:
        assert pedido.costo_total > 0, "El costo total debe ser mayor a cero"
        assert pedido.tiempo_estimado_llegada > 0, "El tiempo estimado debe ser mayor a cero"