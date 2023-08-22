class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        col_val=["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in col_val:
            self.color=color

