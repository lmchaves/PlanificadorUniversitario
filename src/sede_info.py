from dataclasses import dataclass

@dataclass(frozen=True)
class SedeInfo:
    """
    Objeto valor que describe las características de una sede.

    Atributos:
        nombre (str): Nombre descriptivo de la sede
        ubicacion (str): Ubicación geográfica de la sede
    """
    nombre: str
    ubicacion: str
