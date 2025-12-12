# Marcela, Alejandra Brahim, DNI 20010395 mar.ale.bra@gmail.com
import datetime
from colorama import Fore, Style
from productos_db import *
from productos_validaciones import *
from ventas_db import *
#from ventas import *

# Diccionario para mostrar los productos agregados
#No lo necesitamos en una tabla sino como archivo temporal
productos_agregados = {}


# ====== CREATE/altas
# creat producto con cada item
def agregar_producto(conexion):
    print("\n🔹🔹🔹ALTA PRODUCTO 🔹🔹🔹")
    nombre = validar_producto(input("Nombre: "))
    precio = validar_precio(input("Precio: "))
    stock = validar_stock(input("Stock: "))
    categoria = validar_categoria(input("Categoría: "))
    descripcion = validar_descripcion(input("Descripción: "))
    
    insertar_producto_db(conexion, nombre, precio, stock, categoria, descripcion)
    # Guardar en diccionario para reportar al final 
    productos_agregados[nombre] = {
        "precio": precio,
        "stock": stock,
        "categoria": categoria,
        "descripcion": descripcion
    }
    print(f"Producto agregado: {nombre}")
    sleep(1)
    listar_inventario(conexion)
    sleep(2)

# create producto los datos van por defaulyt
def agregar_producto_default(conexion):
    print("🔹🔹🔹ALTA PRODUCTO (Valores por default)🔹🔹🔹")
    nombre = validar_producto(input("Nombre: ").strip().lower().title())
    precio = 0.00
    stock = 0
    categoria = ""
    descripcion = ""
    insertar_producto_db(conexion, nombre, precio, stock, categoria, descripcion)
     # Guardar en diccionario para reportar al final 
    productos_agregados[nombre] = {
        "precio": precio,
        "stock": stock,
        "categoria": categoria,
        "descripcion": descripcion
    }
    print(f"Producto agregado: {nombre}")
    sleep(1)
    listar_inventario(conexion)
    sleep(2)
    return
      
# ===== READ/ listar

# LISTAR INVENTARIO CON ID NOMBRE PRECIO STOCK CATEGORIA Y DESCRIPCION DEL PRODUCTO
def listar_inventario(conexion):
 
    productos = listar_inventario_bd(conexion)
    imprimir_tituloSimple(" 💠INVENTARIO💠")
    if productos:
      # Aplicar el formateo a la descripción antes de crear la tabla
      productos_formateados = []
      for producto in productos:
        id_prod, nombre, precio, stock, categoria, descripcion = producto
        descripcion_formateada = formatear_descripcion(descripcion)
        productos_formateados.append([id_prod, nombre, precio, stock, categoria, descripcion_formateada])

      print(tabulate(productos_formateados, headers=["ID", "Nombre", "Precio", "Stock", "Categoría", "Descripcion"],maxcolwidths=[4, 25, 10, 4, 12, 8] ,tablefmt="grid"))
      sleep(3)
    else:
        print(" ❌ No hay productos para mostrar.")
    return

# LISTAR INVENTARIO CON CON ALERTAS DE DATOS DE PRODUCTOS
def listar_inventario_alertas(conexion):
               
               """

               """ 
               productos = listar_inventario_alertas_bd(conexion)            
               imprimir_tituloSimple(" 💠INVENTARIO  CON ALERTAS 💠")
               tabla_con_alerta = []
               alerta = []
               productos_formateados = []
               for prod in productos:
                     id_prod, nombre, precio, stock, categoria, descripcion = prod
                     descripcion_formateada = formatear_descripcion(descripcion)
                     productos_formateados.append([id_prod, nombre, precio, stock, categoria, descripcion_formateada])
                     # Inicializar alerta
                     alerta = ""
                     # alerta es una lista ya que los alertas pueden ser 4 por producto
                     alerta_lista = []
                   
                     # Verificar los items estan completos
                 
                     if not precio or precio == '' or precio <= 0 :
                       alerta = "❌ Precio Inválido"
                       alerta_lista.append(alerta)
                     if not stock or stock == '':
                       alerta = "❌ Stock Inválido"
                       alerta_lista.append(alerta)
                     if stock <= 10:
                        alerta = "⚠️ Bajo Stock"
                        alerta_lista.append(alerta)
                     if  not categoria or categoria == '':
                        alerta = "❌ Categoría Inválida"
                        alerta_lista.append(alerta)
                     if  not descripcion_formateada or descripcion_formateada == '':
                        alerta = "❌ Descripción Inválida"
                        alerta_lista.append(alerta)
                     if alerta == "":
                        alerta = "✅"
                        alerta_lista.append(alerta)
                
                     tabla_con_alerta.append([id_prod, nombre, stock, precio, categoria, descripcion_formateada, alerta_lista])
               print(tabulate(tabla_con_alerta, headers=["ID", "Nombre", "Precio", "Stock", "Categoría", "Descripcion", "Alerta"],maxcolwidths=[4, 25, 10, 4, 10, 7, 10 ], tablefmt="grid"))
               sleep(3)
               return

