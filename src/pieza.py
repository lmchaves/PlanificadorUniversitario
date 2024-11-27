from dataclasses import dataclass

@dataclass(frozen=True)
class Pieza:
    """
    Representa una pieza específica dentro del inventario de una sede. Objeto valor

    Atributos:
        descripcion (str): Descripción detallada de la pieza.
        categoria_costo (dict): Diccionario que relaciona la categoría con el costo unitario de la pieza.
        En un diccionario ya que la clave categoría debe tener un solo un costo inmutable en el inventario.
        Un objeto valor será igual a otro si sus atributos son iguales.

    Restricciones:
        - costo debe ser positivo
    """
    descripcion: str
    categoria_costo: dict[str, float]

    def __post_init__(self):
        if not self.descripcion or not self.categoria_costo:
            raise ValueError("Descripción y categoría_costo no pueden estar vacíos.")

        for categoria, costo in self.categoria_costo.items():
            if not isinstance(categoria, str):
                raise ValueError("La categoría debe ser una cadena de texto.")
            if costo <= 0:
                raise ValueError("El costo debe ser mayor que cero.")
