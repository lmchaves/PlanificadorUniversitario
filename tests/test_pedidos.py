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

    
    # Realizar el pedido
    pedido = realizar_pedido(sede_principal, sede_jaen, piezas_requeridas)
    
    # Validaciones (aserciones)
    assert isinstance(pedido, Pedido)
    assert pedido.nombre_sede_origen == "Lopez Rodriguez Manuel"
    assert pedido.nombre_sede_destino == "Jaén"
    assert pedido.piezas_requeridas == piezas_requeridas
    assert pedido.tiempo_estimado_llegada > 0
    assert pedido.costo_transporte > 0
    
    # Comprobar que las 3 piezas del pedido están ahora en el inventario de la sede principal
    inventario_principal = sede_principal.get_inventario()
    piezas_en_inventario = [pieza for pieza in piezas_requeridas.keys() if pieza in inventario_principal]
    
    # Verificar que el inventario tiene al menos las 3 piezas del pedido
    assert len(piezas_en_inventario) == len(piezas_requeridas)
    assert len(inventario_principal) >= len(piezas_requeridas)  # Verifica que el inventario tiene al menos 3 piezas

def test_seleccionar_sede_optima(setup_data):
    # Desempaquetar los datos de la fixture
    sedes, sede_principal, piezas_requeridas = setup_data

    # Llamar a la función con las sedes y piezas requeridas
    resultado = seleccionar_sede_optima(piezas_requeridas, sedes, sede_principal)

    # Comprobaciones básicas
    assert len(resultado) == 3  # Debe haber 3 pedidos (uno por pieza)

    # Verificar las piezas en los pedidos
    pedido_motor = next((p for p in resultado if p["pieza"] == "Motor"), None)
    assert pedido_motor is not None
    assert pedido_motor["cantidad"] == 3
    assert pedido_motor["sede"] in ["Córdoba"]


    pedido_alternador = next((p for p in resultado if p["pieza"] == "Alternador"), None)
    assert pedido_alternador is not None
    assert pedido_alternador["cantidad"] == 2
    assert pedido_alternador["sede"] in [ "Jaén"]
    

    pedido_Correa = next((p for p in resultado if p["pieza"] == "Correa de distribución"), None)
    assert pedido_Correa is not None
    assert pedido_Correa["cantidad"] == 1
    assert pedido_Correa["sede"] in ["Málaga"]


    # Verificar que los costos sean positivos
    for pedido in resultado:
        assert pedido["costo_total"] > 0
        assert pedido["distancia"] > 0


def test_piezas_no_disponibles(setup_data):
    # Desempaquetar los datos de la fixture
    sedes, sede_actual, _ = setup_data

    # Caso de piezas no disponibles
    piezas_requeridas_no_disponibles = {"pieza_d": 1}  # Pieza no existente
    resultado = seleccionar_sede_optima(piezas_requeridas_no_disponibles, sedes, sede_actual)

    # Comprobar que no se generaron pedidos
    assert resultado == []