# LISTAR INVENTARIO CON CAPITAL TOTAL POR CADA PRODUCTO Y CAPITAL DEL INVENTARIO
def capital_inventario_productos(conexion):
  
      productos = capital_inventario_productos_db(conexion)
      imprimir_tituloSimple(" 💠INVENTARIO CON CAPITAL💠")
      total_inventario = 0
      tabla_con_capital = []
      for prod in productos:
        id_prod, nombre, precio, stock = prod
        capital_producto = stock * precio
        total_inventario += capital_producto
        tabla_con_capital.append([id_prod, nombre, precio, stock,  f"{capital_producto:.2f}"])
      print(tabulate(tabla_con_capital, headers=["Id/Código", "Nombre", "Precio", "Stock", "Capital"], tablefmt="grid"))
      print(f"Capital total del inventario: {total_inventario:.2f}") 
      sleep(3)   

# LISTAR ID NOMBRE DE PRODCUTO Y SU STOCK
def listar_stock(conexion):
    """
          Con esta funcion muestro los p´roductos del inventario en relacion con el stocj de cada uno
    """
    imprimir_tituloSimple(" 🫣 Id/CÓDIGOS (ID) 🤓")
    
    resultados = listar_stock_bd(conexion)
    datos_para_tabular = [["Id/Código", "Nombre", "Stock"]] + resultados
    # Imprimir la tabla
    print(tabulate(datos_para_tabular, headers="firstrow", tablefmt="grid"))
    sleep(3)

# LISTAR ID NOMBRE DE PRODCUTO Y SU PRECIO         
def listar_precio(conexion):
        """
        Con esta funcio muestro los productos y su precio en formato de lista
        """
        imprimir_tituloSimple(" 🫣 PRECIOS 🤓")
   
        
        resultados = listar_precio_bd(conexion)
        datos_para_tabular = [["Id/Código", "Nombre", "Precio"]] + resultados
        # Imprimir la tabla
        print(tabulate(datos_para_tabular, headers="firstrow", tablefmt="grid"))
        sleep(3)  
        return

# LISTAR ID NOMBRE DE PRODCUTO Y SU CATEGORIA
def listar_categoria(conexion):
         """
         Con esta funcio muestro los productos y su categoria en formato de lista
         """
         imprimir_tituloSimple(" 🫣 CATEGORÍAS 🤓")  
               
         resultados = listar_categoria_bd(conexion)
         datos_para_tabular = [["Id/Código", "Nombre", "Categoría"]] + resultados
         # Imprimir la tabla
         print(tabulate(datos_para_tabular, headers="firstrow", tablefmt="grid"))
         sleep(3)
         return
     
# LISTAR ID NOMBRE DE PRODCUTO Y SU DESCRIPCION
# ENVUELVO TEXTO DE DESCRIPCION PARA QUE NO ROMPA EL FORMATO TABLA
def preparar_descripcion_con_envoltura(productos, ancho_descripcion=30):
    """
    Funcion para envolver todo el texto de la descripcion de TOPDOS los productos
    a los efectos
    de mostrarla en la misma columna que no se expanda horozontalmente
    al mostrar la tabla de codigo, producto y la descripcion de cada uno.
    """  
    productos_formateados = []
    for p in productos:
             # Envuelve la descripción en la columna "Descripción"
             descripcion_formateada = envolver_texto(p[2], ancho_descripcion)
             productos_formateados.append((p[0], p[1], descripcion_formateada))
    # Hemos isado po p1 p2, ya que extraemos codifo producto yd escripcion y son los indices
    # obtenidos en la lista de productos formateados donde esa extraccion se guardó
    return productos_formateados

def listar_descripcion(conexion):
         """
         Con esta funcion muestro los productos y su descripcion en formato de lista
         mostramos la tabla ordenada codigo, nombre y descripcion de producto
         llamando a las funciones ayudantes para lograrlo
         """
         
         imprimir_tituloSimple(" 🫣 Descripción 🤓")
    
         productos = listar_descripcion_bd(conexion) 
         productos_formateados = preparar_descripcion_con_envoltura(productos)
         datos_para_tabular = [["Id/Código", "Nombre", "Descripción"]] + productos_formateados
         # Imprimir la tabla
         print(tabulate(datos_para_tabular, headers="firstrow", tablefmt="grid"))
         sleep(3)

# LISTAR ID NOMBRE DE PRODCUTO         
def listar_codigo(conexion):
        """
        Con esta funcio muestro los productos y su codigo en formato de lista
        """
        imprimir_tituloSimple(" 🫣 Id/CÓDIGOS 🤓")
        
        resultados = listar_codigo_bd(conexion)
        datos_para_tabular = [["Id/Código","Nombre"]] + resultados
        # Imprimir la tabla
        print(tabulate(datos_para_tabular, headers="firstrow", tablefmt="grid"))
        sleep(3)
        return

