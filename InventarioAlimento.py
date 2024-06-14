import pandas as pd
import os
from Inventario import Inventario
class InventarioAlimento(Inventario):
    def __init__(self, id_producto, nombre_producto, cantidad, precio, codigo_senasag):
        Inventario.__init__(self, id_producto, nombre_producto, cantidad, precio)
        self.__codigo_senasag = codigo_senasag
        self.__archivo = "inventario_alimento.csv"

    def get_codigo_senasag(self):
        return self.__codigo_senasag
    
    def obtener_info_producto(self):
        return f"""
        ID: {self._id_producto}
        Nombre: {self._nombre_producto}
        Cantidad: {self._cantidad}
        Precio: {self._precio}
        Código Senasag: {self.get_codigo_senasag()}
        """

    @staticmethod
    def obtener_inventario(path):
        df = pd.read_csv(path)
        lista_inventario_electronico = []
        for _, row in df.iterrows():
            lista_inventario_electronico.append(InventarioAlimento(row['IDProducto'], row['NombreProducto'], row['Cantidad'], row['Precio'], row['CodigoSenasag']))
        return lista_inventario_electronico

    def generar_dict_inventario(self):
        return {
                "IDProducto": self._id_producto,
                "NombreProducto": self._nombre_producto,
                "Cantidad": self._cantidad,
                "Precio": self._precio,
                "CodigoSenasag": self.get_codigo_senasag()
            }
    
    def agregar_producto(self, id_producto, nombre_producto, cantidad, precio, codigo_senasag):
        self._id_producto = id_producto
        self._nombre_producto = nombre_producto
        self._cantidad = cantidad
        self._precio = precio
        self.__codigo_senasag = codigo_senasag
        try:
            data = self.generar_dict_inventario()
            df = pd.DataFrame([data])
            if not os.path.exists(self.__archivo):
                df.to_csv(self.__archivo, index=False)
            else:
                df.to_csv(self.__archivo, mode="a", index=False, header=False)
            print("Producto agregado exitosamente")
            return True
        except Exception as e:
            print(f"Hubo un error al agregar el producto: {e}")
            return False
    
    @staticmethod
    def guardar_a_csv(lista_inventario, path):
        if lista_inventario:
            lista_df = [producto.generar_dict_inventario() for producto in lista_inventario]
            df = pd.DataFrame(lista_df)
        else:
            df = pd.DataFrame(columns=["IDProducto", "NombreProducto", "Cantidad", "Precio", "CodigoSenasag"])
        df.to_csv(path, index=False)

    @staticmethod
    def eliminar_producto(lista_inventario, id, path):
        found = False
        longitud = len(lista_inventario)
        lista_inventario = [producto for producto in lista_inventario if producto._id_producto != id]
        if len(lista_inventario) < longitud:
            found = True
        InventarioAlimento.guardar_a_csv(lista_inventario, path)
        return found
    @staticmethod
    def buscar_producto(lista_inventario, id):
        producto_encontrado = [producto for producto in lista_inventario if producto._id_producto == id]
        if len(producto_encontrado) > 0:
            return producto_encontrado[0]
        return None
    
    def actualizar_cantidad(lista_inventario, id, cantidad, path):
        found = False
        longitud = len(lista_inventario)
        nuevo_inventario = []
        for producto in lista_inventario:
            if producto._id_producto == id: 
                producto.set_cantidad(cantidad)
                found = True
            nuevo_inventario.append(producto)
        if found: 
            InventarioAlimento.guardar_a_csv(nuevo_inventario, path)
            print("Cantidad Actualizada exitosamente")
            return found
        else:
            print("No se pudo encontrar el producto")
            return found
        
    