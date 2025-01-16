# datos_sedes.py
import pandas as pd
import os
from sede import Sede, crear_inventario

# Cargar los datos de las sedes
script_dir = os.path.dirname(__file__) # Obtiene el directorio del script actual
file_path_mal = os.path.join(script_dir, '../docs/precios/Malaga_precios.xlsx')
file_path_cor = os.path.join(script_dir, '../docs/precios/Cordoba_precios.xlsx')
file_path_jae = os.path.join(script_dir, '../docs/precios/Jaen_precios.xlsx')

datos_malaga = pd.read_excel(file_path_mal)
datos_cordoba = pd.read_excel(file_path_cor)
datos_jaen = pd.read_excel(file_path_jae)


# Crear inventarios
cantidad_fija = 100
inventario_malaga = crear_inventario(datos_malaga, cantidad_fija)
inventario_cordoba = crear_inventario(datos_cordoba, cantidad_fija)
inventario_jaen = crear_inventario(datos_jaen, cantidad_fija)

# Crear sedes
sede_malaga = Sede(
    nombre="Málaga",
    ubicacion_latitude=36.7213,
    ubicacion_longitude=-4.4213,
    inventario=inventario_malaga
)

sede_cordoba = Sede(
    nombre="Córdoba",
    ubicacion_latitude=37.8481,
    ubicacion_longitude=-4.7946,
    inventario=inventario_cordoba
)

sede_jaen = Sede(
    nombre="Jaén",
    ubicacion_latitude=38.0360,
    ubicacion_longitude=-4.0599,
    inventario=inventario_jaen
)

sede_principal = Sede(
    nombre="Lopez Rodriguez Manuel",
    ubicacion_latitude=36.8345,
    ubicacion_longitude=-2.4515,
    inventario={}
)