# LISTAR ID NOMBRE DE PRODCUTO DISPONIBLE, ES IGUAL AL ANTERIOR LO BORRARE
def listar_productos(conexion):
            imprimir_tituloSimple(" 👓 Productos Disponibles ")          
            
            resultados = listar_productos_bd(conexion)
            datos_para_tabular = [["Id/Código", "Nombre"]] + resultados
            # Imprimir la tabla
            print(tabulate(datos_para_tabular, headers="firstrow", tablefmt="grid"))
            sleep(3)
            return

# ========== Funciones Read listando resultados con ALERTAS
# LISTAR ID NOMBRE DE PRODCUTO PRECIO CON ALERTAS DE DATO
def productos_precios_alertas(conexion):
    imprimir_tituloSimple(" 👓Productos: Precios con ALertas ")
    
    productos = productos_precios_alertas_db(conexion)
    tabla_con_alerta = []
    alerta = []
    for prod in productos:
                     id_prod, nombre, precio = prod
                     # Inicializar alerta
                     alerta = ""
                     
                     # Verificar de precios
                     if precio >= 0:
                         alerta = "✅"
                     #if not precio or precio == '' or precio <= 0 :
                     else: alerta = "❌ Precio Inválido."
                     
                     tabla_con_alerta.append([id_prod, nombre, precio, alerta])
    print(tabulate(tabla_con_alerta, headers=["Código", "Nombre", "Precio", "Alerta"],  tablefmt="grid"))
    sleep(3)
    return

# LISTAR ID NOMBRE DE PRODCUTO Y ALERTAS DE CODIGO DE HABERLO
def productos_codigos_alertas(conexion):

          imprimir_tituloSimple(" 👓Producto: Código con Alertas ") 
          productos = productos_codigos_alertas_db(conexion)
          tabla_con_alerta = []
          alerta = []
          for prod in productos:
                     id_prod, nombre = prod
                     # Inicializar alerta
                     alerta = ""
                     
                     # Verificar codigos
                     if not id_prod or id_prod == '' or id_prod <= 0 :
                       alerta = "❌ Código Inválido"
                     if alerta == "":
                        alerta = "✅"
                     tabla_con_alerta.append([id_prod, nombre, alerta])
          print(tabulate(tabla_con_alerta, headers=["Código", "Nombre", "Alerta"],  tablefmt="grid"))
          sleep(3)
          return

# LISTAR ID NOMBRE DE PRODCUTO Y SU STOCK CON ALERTAS DE STOCK BAJO O INV+ALIDO
def productos_stock_alertas(conexion):

          imprimir_tituloSimple("👓Productos: Stock con ALertas")
          productos = productos_stock_alertas_db(conexion)
          tabla_con_alerta = []
          alerta = []
          for prod in productos:
                     id_prod, nombre, stock = prod
                     # Inicializar alerta
                     alerta = ""
                     if stock > 10 :
                        alerta = "✅"
                     elif stock >= 0 and stock <= 10:
                       alerta = " ⚠️ Bajo Stock."   
                     else:  alerta = "❌ Stock Inválido"
                     tabla_con_alerta.append([id_prod, nombre, stock, alerta])
          print(tabulate(tabla_con_alerta, headers=["Código", "Nombre", "Stock", "Alerta"],  tablefmt="grid"))
          sleep(3)
          return

# LISTAR ID NOMBRE DE PRODCUTO Y SU CATEGORIA Y ALERTA DE CATEGORIA INVÁLIDA 
def productos_categorias_alertas(conexion):
    #listar_inventario) con este titlo y la funcion tabulate
    imprimir_tituloSimple("👓 Producto: Categoría y ALertas")
  
    productos = productos_categorias_alertas_db(conexion)
    tabla_con_alerta = []
    alerta = []
    for prod in productos:
                     id_prod, nombre, categoria = prod
                     # Inicializar alerta
                     alerta = ""
                     
                     # Verificar de CATEGORIAS
                     if not categoria or categoria == '' :
                       alerta = "❌ Categoría Inválida."
                     if alerta == "":
                        alerta = "✅"
                     tabla_con_alerta.append([id_prod, nombre, categoria, alerta])
    print(tabulate(tabla_con_alerta, headers=["Código", "Nombre", "Categoría", "Alerta"],  tablefmt="grid"))
    sleep(3)
    return

# LISTAR ID NOMBRE DE PRODCUTO Y DESCRIPCION CON ALERTAS
def productos_desc_alertas(conexion):
    #listar_inventario) con este titlo y la funcion tabulate
    imprimir_tituloSimple("👓 Producto: Descripción con Alertas")
    
    productos = productos_desc_alertas_db(conexion)
    productos_formateados = preparar_descripcion_con_envoltura(productos)
      
    tabla_con_alerta = []
    alerta = []
    for prod in productos_formateados:
         
                     id_prod, nombre, descripcion_formateada = prod
                     
                     # Inicializar alerta
                     alerta = ""    
                     # Verificar de DESCRIPCIONES
                     if not descripcion_formateada or descripcion_formateada == '' :
                       alerta = "❌ Descirpcion Inválida."
                     if alerta == "":
                        alerta = "✅"
                     tabla_con_alerta.append([id_prod, nombre, descripcion_formateada, alerta])
    print(tabulate(tabla_con_alerta, headers=["Código", "Nombre", "Descripcion", "Alerta"],  tablefmt="grid"))
    sleep(3)
    return

