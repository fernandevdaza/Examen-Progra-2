from Inventario import Inventario
import pandas as pd
import os
class InventarioElectronico(Inventario):
    def __init__(self, id_producto, nombre_producto, cantidad, precio, nro_serie):
        Inventario.__init__(self, id_producto, nombre_producto, cantidad, precio)
        self.__nro_serie = nro_serie
        self.__archivo = "inventario_eletronico.csv"

    def get_nro_serie(self):
        return self.__nro_serie
    
    def obtener_info_producto(self):
        return f"""
        ID: {self._id_producto}
        Nombre: {self._nombre_producto}
        Cantidad: {self._cantidad}
        Precio: {self._precio}
        Número de Serie: {self.get_nro_serie()}
        """

    @staticmethod
    def obtener_inventario(path):
        df = pd.read_csv(path)
        lista_inventario_electronico = []
        for _, row in df.iterrows():
            lista_inventario_electronico.append(InventarioElectronico(row['IDProducto'], row['NombreProducto'], row['Cantidad'], row['Precio'], row['NroSerie']))
        return lista_inventario_electronico

    def generar_dict_inventario(self):
        return {
                "IDProducto": self._id_producto,
                "NombreProducto": self._nombre_producto,
                "Cantidad": self._cantidad,
                "Precio": self._precio,
                "NroSerie": self.get_nro_serie()
            }

    def agregar_producto(self, id_producto, nombre_producto, cantidad, precio, nro_serie):
        self._id_producto = id_producto
        self._nombre_producto = nombre_producto
        self._cantidad = cantidad
        self._precio = precio
        self.__nro_serie = nro_serie
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
            df = pd.DataFrame(columns=["IDProducto", "NombreProducto", "Cantidad", "Precio", "NroSerie"])
        df.to_csv(path, index=False)

    @staticmethod
    def eliminar_producto(lista_inventario, id, path):
        found = False
        longitud = len(lista_inventario)
        lista_inventario = [producto for producto in lista_inventario if producto._id_producto != id]
        if len(lista_inventario) < longitud:
            found = True
        InventarioElectronico.guardar_a_csv(lista_inventario, path)
        return found
    @staticmethod
    def buscar_producto(lista_inventario, id):
        producto_encontrado = [producto for producto in lista_inventario if producto._id_producto == id]
        if producto_encontrado:
            return producto_encontrado[0]
        return None
    @staticmethod
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
            InventarioElectronico.guardar_a_csv(nuevo_inventario, path)
            print("Cantidad Actualizada exitosamente")
            return found
        else:
            print("No se pudo encontrar el producto")
            return found
            
        
        

        