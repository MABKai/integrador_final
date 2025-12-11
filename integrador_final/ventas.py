# Modulo ventas

import datetime
from colorama import Fore, Style
from productos_db import *
from productos_validaciones import *
from ventas_db import *
from productos_db import actualizar_stock_db 
from productos_db import buscar_producto_por_nombre_db
from ventas_db import registrar_venta_db
from ventas_db import listar_ventas_bd

def venta_producto(conexion):
    while True:
        print("\n" * 2)
        print("Ingresá el nombre del producto vendido (o Enter para terminar):\n")
        producto_vendido = input("⤴️ Producto vendido: ").strip().title()
        if producto_vendido == "":
            break
        producto_validado= validar_producto(producto_vendido)
        prod = buscar_producto_por_nombre_db(conexion, producto_validado)
        if not prod:
            print("❌ El producto no existe en tu inventario.")
            continue

        id_producto, nombre, precio, stock = prod
        print(f"Producto: {nombre} | Stock: {stock} | Precio: {precio}")

        if stock < 1:
            print("⚠️ No hay stock suficiente para realizar ventas.")
            continue

        venta = input("⤴️ Cantidad vendida: ")
        cantidad_vendida = validar_stock_vendido(venta)
        if cantidad_vendida is None:
            continue

        if cantidad_vendida > stock:
            print("❌ Stock insuficiente para esa venta.")
            continue

        # Calcular venta
        monto_vendido = float(precio) * int(cantidad_vendida)
        fecha_iso = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Registrar venta con UPSERT
        registrar_venta_db(conexion, nombre, cantidad_vendida, monto_vendido, fecha_iso)

        # Actualizar stock
        nuevo_stock = int(stock) - int(cantidad_vendida)
        actualizar_stock_db(conexion, id_producto, nuevo_stock)   
        print(f"✅ Venta registrada: {cantidad_vendida} x {nombre} | Total: {monto_vendido:.2f} | Stock actual: {nuevo_stock}")