# ================= Listar graficas =========================

# GR+AFICA DE STOCK DISONIBLE DE CADA PRODUCTO EN EL INVENTARIO
def grafica_stock_producto(conexion):
            # Grafica de stock por producto
            #cursor = conexion.cursor()
            #cursor.execute("SELECT nombre, stock FROM productos")
            nombres_stock = []
            dato_grafica = grafica_stock_producto_db(conexion)
           # Guardo los resultados en una lista de tuplas, cada tupla es (nombre, stock)
            #for fila in cursor.fetchall():
            for fila in dato_grafica:
               nombres_stock.append(fila)
              
            nombres_productos = [dato[0] for dato in nombres_stock]
            stocks_productos = [dato[1] for dato in nombres_stock]
            # Creo una lista de colores para destacar el alerta de stock
            #colors = ['red' if (stock != None and isinstance(stock, int) and stock <= 10) else 'lavender']
            colores =["red" if stock <= 10 else "c" for stock in stocks_productos]
            plt.figure(figsize=(5, 4)) # tamaño del grafico
            plt.bar(nombres_productos, stocks_productos, color=colores) # colores
            plt.xlabel("Producto") # etiqueta o eje de producto, el horizontal
            plt.ylabel("Stock") #etiqueta / eje de cantidad, el vertical
            plt.title("Stock de Productos en Inventario") # titulo del grafico
            plt.xticks(rotation=45, ha='right')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            print(separador)

# GRAFICA DE CAPITAL DE CADA PRODUCTO DISPONIBLE EN EL INVENTARIO
def grafica_capital_producto(conexion):
    
            # Ver gráfi co de capital POR producto
            # Calculo de Totales por Producto
            # se peuden tomar los calculos de capitales_producto_totales()
            """
            conexion = sqlite3.connect('inventario_mabk.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT id_producto, nombre, precio, stock FROM productos")
            """
            # Para esta gráfica, necesitamos calcular el precio total (stock * precio)
            nombres_precio_total = [] # Tupla, producto/capital total del mismo
            capital_total_iventario = 0 # Acumulador del capital del inventario
            #cursor.execute("SELECT nombre, precio, stock FROM productos")
            # Guardo resultados en una lista de tuplas, cada tupla es (nombre, stock, precio)
            datos_grafica = grafica_capital_producto_db(conexion)
            #for fila in cursor.fetchall():
            for fila in datos_grafica:
                 nombre, precio, stock = fila
                 capital_producto = stock * precio
                 # Guardo junto al nombre, el capital total del producto en la tupla
                 nombres_precio_total.append((nombre, capital_producto))
                 capital_total_iventario = capital_total_iventario + capital_producto
                 capital_producto = 0
        
            # Obtengo dos listas d ela tupla, una con el dato del primer indice que es el nombre del producto
            # La segunda lista cpon el segundo dato de la tupla, ubicado en el indice 1 que es el capital
            nombres_productos = [dato[0] for dato in nombres_precio_total]
            capitales_productos = [dato[1] for dato in nombres_precio_total]
            # Gráfico el capital POR producto
            
            # Creo una lista de colores para destacar el alerta de precio
            colores =["c" if capital >= 0 else "red" for capital in capitales_productos]
            plt.figure(figsize=(5, 4)) # tamaño del gráfico
            plt.bar(nombres_productos, capitales_productos, color=colores) # colores
            plt.xlabel(" Producto ") # etiqueta o eje de producto, el horizontal
            plt.ylabel(" Valor Total Del Producto ") # etiqueta / eje de cantidad, el vertical
            plt.title(" Valor Total Por Producto en Inventario ") # título del gráfico
            plt.xticks(rotation=45, ha='right')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            print("\n"*2)
            print(separador)

# ===============  BUSQUEDA
# ********************* BUSCAR PRODUCTO POR ID
# Obtiene todos los datos del producto buscado por ID
def buscar_producto_id(conexion):
    listar_productos(conexion)
    id_buscar = validacion_numerica(input("Código del producto a buscar: "))
    # luego de validar la entrada numérica delusuario, valido la presencia delmproducto en la base de datos
    # si el producto fue ingfresado en la base de datos, obtengo los datos y los retorno
    # hacia esta funcion para mostrarlos pro consola
    producto = buscar_producto_id_db(conexion, id_buscar)
    if producto:
        """
        id_producto, nombre, precio, stock, categoria, descripcion = producto
        # si esta el prodcuto, comienzo con el formateo de la descripcion
        producto_formateado = []
        descripcion_formateada = formatear_descripcion(descripcion)
        # Obtengo los datos para el producto sumando la descriocion formateada
        producto_formateado.append(id_producto, nombre, precio, stock, categoria, descripcion_formateada) 
        """
        
        id_producto, nombre, precio, stock, categoria, descripcion = producto
        
        descripcion_formateada = formatear_descripcion(descripcion)
        datos = [id_producto, nombre, precio, stock, categoria, descripcion_formateada]
        # Encabezados (opcional, para una tabla horizontal más clara)
        headers = ["ID", "Nombre", "Precio", "Stock", "Categoría", "Descripción"]
        # Construir la tabla con tabulate
        print(tabulate([datos], headers=headers, maxcolwidths=[4, 25, 10, 4, 12, 8] , tablefmt="grid"))
        sleep(3)
    else:
        print("❌No existe producto con ese Código")
    return

