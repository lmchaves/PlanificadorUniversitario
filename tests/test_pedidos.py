import pytest
from pedido import seleccionar_sede_optima, realizar_pedido, Pedido
from datos_sedes import sede_malaga, sede_cordoba, sede_jaen, sede_principal

@pytest.fixture
def setup_data():
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

    pedido_motor = next((p for p in resultado if p["pieza"] == "Motor"), None)
    assert pedido_motor is not None, "No se encontró el pedido para 'Motor'"
    assert pedido_motor["cantidad"] == 3, f"Se esperaba 3 motores, pero obtuve {pedido_motor['cantidad']}"
    assert pedido_motor["sede"] == "Córdoba", f"Se esperaba que la sede fuera 'Córdoba', pero obtuve {pedido_motor['sede']}"



    pedido_alternador = next((p for p in resultado if p["pieza"] == "Alternador"), None)
    assert pedido_alternador is not None,  "No se encontró el pedido para 'Alternador'"
    assert pedido_alternador["cantidad"] == 2,f"Se esperaba 3 alnernadores, pero obtuve {pedido_alternador['cantidad']}"
    assert pedido_alternador["sede"] in [ "Jaén"], f"Se esperaba que la sede fuera 'Jaén', pero obtuve {pedido_alternador['sede']}" 
    

    pedido_Correa = next((p for p in resultado if p["pieza"] == "Correa de distribución"), None)
    assert pedido_Correa is not None,"No se encontró el pedido para 'Correa de distribución'"
    assert pedido_Correa["cantidad"] == 1,f"Se esperaba 1 correa de distribución, pero obtuve {pedido_Correa['cantidad']}"
    assert pedido_Correa["sede"] in ["Málaga"], f"Se esperaba que la sede fuera 'Málaga', pero obtuve {pedido_Correa['sede']}" 


def test_calcular_costos_distancias(setup_data):
    sedes, sede_principal, piezas_requeridas = setup_data

    resultado = seleccionar_sede_optima(piezas_requeridas, sedes, sede_principal)

    for pedido in resultado:
        assert pedido["costo_total"] > 0, "El costo total debe ser mayor a cero"
        assert pedido["distancia"] > 0, "La distancia debe ser mayor a cero"


def test_piezas_no_disponibles(setup_data):
    sedes, sede_actual, _ = setup_data

    piezas_requeridas_no_disponibles = {"pieza_d": 1}  
    resultado = seleccionar_sede_optima(piezas_requeridas_no_disponibles, sedes, sede_actual)

    assert resultado == []