# codigo reeemplazado, funciona perfectamente
# Venat de producto, obteniendo datos de tablas productos y ventas y actualizando ambas
"""
def venta_producto(conexion):

 while True:
    print("\n" * 2) # doble espacio
    print(" Ingresá el nombre del producto vendido:(o presioná Enter para terminar): \n")
    producto_vendido = input(" ⤴️ Producto vendido: ").lower().title().strip()
     # Condición para salir del bucle si el código está vacío
    if producto_vendido == "":
        break
    # salgo de la actividad
    # Valido que se ingresen letras
    buscar_nombre = validar_producto( producto_vendido) 
    # obtengo el stock del productpara hacer los calculos de venta
    prod_stock = buscar_stock_producto_nombre_db(conexion, buscar_nombre)
    print(prod_stock)
    if prod_stock:
        # desempaco los datos
        nombre, stock = prod_stock
        # los muestro
        print(f" 💠 Producto: {nombre}, Stock: {stock} unidades. \n")
        stock_original = stock 
        if stock_original >=1 :
        # Bucle para intoducir cantidad vendida, validar y hacer los calculos por cada producto
         while True:
           # try:
                venta = (input(" ⤴️ Cantidad vendida: o presione Enter para salir: "))
                if venta == "":
                    break
                cantidad_vendida = validar_nuevo_stock(venta)
                # verifico si el stock es sufiviente para concretar la venta
                if stock_original < cantidad_vendida:
                    print(f" ❌ Stock Insuficiente. \n")
                    # vuelve a pedir un numero para la venta
                    continue
                nuevo_stock = stock_original - cantidad_vendida 
                # Calculo de resta del stock segun la cantidad vendoida ingresada
                # actualizo el stock en lña tabla productos
                actualizar_stock_nombre_db( buscar_nombre, nuevo_stock)           
                # trabajare en hacer una funciom db de ventas de producto para los calculos
                
                # Calculos ventas por producto
                # consigo los datos de precio del producto de la tabla prodcutos
                prod_precio = buscar_precio_producto_nombre_db(conexion, buscar_nombre)
                if prod_precio:
                    nombre, precio = prod_precio
                    # calculo el monto vendido para sumar a la tabla ventas
                    montoTotal_vendido = precio * cantidad_vendida
                    # Obtengo los datos de la tabla ventas  del producto vendido 
                    datos_ventas = buscar_montoTotal_cantidad_producto_db(conexion, buscar_nombre)
                    if datos_ventas:
                         # si ya existen, los actualizo
                         #desempaco los datos recibidos
                         producto_nombre,cantidad, monto_total = datos_ventas
                         nueva_cantidad = int(cantidad) + int(cantidad_vendida)
                         nuevo_montoTotal = float(monto_total) + float(montoTotal_vendido)
                         nueva_fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                         # actualizo los datos en la tabla ventas si hay datos previos
                         actualizar_montoTotal_Cantidad_db(conexion, producto_nombre, nueva_cantidad, nuevo_montoTotal, nueva_fecha)
                    else:
                         # de no existir, los inserto
                         producto_nombre = str(producto_nombre)
                         nueva_cantidad = int(cantidad_vendida)
                         nuevo_montoTotal = float(montoTotal_vendido)
                         nueva_fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                         insertar_venta_db(conexion, producto_nombre, cantidad_vendida, montoTotal_vendido, nueva_fecha)
                    print("✅ Venta registrada correctamente")
                    listar_ventas(conexion)
                    listar_stock(conexion)
                    break
                else:
                    print(f" ❌ El producto '{producto_validado}' no tiene un precio válido. \n")
        # Alerto el bajo stock para concretar la venta
        else:
            print (" ⚠️ No tiene stock suficiente para realizar ventas")
    else:
        print(" ❌ El producto no existe en su inventario")
 return


"""
# LISTO LA TABLA DE VENTAS    
def listar_ventas(conexion):
    productos_ventas = listar_ventas_bd(conexion)
    if productos_ventas:
      #for producto_venta in productos_ventas:
      #  producto_nombre, cantidad, monto_total, fecha = producto_venta  
      print(tabulate(productos_ventas, headers=[ "Nombre", "Cantidad Vendida", "Monto Vendido", "Fecha"],maxcolwidths=[None, None, None, None] ,tablefmt="grid"))
      sleep(3)
    else:
        print(" ❌ No hay productos para mostrar.")
    return

# id producto, nombre precio de la venta  stock_vendido y fecha
def eliminar_tabla_ventas(conexion):
    # Muestro el listado
    listar_ventas(conexion)
    while True:
      respuesta = input(" Para eliminar la tabla, presione: S, para salir presione Enter: ")
      if respuesta == "": 
         break
      elif ((respuesta).strip().lower()) == "s":
        confirmacion = input("Confirma la eliminaci+on de todos los registros?: (S/N)").strip().lower()
        if confirmacion == "s":
            eliminar_tabla_ventas_bd(conexion)
            break
        else: 
            continue
    if eliminar_tabla_ventas_bd(conexion):
        print("✅ Registors eliminados correctamente.")
    else:
        print("❌ No existen registros para eliminar")
    return

