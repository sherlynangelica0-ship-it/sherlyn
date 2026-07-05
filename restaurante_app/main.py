from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante("Sabor Casero")

# Crear productos
hamburguesa = Producto("Hamburguesa", 5.50)
pizza = Producto("Pizza", 8.00)
jugo = Producto("Jugo Natural", 2.25)

# Agregar productos
restaurante.agregar_producto(hamburguesa)
restaurante.agregar_producto(pizza)
restaurante.agregar_producto(jugo)

# Registrar clientes
juan = Cliente("Juan Pérez")
maria = Cliente("María López")

restaurante.registrar_cliente(juan)
restaurante.registrar_cliente(maria)

# Mostrar información
print(f"Restaurante: {restaurante.nombre}\n")

restaurante.mostrar_productos()
print()
restaurante.mostrar_clientes()