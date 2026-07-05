class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        return f"{self.nombre} - ${self.precio:.2f}"
    