# ********************** BUSCAR PRODUCTO POR NOMBRE
# Obtiene todos los datos del producto buscado por Nombre
def buscar_producto_nombre(conexion):
    # muestro al usuario su base de datos de prodcutos
    listar_productos(conexion)
    # solicito al usuario elingreso del nombre delproducto a buscar y lo valido
    buscar_nombre= validar_producto(input(" Nombre de Producto a buscar: ").strip().lower().title())
    # con la devolucion de la validacion del input del usuario
    # llamo a la funcion de validacion de existenciay retorno de datos del producto buiscado
    
    producto = buscar_producto_nombre_db(conexion, buscar_nombre)
    # si existe el podcuto, prepraro los datos para salida por consola
    if producto:
        
        id_producto, nombre, precio, stock, categoria, descripcion = producto
        descripcion_formateada = formatear_descripcion(descripcion)
         
         # Imprimir la tabla
        datos_para_tabular = [["ID", id_producto],["Nombre", nombre],
            ["Precio", precio],["Stock", stock], ["Categoría", categoria],
            ["Descripción", descripcion_formateada]]
        print(tabulate(datos_para_tabular, headers=["Campo", "Valor"],maxcolwidths=[10, 60] , tablefmt="grid"))
        sleep(3)
    # Si no existe el producto, le aviso al cliente, es un refuerzo
    else:
        print("❌ No existe producto con ese Nombre.")
        
# ********************** Buscar el codigo del un producto
# Obtengo el ID de un producto buscado por nombre
def buscar_codigo_producto(conexion):
    listar_productos(conexion)
    # solicito al usuario el ingreso del nombre delproducto a buscar y lo valido
    buscar_nombre= validar_producto(input(" Nombre de Producto a buscar código: ").strip().lower().title())
    # con la devolucion de la validacion del input del usuario
    # llamo a la funcion de validacion de existenciay retorno de datos del producto buiscado
    producto = buscar_cod_producto_db(conexion, buscar_nombre)
    # si existe el podcuto, prepraro los datos para salida por consola
    if producto:
        """
        datos_para_tabular = [["Código","Nombre"]] + producto
        # Imprimir la tabla
        print(tabulate(datos_para_tabular, headers="firstrow", tablefmt="grid"))
        """
        headers = ["Código", "Nombre"]
        print(tabulate([producto], headers=headers, tablefmt="grid"))
        sleep(3)
    # Si no existe  elmprodcuto, le aviso al cliente, es un refuerzo
    else:
        print("❌No existe producto con ese Nombre")

# Obtengo el ID de un producto buscado por nombre
def buscar_producto_id(conexion):
    listar_productos(conexion)
    # solicito al usuario el ingreso del nombre delproducto a buscar y lo valido
    buscar_id= validar_id(input(" Id del Producto a buscar nombre: ").strip())
    # con la devolucion de la validacion del input del usuario
    # llamo a la funcion de validacion de existenciay retorno de datos del producto buiscado
    producto = buscar_prod_id_db(conexion, buscar_id)
    # si existe el podcuto, prepraro los datos para salida por consola
    if producto:
        
        headers = ["Id/Código", "Nombre"]
        print(tabulate([producto], headers=headers, tablefmt="grid"))
        sleep(3)
    # Si no existe  elmprodcuto, le aviso al cliente, es un refuerzo
    else:
        print("❌ No existe producto con ese ID/Código.")
        
# *************** Buscar precio de un producto
# Por ID
def buscar_precio_producto_id(conexion):
    listar_productos(conexion)
    id_buscar = validacion_numerica(input("Id/Código del producto a buscar precio: "))
    # Luego de validar la entrada numérica delusuario, valido la presencia delmproducto en la base de datos
    # si el producto fue ingfresado en la base de datos, obtengo los datos y los retorno
    # hacia esta funcion para mostrarlos pro consola
    prod_precio = buscar_precio_producto_id_db(conexion, id_buscar)
    if prod_precio:
        # si esta el prodcuto, preparo los headers de la tabla con el resultado de la busqueda
        headers = ["Nombre", "Precio"]
        print(tabulate([prod_precio], headers=headers, tablefmt="grid"))
        sleep(3)
    else:
        print("❌ No existe producto con ese Id/Código.")
        
