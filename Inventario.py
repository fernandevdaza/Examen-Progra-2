class Inventario:
    def __init__(self, id_producto, nombre_producto, cantidad, precio):
        self._id_producto = id_producto
        self._nombre_producto = nombre_producto
        self._cantidad = cantidad
        self._precio = precio
        self._lista_inventarios = []
    
    def set_cantidad(self, cantidad):
        self._cantidad = cantidad
