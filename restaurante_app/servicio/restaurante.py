class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print("=== Menú ===")
        for producto in self.productos:
            print(producto.mostrar_info())

    def mostrar_clientes(self):
        print("=== Clientes ===")
        for cliente in self.clientes:
            print(cliente.mostrar_info())