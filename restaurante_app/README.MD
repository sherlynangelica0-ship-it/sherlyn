# Sabor casero – Sistema Básico de Gestión de Restaurante

**Autora:** Sherlyn Angélica Vargas Tapuy
**Curso:** Programación Orientada a Objetos
**Actividad:** Taller práctico – Organización modular en Python

## Descripción

Este proyecto consiste en un sistema básico de gestión de un restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO). Su objetivo es demostrar la organización del código en módulos, la separación de responsabilidades entre clases y la comunicación entre archivos mediante importaciones.

El sistema permite registrar productos y clientes del restaurante, almacenarlos y mostrar la información en consola.

## Estructura del proyecto

```text
Repositorio GitHub
├── restaurante_app/
│   ├── modelos/
│   │   ├── producto.py
│   │   └── cliente.py
│   ├── servicios/
│   │   └── restaurante.py
│   └── main.py
└── README.md
```

## Descripción de los archivos

### modelos/producto.py

Contiene la clase `Producto`, que representa un producto del restaurante mediante los atributos:

* nombre
* precio

También incluye el método `mostrar_info()`, encargado de mostrar la información del producto.

### modelos/cliente.py

Contiene la clase `Cliente`, que representa a un cliente del restaurante.

Atributo:

* nombre

Método:

* `mostrar_info()`

### servicios/restaurante.py

Contiene la clase `Restaurante`, responsable de administrar la información del restaurante.

Sus funciones principales son:

* Agregar productos.
* Registrar clientes.
* Mostrar el menú de productos.
* Mostrar la lista de clientes.

### main.py

Es el archivo principal del programa. En él se crean los objetos de las clases `Producto`, `Cliente` y `Restaurante`, se registran los datos y se muestra la información en pantalla.

## Funcionamiento

Al ejecutar el programa se realiza el siguiente proceso:

1. Se crea un restaurante.
2. Se registran varios productos.
3. Se registran clientes.
4. Se muestran en consola los productos disponibles y los clientes registrados.

## Conceptos de Programación Orientada a Objetos aplicados

* Clases y objetos.
* Encapsulación básica de los datos mediante atributos.
* Organización modular del proyecto.
* Separación de responsabilidades.
* Importación de módulos entre archivos.

## Ejecución

Desde la carpeta `restaurante_app`, ejecutar:

```bash
python main.py
```

## Resultado esperado

El programa mostrará en pantalla el nombre del restaurante, el menú de productos registrados y la lista de clientes.

## Autora

**Sherlyn Angélica Vargas Tapuy**
