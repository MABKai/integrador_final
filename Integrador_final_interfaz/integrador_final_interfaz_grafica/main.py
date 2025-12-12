# main productos
# Marcela, Alejandra Brahim, DNI 20010395 mar.ale.bra@gmail.com
"""
FALTA
EMPROLIJAR todo,
MENUES SECUNDARIOS
chequear CERRAR_CONEXION() 
cheaquear Ortografia
sumar docstring
terminar README con muestras de tablas y codigo
AGREGAR:
TKINTER
colorama 

***** Unir con clientes Servicios y Ventas

"""
from productos_db import *
from funciones_helpers import imprimir_tituloSimple
from funciones_helpers import imprimir_titulo
from productos import *
from productos_db import conectar_db
from ventas_db import *
from ventas import *
from interfaz import *
from interfaz_aux import *
from colorama import Fore, Style, init
init(autoreset=True)

# ======================= ACTIVIDADES DEL MENU PRINCIPAL==========
# EN TUPLA PARA QUE NO SE PUEDAN MODIFICAR ACCIDENTALMENTE
actividades =(   "Inventario",
                 "Alta de Producto",
                 "Alta productos datos default",
                 "Menú Listar/ Read", 
                 "Menú Actualizar/Upgrade", 
                 "Menú Eliminar/Delete",
                 "Menú Buscar/Search", 
                 "Tabla Ventas",
                 "Venta de producto",
                 "Gráficas Stock y Capital Vendido",
                 "Gráfica Stock vendido",
                 "grafica Monto Vendido",
                 "Inventario: Alertas",
                 "Inventario: Capital", 
                 "Gráficas", "Reporte Bajo Stock", 
                 "Otros Reportes",
                 "Interfaz Gráfica: Inventario",
                 "Salir" )

# ============== ACTIVIDADES DE LOS SUB MENU================
# Actividades del Sub Menu Read/Listar
menu_listados = ('Stock', 'Precio', 'Categoría', 'ID', 'Descripción', 'Productos Disponibles', 'Alertas de Stock', 'Alertas de Stock', 'Alerta de Precio', 'Alerta de Categoría', 'Alerta Descripción', "Volver Menú Principal")

# ============ ACtividades del sub Menu actualizar/upgrade
menu_actualizaciones = (
    "Actualizar Producto",
    "Actualizar Stock",
    "Actualizar Precio",
    "Actualizar Categoría",
    "Actualizar Descripción", "Volver al Menú Principal"
)

#============ Actividades del Sub Menu delete/eliminar
menu_eliminaciones = ("Eliminar Producto P/Nombre", "Eliminar Producto_ P/ID", "Eliminar Tabla Productos", "Eliminar Inventario", "Eliminar Tabla Ventas", "Volver al Menú Principal")

 # ============ ACtividades del Sub Menu Biuscar/Search
menu_busquedas = (
    "Producto: Buscar por ID",
    "Producto: Buscar por nombre",
    "Buscar ID de Producto",
    "Precio: Buscar por prod/ID",
    "Stock: Buscar por prod/ID",
    "Categoría: Buscar por prod/ID",
    "Descripción: buscar por prod/ID",
    "Precio: Buscar por nombre/prod",
    "Stock: Buscar por nombre/Prod",
    "Categoría: Buscar por nombre/Prod",
    "Descripción: Buscar por nombre/Prod",
    "Volver al Menú Principal"
)

# ============= Actib¿vidades del Sub Menu OTROS reportes
menu_reportes = (
                 "Productos Eliminados",
                 "Productos Agregados",
                 "Productos Bajo_Stock")
# ========== MENU PRINCIPAL: MUESTRA Y ELECCION DE LAS ACTIVIDADES
# Función Elección de operación a realizarse del menú de actividades
def menu():
    # Muestro el Menu principal
    imprimir_tituloSimple(" 🍀 MENÚ 🍀 🫣 ")
    for i, actividad in enumerate (actividades): # Muestro el listado de actividades enumeradas ya que los numeros son respuesta y utilzo mat
           if (i+1 )% 2 == 1: # Al ser el numero impar. alinea a la izquiera
                 print(f"{i+1:2}🔸{actividad:<40}", end="")
           else: # Al ser el numero par alinea a la derecha
                 print(f"{i+1:2}🔸{actividad:43}")
                 