# Graficas de ventas juntas EN LA MISMA FIGURA
# GRAFICA CANTIDAD VENDIDA POR PRODUCTO Y MONTO TOTAL VENDIDO POR PRODUCTO
def graficas_stock_capitalVendido_producto(conexion):
        nombres_cantidad = []
        nombres_productos = []
        cantidad_productos = []
        datos_para_grafica = grafica_cantidad_producto_db(conexion)
       # Para Grafica Cantidad o Stock Vendido Por Porducto
        for fila in datos_para_grafica:
            nombres_cantidad.append(fila)
              
        nombres_productos = [dato[0] for dato in nombres_cantidad]
        cantidad_productos = [dato[1] for dato in nombres_cantidad]
        #  grafica una junto a la otra
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4
                                                                        ))
        #  Stock total vendido por producto
        # determino el color de las barras de esta gráfica
        ax1.bar(nombres_productos, cantidad_productos, color='skyblue')
         # Seteo el titulo de la gráfica
        ax1.set_title('Stock Total Vendido por Producto')
        # Etiqueto el eje X
        ax1.set_xlabel('Producto')
        # Etiqueto el eje Y
        ax1.set_ylabel('Unidades Vendidas')
        # determino que el eje x tenga las etiquetas rotadas 45 grados
        ax1.tick_params(axis='x', rotation=45)
        # determino el estilo de linea para eje y
        ax1.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Para Grafica Monto Total Vendido por Producto
        nombres_montoTotal = []
        datos_para_grafica2 = grafica_montoTotal_producto_db(conexion)
        for fila in datos_para_grafica2:
            nombres_montoTotal.append(fila)
              
        nombres_productos2 = [dato[0] for dato in nombres_montoTotal]
        montoTotal_productos = [dato[1] for dato in nombres_montoTotal]
        
        # Precio total vendido por producto
        # Color para las barras de estea gráfica
        ax2.bar(nombres_productos2, montoTotal_productos, color='lightgreen')
        ax2.set_title('Monto Total Vendido por Producto') # Titulo
        ax2.set_xlabel('Producto') # Etiqueta eje x
        ax2.set_ylabel('Monto Total Vendido ($)') # Etiqueta eje y
        ax2.tick_params(axis='x', rotation=45)
        ax2.grid(axis='y', linestyle='--', alpha=0.7)
        # Ajustar el diseño para evitar superposiciones
        plt.tight_layout()
        # Mostrar los gráficos
        plt.show()

# Graficas de Ventas separadas
# GRAFICA DE STOCK TOTAL VENDIDO POR PRODUCTO
def grafica_stockVendido_producto(conexion):
            nombres_cantidad = []
            nombres_productos = []
            cantidad_productos = []
            datos_para_grafica = grafica_cantidad_producto_db(conexion)
            # Para Grafica Cantidad o Stock Vendido Por Porducto
            for fila in datos_para_grafica:
               nombres_cantidad.append(fila)
              
            nombres_productos = [dato[0] for dato in nombres_cantidad]
            cantidad_productos = [dato[1] for dato in nombres_cantidad]
            plt.figure(figsize=(5, 4)) # tamaño del gráfico
            #  Stock total vendido por producto
            # determino el color de las barras de esta gráfica
            plt.bar(nombres_productos, cantidad_productos, color='skyblue')
            # Seteo el titulo de la gráfica
            plt.title('Stock Total Vendido por Producto')
            # Etiqueto el eje X
            plt.xlabel('Producto')
            # Etiqueto el eje Y
            plt.ylabel('Unidades Vendidas')
            # determino que el eje x tenga las etiquetas rotadas 45 grado
            plt.xticks(rotation=45, ha='right')
            # determino el estilo de linea para eje y
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            # Mostrar gráfico
            plt.show()
            print("\n")
 
# GRAFICA DE CAPITAL VENDIDO TOTAL POR PRODUCTO           
def grafica_capitalVendido_producto(conexion):
               # Para Grafica Monto Total Vendido por Producto
            nombres_montoTotal = []
            datos_para_grafica2 = grafica_montoTotal_producto_db(conexion)
            for fila in datos_para_grafica2:
              nombres_montoTotal.append(fila)
              
            nombres_productos2 = [dato[0] for dato in nombres_montoTotal]
            montoTotal_productos = [dato[1] for dato in nombres_montoTotal]
        
            # Color para las barras de estea gráfica
            plt.figure(figsize=(5, 4)) # tamaño del gráfico
            plt.bar(nombres_productos2, montoTotal_productos, color='lightgreen')
            plt.title('Capital Vendido por Producto') # Titulo
            plt.xlabel('Producto') # Etiqueta eje x
            plt.ylabel('Capital Vendido ($)') # Etiqueta eje y
            plt.xticks(rotation=45, ha='right')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            # Ajustar el diseño para evitar superposiciones
            plt.tight_layout()
            # Mostrar gráfico
            plt.show()
            print("\n")