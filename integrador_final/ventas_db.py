# Tabla Ventas Base de Datos inventario_mabk
# Marcela, Alejandra Brahim, DNI 20010395 mar.ale.bra@gmail.com
import sqlite3
import matplotlib.pyplot as plt
from tabulate import tabulate
from time import sleep
import pandas as pd
import numpy as np
#from ventas import *
import datetime


#from main import *
from productos_validaciones import *
from funciones_helpers import *

# conecto a la tabla de ventas
def conectar_db():
    """
    Establece una conexión con la base de datos SQLite3 'inventario.db'.
    Crea la base de datos si no existe.
    Retorna el objeto de conexión y un objeto cursor.
    """
    try:
        
      return sqlite3.connect("inventario_mabk.db")
     # conexion = sqlite3.connect('inventario.db')
     # cursor = conexion.cursor()
      #return conexion, cursor
    except sqlite3.Error as e:
        print("❌ Error al conectar con la base de datos:", e)
        return None

# Read
# Muestro la tabla Ventas
def listar_ventas_bd(conexion):

    try:  
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT producto_nombre, cantidad, monto_total, fecha  FROM ventas")
        productos_ventas = cursor.fetchall()
        conexion.close()
        return productos_ventas       
    except sqlite3.Error as e:
        print("❌ Error:", e)
        return None

def registrar_venta_db(conexion, producto_nombre, cantidad_vendida, monto_vendido, fecha_iso):
    """
    Inserta o actualiza automáticamente la venta usando UPSERT.
    """
    try:
      conexion = sqlite3.connect('inventario_mabk.db')
      cursor = conexion.cursor()
      cursor.execute(
        """
        INSERT INTO ventas (producto_nombre, cantidad, monto_total, fecha)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(producto_nombre) DO UPDATE SET
            cantidad = ventas.cantidad + excluded.cantidad,
            monto_total = ventas.monto_total + excluded.monto_total,
            fecha = excluded.fecha
        """,
        (producto_nombre, int(cantidad_vendida), float(monto_vendido), str(fecha_iso)))
      conexion.commit()
    except sqlite3.Error as e:
        print("❌ Error:", e)
        return None

    
# Graficas
# unidades/stock/cantidad vendida total POR producto
def grafica_cantidad_producto_db(conexion):
    try:
            # Grafica de stock por producto
            conexion = sqlite3.connect('inventario_mabk.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT producto_nombre, cantidad FROM ventas")
            dato_grafica = cursor.fetchall()
            return dato_grafica
    except sqlite3.Error as e:
                print("❌ Error:", e)
                return []        

# Grafica de monto total  vendido por cada producto  
def grafica_montoTotal_producto_db(conexion):
    try:
            # Ver gráfi co de capital POR producto
            # Calculo de Totales por Producto
            # se peuden tomar los calculos de capitales_producto_totales()
            conexion = sqlite3.connect('inventario_mabk.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT producto_nombre, monto_total FROM ventas")
            
            return cursor.fetchall()
    except sqlite3.Error as e:
                print("❌ Error:", e)
                return None
            
# Delete
# eliminar producto por id 
def eliminar_productoVentas_db(id_prod):
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM ventas WHERE id = ?", (id_prod,))
        conexion.commit()
        if cursor.rowcount == 0:
            print("❌ No existe un producto con ese ID.")
        else:
            print("✅ producto eliminado correctamente.")
           
    except sqlite3.Error as e:
        print("❌ Error al eliminar:", e)

# eliminar producto de la tabla po nombre
def eliminar_productoVentas_nombre_db(conexion, nombre):
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM ventas WHERE producto_nombre = ?", (nombre,))
        conexion.commit()
        if cursor.rowcount == 0:
            print("❌ No existe un producto con ese nombre.")
        else:
            print("✅ producto eliminado correctamente.")
           
    except sqlite3.Error as e:
        print("❌ Error al eliminar:", e)

# eliminar la tabla ventas inventario
def eliminar_tabla_ventas_bd(conexion):
    
    try:
       conexion = sqlite3.connect('inventario_mabk.db')
       cursor = conexion.cursor()

       # Elimino todos los productos o registros de la tabla 'ventas'
       cursor.execute("DELETE FROM ventas")
       conexion.commit() # Guardo los cambios
       print(" ✅ Todos los productos han sido eliminados exitosamente.")
    except Exception as e:
       print(f" ❌ Ocurrió un error: {e}")
       conexion.rollback() 
       # Deshace los cambios si hubo un error
    finally:
       cursor.close()
       conexion.close()
       
# Buscar
def buscar_montoTotal_cantidad_producto_db(conexion, buscar_nombre):
    
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT producto_nombre, cantidad, monto_total FROM ventas WHERE (producto_nombre) =(?) ", (buscar_nombre,))
        datos_venta= cursor.fetchone()
        return datos_venta
    
    except sqlite3.Error as e:
        print("❌ Error al buscar por nombre:", e)
        return None

# Update
def actualizar_montoTotal_Cantidad_db(conexion, producto_nombre, nueva_cantidad, nuevo_montoTotal, nueva_fecha):
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        
        # Aseguramos que los valores sean del tipo correcto
        
        
        nueva_cantidad = int(nueva_cantidad)         # cantidad como entero
        nuevo_montoTotal = float(nuevo_montoTotal)   # monto como número
        nueva_fecha = str(nueva_fecha)               # fecha como texto (ISO string)
        producto_nombre = str(producto_nombre)
        cursor.execute(
            "UPDATE ventas SET cantidad = ?, monto_total = ?, fecha = ? WHERE producto_nombre = ?",
            (nueva_cantidad, nuevo_montoTotal, nueva_fecha, producto_nombre)
        )
        conexion.commit()
        
        if cursor.rowcount == 0:
            print("❌ No existe un producto con ese nombre.")
        else:
            print("✅ Venta actualizada correctamente.")
           
    except sqlite3.Error as e:
        print(f"❌ Error al actualizar el producto: {e}")

# procedimientos para actualizar la tabla de ventas 
# Insert
def insertar_venta_db(conexion, producto_nombre, cantidad, monto_total, fecha):
    """
    Inserta un nuevo registro de venta en la tabla 'ventas'.
    """
    try:
        cursor = conexion.cursor()

        # Aseguramos tipos correctos
        cantidad = int(cantidad)
        monto_total = float(monto_total)
        fecha = str(fecha)  # convertir a texto (ej: '2025-12-05 11:45:00')

        cursor.execute(
            "INSERT INTO ventas (producto_nombre, cantidad, monto_total, fecha) VALUES (?, ?, ?, ?)",
            (producto_nombre, cantidad, monto_total, fecha)
        )
        conexion.commit()
        print(f"✅ Venta registrada: {cantidad} unidades de {producto_nombre}, total ${monto_total}.")
    except sqlite3.Error as e:
        print(f"❌ Error al insertar venta: {e}")
"""
def cerrar_conexion(conexion):
    try:
        if conexion:
            conexion.close()
    except sqlite3.Error as e:
        print("❌ Error al cerrar:", e)
"""