# Defino la funcion de elegir la opcion del menu de actividades principal
def seleccionar_opcion(opcion):
  """
   Esta funcion define los métodos para elñegir una opcion del menu de opciones que tiene este progrma sección 'clientes', utilizando un bucle whilw true que invita a seguir optando por tareas hasta que se quiera salir, se hace con un Enter mostrando los reportes del archivo 'clientes' al finalizar
  """
  while True:
    match opcion:
        # ============== Listado de producctos
        case '1':
           listar_inventario(conexion)
           break
        # =============== Create Producto
        case '2':
            agregar_producto(conexion)
            break
        # ============== Create RAPIDO producto con datros por default
        case '3':
            agregar_producto_default(conexion)
            break
        # ==============
        case '4':
            seleccionar_opcion_listar(conexion)
            break
        # ==============
        case '5':
            seleccionar_update_opcion(conexion)
            break
        # ==============
        case '6':
            seleccionar_eliminar_opcion(conexion)
            break
        # =============
        case '7':
            seleccionar_buscar_opcion(conexion)
            break
        # ============= Ventas
        case '8':
            listar_ventas(conexion)
            break
        # ============= Ventas: Graficas en la misma figura
        case '9':
            venta_producto(conexion)
            break
        # ============= Ventas: Graficas en la misma figura
        case '10':
            graficas_stock_capitalVendido_producto(conexion)
            break
        # ============= Ventas: Graficas en la misma figura
        case '11':
            grafica_stockVendido_producto(conexion)
            break
        #=====================================
        case '12':
            grafica_capitalVendido_producto(conexion)
            break
        # ======== Se muestra el inventario con las alertas
        case '13':
           listar_inventario_alertas(conexion)
           break
        # =========== Tabla de Productos con sus capitales y capital total
        case '14':
          capital_inventario_productos(conexion)
          break
        # ========== Graficas de Stock y Capital por producto DISPONIBLR en Inventario
        case '15':
          ver_graficas(conexion)
          break      
        # ========== reporte bajo stock =====
        case '16':
           reporte_bajo_stock(conexion)
           break
        # ========= otros reportes =====
        case '17':
            listar_otros_reportes(conexion)
            break
        # ========= interfaz grafica =====
        case '18':
            mostrar_inventario(conexion)
            break
        # ======== Opciónn de concluir el programa
        case '19' | '':
           break
        # ============== Opción inválida
        case _:
           print("❌ Por favor, ingrese una opción válida.")
           break

# ===================== MENU SECUNDARIOS =================     
# Funciones Menues secundarios
# SubMenu Listados: muestor el menu con formato, selecciono y valido opcion
def seleccionar_opcion_listar(opcion):
  while True:
    imprimir_tituloSimple(" 🍀 MENÚ Listar/Read 🍀 🫣 ")
    for i, m in enumerate (menu_listados): # Muestro el listado de actividades enumeradas ya que los numeros son respuesta y utilzo mat
           if (i+1 )% 2 == 1: # Al ser el numero impar. alinea a la izquiera
                 print(f"{i+1:2}🔸{m:<40}", end="")
           else: # Al ser el numero par alinea a la derecha
                 print(f"{i+1:2}🔸{m:43}")
    
    opcion = input("Elegí una opción de Listados: (O presiona Enter para salir): ").strip()
    # ======== Salir del Sub Menu
    if opcion == '12' or opcion == "":
        print("Regreso al Menú Principal. ")
        break
    else:
     if opcion.isdigit() and 1 <= int(opcion) <= len(menu_listados):
     # Utilizo match
      match opcion:
      
       # ============== Listar Stock con Id y producto
       case '1':
         listar_stock(conexion)
         break
       # ============== Listar precios con Id productos
       case '2':
            listar_precio(conexion)
            break
       # ============== listar categorias con Id productos
       case '3':
            listar_categoria(conexion)
            break
        # ========= listar  Producto e ID
       case '4':
            listar_codigo(conexion)
            break
       # ======== listar descripcion con Id y producto
       case'5':
            listar_descripcion(conexion)
            break
        # ======== muestro los productos disponibles nombre/ID
       case'6':
           listar_productos(conexion)
           break
       # ======== se muestran los alertas de ID de haberlos
       case '7':
           productos_codigos_alertas(conexion)
           break
       # ======== muestro lista de productos con su stock y alertas si las hay
       case'8':
           productos_stock_alertas(conexion)
           break
      # ======== muestro lista de productos con sus precios y alertas si las hay
       case'9':
           productos_precios_alertas(conexion)
           break
      # ======== muestro lista de categorias de productos con las alertas si las hay
       case'10':
           productos_categorias_alertas(conexion)
           break
       # ======== muestro la lista de descrpciones con las alertas
       case '11':
           productos_desc_alertas(conexion)
           break
         # ======== Opciónn de concluir el programa
       case '12' | '':
           break
        # ============== Opción inválida
       case _:
           print("❌ Por favor, ingrese una opción válida.")
           break
     else:
        print("❌ Por favor, ingrese una opción válida.")   

