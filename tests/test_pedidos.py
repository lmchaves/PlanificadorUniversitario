import pytest
from sede  import Sede, InventarioItem

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
        nombre="Principal",
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

def test_seleccionar_sede_optima_por_pieza(setup_data):
    sedes, sede_principal, piezas_requeridas = setup_data

    resultado = Sede.seleccionar_sede_optima(piezas_requeridas, sedes, sede_principal)

    assert len(resultado) == 3, f"Se esperaba 3 piezas, pero obtuve {len(resultado)}"

    pedido_motor = next((p for p in resultado if p["pieza"] == "Motor"), None)
    assert pedido_motor is not None, "No se encontró el pedido para 'Motor'"
    assert pedido_motor["cantidad"] == 3, f"Se esperaba 3 motores, pero se obtuvo {pedido_motor['cantidad']}"
    assert pedido_motor["sede_origen"] == "Córdoba", f"Se esperaba que la sede origen fuera 'Córdoba', pero fue {pedido_motor['sede_origen']}"

    pedido_alternador = next((p for p in resultado if p["pieza"] == "Alternador"), None)
    assert pedido_alternador is not None, "No se encontró el pedido para 'Alternador'"
    assert pedido_alternador["cantidad"] == 2, f"Se esperaba 2 alternadores, pero se obtuvo {pedido_alternador['cantidad']}"
    assert pedido_alternador["sede_origen"] == "Córdoba", f"Se esperaba que la sede origen fuera 'Córdoba', pero fue {pedido_alternador['sede_origen']}"

    pedido_correa = next((p for p in resultado if p["pieza"] == "Correa de distribución"), None)
    assert pedido_correa is not None, "No se encontró el pedido para 'Correa de distribución'"
    assert pedido_correa["cantidad"] == 1, f"Se esperaba 1 correa de distribución, pero se obtuvo {pedido_correa['cantidad']}"
    assert pedido_correa["sede_origen"] == "Málaga", f"Se esperaba que la sede origen fuera 'Málaga', pero fue {pedido_correa['sede_origen']}"


def test_calcular_costos_hora(setup_data):
    sedes, sede_principal, piezas_requeridas = setup_data

    resultado = Sede.seleccionar_sede_optima(piezas_requeridas, sedes, sede_principal)

    for pedido in resultado:
        assert pedido["costo_transporte"] > 0, "El costo total debe ser mayor a cero"
        assert pedido["tiempo_estimado"] > 0, "La hora debe ser mayor a cero"
        
        


def test_piezas_no_disponibles(setup_data):
    sedes, sede_actual, _ = setup_data

    piezas_requeridas_no_disponibles = {"pieza_d": 1}  
    resultado = Sede.seleccionar_sede_optima(piezas_requeridas_no_disponibles, sedes, sede_actual)

    assert resultado == []

