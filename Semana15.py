# Programa: Gestión de Inventario de una Tienda
#Autor: Marco Ambo
#Descripción: Permite administrar productos de una tienda usando
#             diccionarios y listas.
# ============================================
# COLECCIÓN PRINCIPAL: Diccionario de productos
# ============================================
# Estructura: {codigo: {"nombre": str, "precio": float, "stock": int}}
inventario = {
    "P001": {"nombre": "Arroz 1kg",     "precio": 1.20, "stock": 20},
    "P002": {"nombre": "Leche 1L",      "precio": 1.00, "stock": 15},
    "P003": {"nombre": "Pan tajado",    "precio": 1.80, "stock": 20},
}

# COLECCIÓN SECUNDARIA: Lista de historial de movimientos
historial = []


# FUNCIONES
# ============================================

def agregar_producto(codigo, nombre, precio, stock):
    """Inserta un nuevo producto al inventario."""
    if codigo in inventario:
        print(f" El código {codigo} ya existe.")
        return
    inventario[codigo] = {"nombre": nombre, "precio": precio, "stock": stock}
    historial.append(f"Agregado: {nombre} (código {codigo}, stock {stock})")
    print(f" Producto '{nombre}' agregado correctamente.")


def mostrar_inventario():
    """Recorre y muestra todos los productos almacenados."""
    if not inventario:
        print(" El inventario está vacío.")
        return
    print("\n" + "=" * 60)
    print(f"{'CÓDIGO':<8}{'PRODUCTO':<20}{'PRECIO':<12}{'STOCK':<8}")
    print("=" * 60)
    for codigo, datos in inventario.items():
        print(f"{codigo:<8}{datos['nombre']:<20}"
              f"${datos['precio']:<11.2f}{datos['stock']:<8}")
    print("=" * 60)
    print(f"Total de productos registrados: {len(inventario)}")


def buscar_producto(codigo):
    """Busca un producto por su código."""
    if codigo in inventario:
        d = inventario[codigo]
        print(f"\nProducto encontrado:")
        print(f"   Código : {codigo}")
        print(f"   Nombre : {d['nombre']}")
        print(f"   Precio : ${d['precio']:.2f}")
        print(f"   Stock  : {d['stock']} unidades")
    else:
        print(f"No se encontró ningún producto con el código {codigo}.")


def eliminar_producto(codigo):
    """Elimina un producto del inventario."""
    if codigo in inventario:
        eliminado = inventario.pop(codigo)
        historial.append(f" Eliminado: {eliminado['nombre']} (código {codigo})")
        print(f" Producto '{eliminado['nombre']}' eliminado.")
    else:
        print(f" No existe el código {codigo}.")


def vender_producto(codigo, cantidad):
    """Descuenta unidades del stock al vender."""
    if codigo not in inventario:
        print(f"Código {codigo} no registrado.")
        return
    producto = inventario[codigo]
    if producto["stock"] < cantidad:
        print(f" Stock insuficiente. Solo hay {producto['stock']} unidades.")
        return
    producto["stock"] -= cantidad
    historial.append(
        f"Venta: {cantidad} x {producto['nombre']} "
        f"(total ${cantidad * producto['precio']:.2f})"
    )
    print(f" Venta registrada. Nuevo stock de '{producto['nombre']}': "
          f"{producto['stock']}")


def mostrar_historial():
    """Muestra la lista de movimientos realizados."""
    print("\n HISTORIAL DE MOVIMIENTOS")
    print("-" * 50)
    if not historial:
        print("(Sin movimientos aún)")
    else:
        for i, mov in enumerate(historial, 1):
            print(f"{i}. {mov}")

# MENÚ PRINCIPAL
# ============================================

def menu():
    while True:
        print("\n🛒 SISTEMA DE INVENTARIO")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Vender producto")
        print("6. Ver historial")
        print("7. Salir")

        opcion = input("Elige una opción (1-7): ").strip()

        if opcion == "1":
            codigo = input("Código: ").strip().upper()
            nombre = input("Nombre: ").strip()
            try:
                precio = float(input("Precio: "))
                stock  = int(input("Stock inicial: "))
                agregar_producto(codigo, nombre, precio, stock)
            except ValueError:
                print(" Precio o stock inválidos.")

        elif opcion == "2":
            mostrar_inventario()

        elif opcion == "3":
            codigo = input("Código a buscar: ").strip().upper()
            buscar_producto(codigo)

        elif opcion == "4":
            codigo = input("Código a eliminar: ").strip().upper()
            eliminar_producto(codigo)

        elif opcion == "5":
            codigo = input("Código del producto: ").strip().upper()
            try:
                cantidad = int(input("Cantidad a vender: "))
                vender_producto(codigo, cantidad)
            except ValueError:
                print(" Cantidad inválida.")

        elif opcion == "6":
            mostrar_historial()

        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print(" Opción no válida.")


if __name__ == "__main__":
    menu()