# SubMenu Update: muestro menu con formato, selecciona y valida opcion          
def seleccionar_update_opcion(opcion):

 while True:
  imprimir_tituloSimple(" 🍀 MENÚ Actualizar/Upgrade 🍀 🫣 ")
  for i, actualizacion in enumerate (menu_actualizaciones): # Muestro el listado de actividades enumeradas ya que los numeros son respuesta y utilzo mat
           if (i+1 )% 2 == 1: # Al ser el numero impar. alinea a la izquiera
                 print(f"{i+1:2}🔸{actualizacion:<40}", end="")
           else: # Al ser el numero par alinea a la derecha
                 print(f"{i+1:2}🔸{actualizacion:43}") 
  opcion = input("Elegí una opción de Actualización (O presiona Enter para salir: )").strip()
       
  if  opcion == '6' or opcion == "":
            print(" Regreso al Menú Principal. ")
            break
  else:
    if opcion.isdigit() and 1 <= int(opcion) <= len(menu_actualizaciones):
     match opcion:
       # ======= Actualizo producto
       case '1':
           actualizar_producto(conexion)
           break
       # ======== modifico stock de un producto
       case'2':
           actualizar_stock(conexion)
           break
       # ========  modificar precio de un producto
       case'3':
           actualizar_precio(conexion)
           break
       # ======== Modificar categoría de un producto
       case'4':
            actualizar_categoria(conexion)
            break 
       # ======== Modificar descripcion de un producto
       case '5':
           actualizar_descripcion(conexion)
           break
       # ========= Regreso al menu principal
       case '6' | '':
           break
        # ============== Opción inválida
       case _:
           print("❌ Por favor, ingrese una opción válida.")
           break
    else:
               print("❌ Por favor, ingrese una opción válida.")

