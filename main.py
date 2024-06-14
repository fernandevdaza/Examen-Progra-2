from InventarioAlimento import InventarioAlimento
from InventarioElectronico import InventarioElectronico

PATH_ALIMENTO_CSV = "inventario_alimento.csv"
PATH_ELECTRONICO_CSV = "inventario_eletronico.csv"

def Menu():
    while True:
        try:
            print("\n")
            print("Inventarios\n")
            print("¿Qué desea hacer?")
            print("1. Agregar producto")
            print("2. Borrar producto")
            print("3. Actualizar cantidad de producto")
            print("4. Ver producto")
            print("5. Ver inventario")
            print("6. Salir")
            print("\n")
            
            option = int(input("Ingresa una opción: "))
            if option == 1:
                agregar_producto()
            elif option == 2:
                borrar_producto()
            elif option == 3:
                actualizar_cantidad()
            elif option == 4:
                ver_producto()
            elif option == 5:
                ver_inventario()
            elif option == 6:
                exit()
            else:
                print("Ingrese una opción válida")
        except ValueError:
            print("Error, por favor escriba un número")

def agregar_producto():
    while True:
        try:
            print("\n")
            print("¿Qué tipo de producto quieres ingresar?")
            print("1. Alimento")
            print("2. Electrónico")
            print("3. Regresar")
            print("\n")
            option = int(input("Seleccione una opción: "))
            if option != 1 and option != 2 and option != 3:
                print("Selecciona una opción válida")
                continue
            if option == 3:
                return
            id = int(input("Ingresa el id del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingresa la cantidad del producto: "))
            precio = int(input("Ingresa el precio del producto: "))
            if option == 1:
                codigo_senasag = int(input("Ingresa el código de senasag: "))
                nuevo_alimento = InventarioAlimento(id, nombre, cantidad, precio, codigo_senasag)
                nuevo_alimento.agregar_producto(id, nombre, cantidad, precio, codigo_senasag)

            elif option == 2:
                nro_serie = int(input("Ingrese el nro de serie: "))
                nuevo_electronico = InventarioElectronico(id, nombre, cantidad, precio, nro_serie)
                nuevo_electronico.agregar_producto(id, nombre, cantidad, precio, nro_serie)
            else:
                return
            return
        except ValueError:
            print("Error, por favor escriba un número")
            continue    

def borrar_producto():
    while True:
        try:
            isRemoved = False
            print("\n")
            print("¿Qué tipo de producto quieres borrar?")
            print("1. Alimento")
            print("2. Electrónico")
            print("3. Regresar")
            print("\n")
            
            option = int(input("Seleccione una opción: "))
            if option != 1 and option != 2 and option != 3:
                print("Selecciona una opción válida: ")
                continue
            print("\n")
            if option == 3:
                return
            id_producto = int(input("Ingresa el id del producto: "))
            if option == 1:
                lista_inventario_alimento = InventarioAlimento.obtener_inventario(PATH_ALIMENTO_CSV)
                isRemoved = InventarioAlimento.eliminar_producto(lista_inventario_alimento, id_producto, PATH_ALIMENTO_CSV)
            else:
                lista_inventario_electronico = InventarioElectronico.obtener_inventario(PATH_ELECTRONICO_CSV)
                isRemoved = InventarioElectronico.eliminar_producto(lista_inventario_electronico, id_producto, PATH_ELECTRONICO_CSV)
            if isRemoved:
                print("Producto eliminado exitosamente")
            else:
                print("Hubo un error al eliminar al producto")
            return
        except ValueError:
            print("Error, por favor escriba un número")
        except Exception as e:
            print(f"Hubo un error: {e}")

def actualizar_cantidad():
    while True:
        try:
            print("\n")
            print("¿De qué tipo de producto quieres editar la cantidad?")
            print("1. Alimento")
            print("2. Electrónico")
            print("3. Regresar")
            print("\n")
            option = int(input("Seleccione una opción: "))
            if option != 1 and option != 2 and option != 3:
                print("Selecciona una opción válida: ")
                continue
            print("\n")
            if option == 3:
                return
            id_producto = int(input("Ingresa el id del producto: "))
            cantidad = int(input("Ingresa la nueva cantidad: "))
            if option == 1:
                lista_inventario_alimento = InventarioAlimento.obtener_inventario(PATH_ALIMENTO_CSV)
                InventarioAlimento.actualizar_cantidad(lista_inventario_alimento, id_producto, cantidad, PATH_ALIMENTO_CSV)
            elif option == 2:
                lista_inventario_electronico = InventarioElectronico.obtener_inventario(PATH_ELECTRONICO_CSV)
                InventarioElectronico.actualizar_cantidad(lista_inventario_electronico, id_producto, cantidad, PATH_ELECTRONICO_CSV)
            else:
                return
            return
        except ValueError:
            print("Error, por favor escriba un número")
        except Exception as e:
            print(f"Hubo un error: {e}")
    return

def ver_producto():   
    while True:
        try:
            print("\n")
            print("¿Qué tipo de producto quieres ver?")
            print("1. Alimento")
            print("2. Electrónico")
            print("3. Regresar")
            print("\n")
            option = int(input("Seleccione una opción: "))
            if option != 1 and option != 2 and option != 3:
                print("Selecciona una opción válida: ")
                continue
            print("\n")
            if option == 3:
                return
            id_producto = int(input("Ingresa el id del producto: "))
            if option == 1:
                lista_inventario_alimento = InventarioAlimento.obtener_inventario(PATH_ALIMENTO_CSV)
                alimento_encontrado = InventarioAlimento.buscar_producto(lista_inventario_alimento, id_producto)
                if not alimento_encontrado:
                    print("No se encontró el producto")
                    return
                print(alimento_encontrado.obtener_info_producto())
            elif option == 2:
                lista_inventario_electronico = InventarioElectronico.obtener_inventario(PATH_ELECTRONICO_CSV)
                electronico_encontrado = InventarioElectronico.buscar_producto(lista_inventario_electronico, id_producto)
                if not electronico_encontrado:
                    print("No se encontró el producto")
                    return
                print(electronico_encontrado.obtener_info_producto())
            else:
                return
            return
        except ValueError:
            print("Error, por favor escriba un número")
        except Exception as e:
            print(f"Hubo un error: {e}")
    

def ver_inventario():
    while True:
        try:
            print("\n")
            print("¿Qué tipo de inventario quieres ver?")
            print("1. Alimentos")
            print("2. Electrónicos")
            print("3. Regresar")
            print("\n")
            option = int(input("Seleccione una opción: "))
            if option != 1 and option != 2 and option != 3:
                print("Selecciona una opción válida: ")
                continue
            print("\n")
            if option == 3:
                return
            if option == 1:
                lista_inventario_alimento = InventarioAlimento.obtener_inventario(PATH_ALIMENTO_CSV)
                for alimento in lista_inventario_alimento:
                    print(alimento.obtener_info_producto())
            elif option == 2:
                lista_inventario_electronico = InventarioElectronico.obtener_inventario(PATH_ELECTRONICO_CSV)
                for electronico in lista_inventario_electronico:
                    print(electronico.obtener_info_producto())
            else:
                return
            return
        except ValueError:
            print("Error, por favor escriba un número")
        except Exception as e:
            print(f"Hubo un error: {e}")

   
Menu()