# Por NOMBRE
def buscar_precio_producto_nombre(conexion):
    # muestro al usuario su base de datos de prodcutos
    listar_productos(conexion)
    # solicito al usuario elingreso del nombre delproducto a buscar y lo valido
    buscar_nombre= validar_producto(input(" Nombre de Producto a buscar precio: ").strip().lower().title())
    # con la devolucion de la validacion del input del usuario
    # llamo a la funcion de validacion de existenciay retorno de datos del producto buiscado
    prod_precio = buscar_precio_producto_nombre_db(conexion, buscar_nombre)
    # si existe el podcuto, prepraro los datos para salida por consola
    if prod_precio:
        
        headers = ["Nombre", "Precio"]
        print(tabulate([prod_precio], headers=headers, tablefmt="grid"))
        sleep(3)
    # Si no existe elmprodcuto, le aviso al cliente, es un refuerzo
    else:
        print("❌ No existe producto con ese Nombre.")
        
# *************** Buscar Stock de un producto
# Por ID
def buscar_stock_producto_id(conexion):
    listar_productos(conexion)
    id_buscar = validacion_numerica(input("Id/Código del producto a buscar stock: "))
    # Luego de validar la entrada numérica delusuario, valido la presencia delmproducto en la base de datos
    # si el producto fue ingfresado en la base de datos, obtengo los datos y los retorno
    # hacia esta funcion para mostrarlos pro consola
    prod_stock = buscar_stock_producto_id_db(conexion, id_buscar)
    if prod_stock:
        # si esta el producto, preparo los headers de la tabla con el resultado de la busqueda
        headers = ["Nombre", "Stock"]
        print(tabulate([prod_stock], headers=headers, tablefmt="grid"))
        sleep(3)
    else:
        print("❌ No existe producto con ese Id/Código.")
        
# Por NOMBRE
def buscar_stock_producto_nombre(conexion):
    # muestro al usuario su base de datos de prodcutos
    listar_productos(conexion)
    # solicito al usuario elingreso del nombre delproducto a buscar y lo valido
    buscar_nombre= validar_producto(input(" Nombre de Producto a buscar stock: ").strip().lower().title())
    # con la devolucion de la validacion del input del usuario
    # llamo a la funcion de validacion de existencia y retorno de datos del producto buiscado
    prod_stock = buscar_stock_producto_nombre_db(conexion, buscar_nombre)
    # si existe el podcuto, prepraro los datos para salida por consola
    if prod_stock:
       headers = ["Nombre", "Stock"]
       print(tabulate([prod_stock], headers=headers, tablefmt="grid"))
       sleep(3)
    # Si no existe prodcuto, le aviso al cliente, es un refuerzo
    else:
        print("❌ No existe producto con ese Nombre")
        
# ***************  BUSCAR CATEGORIA DE UN PRODUCTO
# Por ID
def buscar_cat_producto_id(conexion):
    listar_productos(conexion)
    id_buscar = validacion_numerica(input("Id/Código del producto a buscar categoría: "))
    # Luego de validar la entrada numérica delusuario, valido la presencia delmproducto en la base de datos
    # si el producto fue ingfresado en la base de datos, obtengo los datos y los retorno
    # hacia esta funcion para mostrarlos pro consola
    prod_categoria= buscar_cat_producto_id_db(conexion, id_buscar)
    if prod_categoria:
        # si esta el prodcuto, preparo los headers de la tabla con el resultado de la busqueda
        headers = ["Nombre", "Categoría"]
        print(tabulate([prod_categoria], headers=headers, tablefmt="grid"))
        sleep(3)
    else:
        print("❌ No existe producto con ese Id/Código.")
        
# Por NOMBRE
def buscar_cat_producto_nombre(conexion):
    # muestro al usuario su base de datos de prodcutos
    listar_productos(conexion)
    # solicito al usuario elingreso del nombre delproducto a buscar y lo valido
    buscar_nombre= validar_producto(input(" Nombre de Producto a buscar la categoría: ").strip().lower().title())
    # con la devolucion de la validacion del input del usuario
    # llamo a la funcion de validacion de existenciay retorno de datos del producto buiscado
    prod_categoria = buscar_cat_producto_nombre_db(conexion, buscar_nombre)
    # si existe el podcuto, prepraro los datos para salida por consola
    if prod_categoria:
        headers = ["Nombre", "Categoría"]
        print(tabulate([prod_categoria], headers=headers, tablefmt="grid"))
        sleep(3)
    # Si no existe elmprodcuto, le aviso al cliente, es un refuerzo
    else:
        print("❌ No existe producto con ese Nombre.")

# ***************  BUSCAR Descripción DE UN PRODUCTO
def preparar_descripcion_con_envoltura_producto(prod_descripcion, ancho_descripcion=40):
    
   producto_formateado= []
   # Envuelve la descripción en la columna "Descripción"
   descripcion_formateada = envolver_texto(prod_descripcion[2], ancho_descripcion)
   producto_formateado.append((prod_descripcion[0], prod_descripcion[1], descripcion_formateada))
   
   return producto_formateado

