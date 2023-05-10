"""System module."""


def get_product(**datos):
    """Funcion que trabaja con datos."""
    print(datos["id"], datos["desc"])


get_product(id="9879", name="iPhone", desc="Esto es un iphone")
