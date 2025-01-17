import pytest
from pedido import seleccionar_sede_optima
from sede  import Sede

@pytest.fixture
def setup_data():
    inventario_malaga = {
        "Motor": (5, 3100),
        "Correa de distribución": (3, 75),
    }
    inventario_cordoba = {
        "Motor": (10, 3050),
        "Alternador": (4, 240),
    }
    inventario_jaen = {
        "Alternador": (5, 3150),
        "Correa de distribución": (2, 70),
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

    resultado = seleccionar_sede_optima(piezas_requeridas, sedes, sede_principal)

    assert len(resultado) == 3, f"Se esperaba 3 piezas, pero obtuve {len(resultado)}"

    pedido_motor = next((p for p in resultado if "Motor" in p.piezas_requeridas), None)
    assert pedido_motor is not None, "No se encontró el pedido para 'Motor'"
    assert pedido_motor.piezas_requeridas["Motor"] == 3, f"Se esperaba 3 motores, pero obtuve {pedido_motor.piezas_requeridas['Motor']}"
    assert pedido_motor.nombre_sede_destino == "Córdoba", f"Se esperaba que la sede fuera 'Córdoba', pero obtuve {pedido_motor.nombre_sede_destino}"



    pedido_alternador = next((p for p in resultado if "Alternador" in p.piezas_requeridas), None)
    assert pedido_alternador is not None,  "No se encontró el pedido para 'Alternador'"
    assert pedido_alternador.piezas_requeridas["Alternador"] == 2,f"Se esperaba 3 alnernadores, pero obtuve {pedido_alternador.piezas_requeridas['Alternador']}"
    assert pedido_alternador.nombre_sede_destino in [ "Córdoba"], f"Se esperaba que la sede fuera 'Córdoba', pero obtuve {pedido_alternador.nombre_sede_destino}" 
    

    pedido_Correa = next((p for p in resultado if "Correa de distribución" in p.piezas_requeridas), None)
    assert pedido_Correa is not None,"No se encontró el pedido para 'Correa de distribución'"
    assert pedido_Correa.piezas_requeridas["Correa de distribución"] == 1,f"Se esperaba 1 correa de distribución, pero obtuve {pedido_Correa.piezas_requeridas['Correa de distribución']}"
    assert pedido_Correa.nombre_sede_destino in ["Málaga"], f"Se esperaba que la sede fuera 'Málaga', pero obtuve {pedido_Correa.nombre_sede_destino}" 


def test_calcular_costos_hora(setup_data):
    sedes, sede_principal, piezas_requeridas = setup_data

    resultado = seleccionar_sede_optima(piezas_requeridas, sedes, sede_principal)

    for pedido in resultado:
        assert pedido.costo_transporte > 0, "El costo total debe ser mayor a cero"
        assert pedido.tiempo_estimado_llegada > 0, "La hora debe ser mayor a cero"


def test_piezas_no_disponibles(setup_data):
    sedes, sede_actual, _ = setup_data

    piezas_requeridas_no_disponibles = {"pieza_d": 1}  
    resultado = seleccionar_sede_optima(piezas_requeridas_no_disponibles, sedes, sede_actual)

    assert resultado == []