# Por ID
def buscar_desc_producto_id(conexion):
 
    listar_productos(conexion)
    #id_buscar = validacion_numerica(input("Código del producto a buscar descripción: "))
    id_buscar = validar_id(input("Id/Código del producto a buscar descripción: "))
    # Luego de validar la entrada numérica del usuario, valido la presencia delmproducto en la base de datos
    # si el producto fue ingfresado en la base de datos, obtengo los datos y los retorno
    # hacia esta funcion para mostrarlos pro consola
    producto_descripcion = buscar_desc_producto_id_db(conexion, id_buscar)
    # si existe el podcuto, prepraro los datos para salida por consola
    if producto_descripcion: 
          prod_formateado = preparar_descripcion_con_envoltura_producto(producto_descripcion)
          datos_para_tabular = [["Id", "Nombre", "Descripción"]] + prod_formateado
          # Imprimir la tabla
          print(tabulate(datos_para_tabular, headers="firstrow", tablefmt="grid"))
          sleep(3)
      
    else:
        print("❌ No existe producto con ese ID/Código.")
    return
      
# Por NOMBRE
def buscar_desc_producto_nombre(conexion):
 
    # muestro al usuario su base de datos de prodcutos
    listar_productos(conexion)
    # solicito al usuario elingreso del nombre del producto a buscar y lo valido
    buscar_nombre= validar_producto(input(" Nombre de Producto a buscar la descripción: ").strip().lower().title())
    # con la devolucion de la validacion del input del usuario
    # llamo a la funcion de validacion de existencia y retorno de datos del producto buscado
    prod_descripcion = buscar_desc_producto_nombre_db(conexion, buscar_nombre)
    # si existe el podcuto, prepraro los datos para salida por consola
    if prod_descripcion: 
          producto_formateado = preparar_descripcion_con_envoltura_producto(prod_descripcion)
          datos_para_tabular = [["Id", "Nombre", "Descripción"]] + producto_formateado
          # Imprimir la tabla
          print(tabulate(datos_para_tabular, headers="firstrow", tablefmt="grid"))
          sleep(3)
          return
      
    else:
        print("❌ No existe producto con ese Nombre")
        return
      
# ===============  UPDATE 

# UPDATE PRODUCTO COMPLETO
def actualizar_producto(conexion):
    listar_inventario(conexion)
    id_prod = validacion_numerica(input("ID/Código a actualizar: "))
    nuevo_precio = validar_precio(input("Nuevo precio: "))
    nuevo_stock = validar_stock(input("Nuevo stock: "))
    nueva_categoria = validar_categoria(input("Nueva categoría: "))
    nueva_descripcion = validar_producto(input("Nueva descripción: "))
    if actualizar_producto_db(conexion, id_prod, nuevo_precio, nuevo_stock, nueva_categoria, nueva_descripcion):
        print("✅ Producto modificado correctamente.")
    else:
        print("❌ No existe producto con ese ID/Código.")
    listar_inventario(conexion)
    sleep(2)

# UPDATE PRECIO DE UN PRODUCTO 
def actualizar_precio(conexion):
    listar_precio(conexion)
    id_prod = validacion_numerica(input("Id/Código de Producto a actualizar precio: "))
   
    nuevo_precio = validar_precio(input("Nuevo Precio: "))
    if actualizar_precio_db(conexion, id_prod, nuevo_precio):
          print("✅ Precio Producto modificado correctamente.")
          listar_precio(conexion)
          sleep(2)
    else:
        print("❌ No existe producto con ese Id/Código.")
    return

# UPDATE STOCK DE UN PRODUCTO  
def actualizar_stock(conexion):
    listar_stock(conexion)
    id_prod = validacion_numerica(input("Id/Código de Porducto a actualizar stock: "))
    nuevo_stock = validar_stock(input("Nuevo stock: "))
    if actualizar_stock_db( conexion, id_prod, nuevo_stock):
        print("✅ Stock del producto modificado correctamente.")
        listar_stock(conexion)
        sleep(3)
    else:
        print("❌ No existe producto con ese Id/Código.")
    return

# UPDATE CATEGORIA DE UN PRODUCTO
def actualizar_categoria(conexion):
    listar_categoria(conexion)
    id_prod = validacion_numerica(input("Id/Código del Producto a actualizar categoría: "))
    nueva_categoria = validar_categoria(input("Nueva categoría: "))
    if actualizar_categoria_db(conexion, id_prod, nueva_categoria):
        print("✅ Categoría del Producto modificado correctamente.")
        listar_categoria(conexion)
        sleep(3)
    else:
        print("❌ No existe producto con ese Id/Código.")

# UPDATE DESCRIPCION DE UN PRODUCTO     
def actualizar_descripcion(conexion):
    listar_descripcion(conexion)
    id_prod = validacion_numerica(input("Id/Código del Producto a actualizar descripción: "))
    nueva_descripcion = validar_descripcion(input("Nueva Descripción: (No puede estar vacía, ni contener solo números/caracteres especiales) "))
    if actualizar_descripcion_db(conexion, id_prod, nueva_descripcion):
        print(" ✅ Descripción del Producto modificado correctamente.")
        listar_descripcion(conexion)
        sleep(3)
    else:
        print("❌ No existe producto con ese Id/Código.")
    return
        
