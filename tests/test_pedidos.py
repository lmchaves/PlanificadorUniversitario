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

def test_realizar_pedido(setup_data):
    sede_principal, piezas_requeridas = setup_data
    
    # Prueba de creación del pedido
    pedido = realizar_pedido(sede_principal, sede_jaen, piezas_requeridas)
    
    assert isinstance(pedido, Pedido), "El pedido no es de tipo Pedido"
    assert pedido.nombre_sede_origen == "Lopez Rodriguez Manuel", f"Esperaba 'Lopez Rodriguez Manuel', pero obtuve {pedido.nombre_sede_origen}"
    assert pedido.nombre_sede_destino == "Jaén", f"Esperaba 'Jaén', pero obtuve {pedido.nombre_sede_destino}"
    assert pedido.piezas_requeridas == piezas_requeridas, "Las piezas requeridas no coinciden"
    assert pedido.tiempo_estimado_llegada > 0, "El tiempo estimado de llegada debería ser mayor que cero"
    assert pedido.costo_transporte > 0, "El costo de transporte debería ser mayor que cero"

def test_inventario_post_pedido(setup_data):
    sede_principal, piezas_requeridas = setup_data
    
    realizar_pedido(sede_principal, sede_jaen, piezas_requeridas)
    
    inventario_principal = sede_principal.get_inventario()
    piezas_en_inventario = [pieza for pieza in piezas_requeridas.keys() if pieza in inventario_principal]
    
    assert len(piezas_en_inventario) == len(piezas_requeridas), "No todas las piezas están presentes en el inventario"
    assert len(inventario_principal) >= len(piezas_requeridas), "El inventario debería haber aumentado con las piezas solicitadas"

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