# SubMenu Buscar. muestto menu de actividades, se selecciona opcion y se valida.              
def seleccionar_buscar_opcion(opcion):
 while True:
    imprimir_tituloSimple(" 🍀 MENÚ Buscar 🍀 🫣 ")
    for i, busqueda in enumerate (menu_busquedas): # Muestro el listado de actividades enumeradas ya que los numeros son respuesta y utilzo mat
           if (i+1 )% 2 == 1: # Al ser el numero impar. alinea a la izquiera
                 print(f"{i+1:2}🔸{busqueda:<40}", end="")
           else: # Al ser el numero par alinea a la derecha
                 print(f"{i+1:2}🔸{busqueda:43}") 
    opcion = input("Elegí una opción de Búsqueda (O presiona Enter para salir): ").strip()
    # ======== Salir del Sub Menu
    if opcion == '14' or opcion == "":
            print("Regreso al Menú Principal. ")
            break
    else:
     if opcion.isdigit() and 1 <= int(opcion) <= len(menu_busquedas):     
      match opcion:
       # ========  buscar producto por ID y lo mostramos con sus datos
       case'1':
           buscar_producto_id(conexion)
           break
       # ======== buscar producto por nombre y lo mostramos con sus datos
       case'2':   
            buscar_producto_nombre(conexion)
            break
       # ========  buscar el código/ID de un producto
       case'3':
           buscar_codigo_producto(conexion)
           break
       # ======== buscamos el precio de un producto por ID
       case'4':
            buscar_precio_producto_id(conexion)
            break
       # ========buscamos stock de un producto por ID
       case'5':
            buscar_stock_producto_id(conexion)
            break
       # ======== buscamos la categoria de un producto por ID
       case '6':
           buscar_cat_producto_id(conexion)
           break
       # ======== buscar la descripcion de un producto por ID
       case '7':
           buscar_desc_producto_id(conexion)
           break
       # ========== Buscar precio de un producto por nombre
       case '8':
          buscar_precio_producto_nombre(conexion)
          break
       # ========== Buscar el stock de un producto mpor nombre
       case '9':
          buscar_stock_producto_nombre(conexion)
          break
       # ========= Buscar la categoria d eun productom por nombre
       case '10':
          buscar_cat_producto_nombre(conexion)
          break
       # ======== Buscar la descripcion de un producto poir nombre
       case '11':
           buscar_desc_producto_nombre(conexion)
           break
       # ======== Opciónn de regreso al menu ´principal
       case '12' | '':
           break
      # ============== Opción inválida
       case _:
           print("❌ Por favor, ingrese una opción válida.")
           break
     else:
               print("❌ Por favor, ingrese una opción válida.")
               
# Submenu: Eliminaciones 

# Se define y muestra la actividad seleccionada del sub menu                    
def seleccionar_eliminar_opcion(opcion):
 while True:
     imprimir_tituloSimple(" 🍀 MENÚ Eliminar/Delete 🍀 🫣 ")
     for i, eliminacion in enumerate (menu_eliminaciones): # Muestro el listado de actividades enumeradas ya que los numeros son respuesta y utilzo mat
           if (i+1 )% 2 == 1: # Al ser el numero impar. alinea a la izquiera
                 print(f"{i+1:2}🔸{eliminacion:<40}", end="")
           else: # Al ser el numero par alinea a la derecha
                 print(f"{i+1:2}🔸{eliminacion:43}") 
     
     opcion = input("Elegí una opción de Eliminaciones (O presiona Enter para salir): ").strip()
     # ======== Salir del Sub Menu
     if opcion == '6' or opcion == "":
            print("Regreso al Menú Principal. ")
            break
     else:
      if opcion.isdigit() and 1 <= int(opcion) <= len(menu_eliminaciones):
            
            
       match opcion:
         # ==========
         case '1':
             eliminar_producto_nombre(conexion)
             break
         # ==========
         case '2':
             eliminar_producto_codigo(conexion)
             break
         # ==========
         case '3':
            eliminar_tabla_productos(conexion)
            break
          # ==========
         case '4':
            #eliminar_inventario(conexion)
            break
         # ==========
         case '5':
            eliminar_tabla_ventas(conexion)
            break
        
         # ======= Opción de regresar al menu principal
         case '6' | '':
             break
         # ============== Opción inválida
         case _:
             print("❌ Por favor, ingrese una opción válida.")
             break
      else:
               print("❌ Por favor, ingrese una opción válida.") 

# ==== Menu Principal
# Defino la funcion del menu principal(main)

def main(conexion):

    crear_tablas(conexion)
    carga_inicial(conexion)
    carga_inicial_ventas(conexion)
    while True:
        
        menu()
        opcion = input("Elegí una opción: (O presiona Enter para salir): ").strip()
        # ======== Salir del programas
        if opcion == '19' or opcion == "":
           
            imprimir_tituloSimple(" 📝 Reporte Final ")
            listar_otros_reportes(conexion)
            #listar_ventas(conexion)
            salir(conexion)
            print(" 👋 Gracias! Fin del programa👋 ")
            break
        else:
            if opcion.isdigit() and 1 <= int(opcion) <= len(actividades):
               seleccionar_opcion(opcion)
            else:
               print("❌ Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    conexion = conectar_db()
    if conexion:
        try:
            main(conexion)     
            
        finally:
            cerrar_conexion(conexion)

        