# =================  DELETE
# Eliminar producto por id/codigo
def eliminar_producto_codigo(conexion):
    listar_productos(conexion)
    buscar_id = validacion_numerica(input("Id/Código del producto a eliminar: "))
    producto_eliminar = buscar_prod_id_db(conexion, buscar_id)

    if producto_eliminar:
        _, nombre = producto_eliminar
        if eliminar_producto_db(conexion, buscar_id):
            print("✅ Producto eliminado correctamente.")
            eliminar_productoVentas_nombre_db(conexion, nombre)   # <-- CORREGIDO
            listar_inventario(conexion)
            sleep(3)
    else:
        print("❌ No existe producto con ese Id/Código.")
    return

# Eliminar producto por nombre
def eliminar_producto_nombre(conexion):
    listar_inventario(conexion)
    nombre = validar_producto(input("Nombre del producto a eliminar: "))

    if eliminar_producto_nombre_db(conexion, nombre):
        print("✅ Producto eliminado correctamente.")
        eliminar_productoVentas_nombre_db(conexion, nombre)   # <-- CORREGIDO
        listar_inventario(conexion)
        sleep(3)
    else:
        print("❌ No existe producto con ese nombre.")
    return

# DELETE TABLA     
def eliminar_tabla_productos(conexion):
    # Muestro el listado
    listar_inventario(conexion)
    while True:
      respuesta = input(" Para elimimar la tabla, presione: S, para salir presione Enter: ")
      if respuesta == "": 
         break
      elif ((respuesta).strip().lower()) == "s":
        confirmacion = input("Confirma la eliminación de todos los registros?: (S/N) ").strip().lower()
        if confirmacion == "s":
            eliminar_tabla_productos_bd(conexion)
            break
        else: 
            continue
    if eliminar_tabla_productos_bd(conexion):
        print("✅ Registros eliminados correctamente.")
    else:
        print("❌ No existen registros para eliminar")
    return

# =============== REPORTES
# TODAS LAS GTRAFICAS
def ver_graficas(conexion):

      imprimir_tituloSimple("📊 GRÁFICAS 📊")
      grafica_stock_producto(conexion)
      sleep(3)
      grafica_capital_producto(conexion)
      sleep(3)
    #  grafica_stockVendido_producto()
     # sleep(10)
    #  grafica_capitalVendido_producto()
     # sleep(10)
      #grafica_ventas_producto()
      #sleep(10)
      # faltya una de ventas totales a lo,largo de los meses

# REPORTE DE BAJO STOCK CON INDICE INTRODUCIDO POR EL USUARIO
def reporte_bajo_stock(conexion):
    imprimir_tituloSimple(" ⚠️ Producto: Bajo Stock")
    limite = validacion_numerica(input("Mostrar productos con stock ≤: "))
    productos_bajo_stock = obtener_bajo_stock_bd(conexion, limite)
    imprimir_tituloSimple(" ⚠️ Listado: Bajo Stock")
    
    if productos_bajo_stock:
            # Aplicar el formateo a la descripción antes de crear la tabla
      productos_formateados = []
      for producto in productos_bajo_stock:
        id_prod, nombre, stock, precio, categoria, descripcion = producto
        descripcion_formateada = formatear_descripcion(descripcion)
        productos_formateados.append([id_prod, nombre, stock, precio, categoria, descripcion_formateada])

      print(tabulate(productos_formateados, headers=["ID", "Nombre", "Stock", "Precio", "Categoría", "Descripcion"],maxcolwidths=[4, 25, 10, 4, 12, 8] ,tablefmt="grid"))
      sleep(3)
    else:
        print(" ❌ No hay productos para mostrar.")
    return

# Reporte Productos agregados
def listar_productos_agregados(conexion):

  imprimir_tituloSimple(" ✔️ Productos Agregados ")
  for producto_agregado, detalles in productos_agregados.items():
       print(f"{producto_agregado}: {detalles}")
  for i, producto_agregado in enumerate(productos_agregados):
    print(f"{i+1}🔸 {producto_agregado}")
  sleep(2)
  print("\n") 
  return


# Muestro los productos eliminados de la tabla productos eliminados
def listar_productos_eliminados(conexion):
  
  imprimir_tituloSimple( " ⛔ Productos Eliminados : \n")
  resultados = reporte_productos_eliminados(conexion)
  if resultados:
        print("\n📋 Reporte de productos eliminados:")
        print(tabulate(resultados, headers=["ID", "Nombre", "Fecha"], tablefmt="fancy_grid"))
        sleep(3)
  else:
        print("✅ No hay productos eliminados registrados.")

# LISTO REPORTES  VARIOS
def listar_otros_reportes(conexion):
  listar_inventario(conexion)
  listar_inventario_alertas(conexion)
  ver_graficas(conexion)
  listar_productos_agregados(conexion)
  listar_productos_eliminados(conexion)
  print(" Gracias por utilizar nuestro programa!")

# Salimos del Programa
def salir(conexion):
            print("\n" *2)
            print(" 👋 Gracias por usar el programa! 👋 ")
            print(separador)
            cerrar_conexion(conexion)




