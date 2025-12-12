# productos_db.py
# Marcela, Alejandra Brahim, DNI 20010395 mar.ale.bra@gmail.com
"""
contiene las operaciones de creacion de la tabla si no existe, de la inciializacion de la misma, si no esta 
inicializada.
funciones CRUD
librerias

"""
import sqlite3
import matplotlib.pyplot as plt
from tabulate import tabulate
from time import sleep
import pandas as pd
import numpy as np
from datetime import datetime


#from main import *
from productos_validaciones import *
from funciones_helpers import *

# conexion a la base d edatos
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

def crear_tablas(conexion):
    """
    Crea las tablas 'productos', 'ventas' y 'productos_eliminados' en la base de datos.
    """
    conexion = sqlite3.connect('inventario_mabk.db')
    cursor = conexion.cursor()

    # Tabla de productos
    cursor.execute("DROP TABLE IF EXISTS productos")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            precio REAL NOT NULL DEFAULT 0,
            stock INTEGER NOT NULL DEFAULT 0,
            categoria TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            tipo TEXT CHECK(tipo IN ('rapido','completo')) NOT NULL DEFAULT 'completo'
        )
    """)
    conexion.commit()

    # Tabla de ventas
    cursor.execute("DROP TABLE IF EXISTS ventas")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto_nombre TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            monto_total REAL NOT NULL,
            fecha TEXT NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY (producto_nombre) REFERENCES productos(nombre)
        )
    """)
    conexion.commit()

    # Tabla productos eliminados
    cursor.execute("DROP TABLE IF EXISTS productos_eliminados")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos_eliminados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL,
            categoria TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            fecha TEXT NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY (nombre) REFERENCES productos(nombre)
        )
    """)
    conexion.commit()

    print("Tablas verificadas/creadas exitosamente.")


def cerrar_conexion(conexion):
    try:
        if conexion:
            conexion.close()
    except sqlite3.Error as e:
        print("❌ Error al cerrar:", e)

# Diccionario para las cargas inciiales y bases de datos 

productos = {
           "Aloe Vera": {"precio": 25000.20, "stock": 100,  "categoria": "Suculenta", 
           "descripcion": " Aloe barbadensis Mill es una suculenta con hojas largas y carnosas, que contienen un gel transparente con propiedades hidratantes, antiinflamatorias y cicatrizantes."},
           "Strelitzia Reginae":{"precio": 105000.00, "stock": 20, "categoria": "Ornamental", 
           "descripcion": "(Ave del Paraíso): originaria de Sudáfrica, conocida por sus flores exóticas naranjas que recuerdan a una ave en vuelo. Prefiere climas cálidos y subtropicales, y requiere suelos bien drenados y un riego moderado."  },
           "Strelitzia Nicolai": { "precio": 102000.00, "stock": 10, "categoria": "Ornamental", 
          "descripcion": "(Ave del paraiso) Originaria de Sudáfrica, conocida por sus flores exóticas que recuerdan a un ave en vuelo, puede alcanzar hasta 10 mts de altura. Sus flores son blancas con toques azulados y sus hojas pueden superar los 2 mts de longitud."},
           "Cicca":{ "precio": 78000.00,"stock": 10, "categoria": "Palmera",
           "descripcion": "Planta primitiva que ha evolucionado desde el Paleozoico tardío, considerada fósil viviente debido a su resistencia y longevidad. Hojas grandes, follaje denso, tronco grueso y robusto, coronado por una roseta de hojas pinnadas coriáceas y brillantes."},
           "Orquidea": { "precio": 50000.99, "stock": 18,  "categoria": "Exotica", 
           "descripcion": " Apreciadas por su belleza y resistencia, requieren condiciones adecuadas de luz y riego."},
           "Pindo": {"precio": 43999.99, "stock": 13, "categoria": "Palmera", 
           "descripcion": "Conocido por sus flores grandes y hermosas, es una opción popular en jardinería y decoración de interiores."},
           "Pandurata HG": {"precio": 120000.50, "stock": 10, "categoria": "Ornamental", 
           "descripcion": "Valorada por su follaje robusto y su capacidad para atraer aves, lo que la convierte en una opción atractiva para paisajismo."},
           "Alocasia": {"precio": 80000.00,"stock": 54, "categoria": "Ornamnetal", 
           "descripcion": " Bbrillantes hojas decorativas ornamentales en forma de corazón, con bordes ondulados. Ieal para decoración de interiores y exteriores, por su apariencia exótica. Sus hojas gigantes se asemejan a las orejas de un elefante"},
           "Pandurata HC": {"precio": 110000.00, "stock": 32,  "categoria": "Ornamental",
           "descripcion": "Valorada por su follaje robusto y su capacidad para atraer aves, con hojas pequeñas, es apreciada por su belleza y resistencia."},
           "Platycerium" : {"precio": 87000.00, "stock": 44, "categoria": "Helecho", 
           "descripcion": "Conocida por sus hojas en forma de cuernos de alce, requiere condiciones específicas de luz y riego."},
           "Potus": {"precio": 20000, "stock": 12, "categoria": "Trepadora", 
           "descripcion": "Epipremnum aureum, originaria del sudeste asiático. Se caracteriza por sus hojas en forma de corazón, que pueden ser verdes o variegadas, y su capacidad para adaptarse a diferentes condiciones de luz y temperatura."},
           "Alegria": {"precio":  25000, "stock": 12, "categoria": "Ornamental", 
           "descripcion": "Vvalorada por su follaje denso y su capacidad para atraer aves, siendo ideal para jardines y espacios verdes."},
           "Spatyphilium": {"precio": 45000.00, "stock": 12,  "categoria": "Ornamental", 
           "descripcion": "Conocida por sus flores grandes y hermosas, apreciada en jardinería y decoración de interiores."},
           "Geranio": { "precio": 20000.00, "stock": 19,  "categoria": "Ornamental", 
           "descripcion": "Planta es apreciada por su follaje y coloridas flores, que se adapta bien a diversas condiciones climáticas."},
           "Mango": {"precio": 30000, "stock": 23,  "categoria": "Frutal", 
           "descripcion": "Árbol que puede alcanzar 3 a 45 mts. Las hojas de color verde oscuro, flores con cinco pétalos rojos y frutos amarillos, verdes naranjas."},
           "Palta": {"precio": 12000, "stock": 12,  "categoria": "Frutal", 
           "descripcion": "Árbol que puede alcanzar hasta 30 mts. Hojas grandes, ovaladas y brillantes. Flores pequeñas de color verde. Fruto ovalado con pulpa cremosa y hueso central grande"}
           }

def carga_inicial(conexion):
    
   conexion = sqlite3.connect("inventario_mabk.db")
   cursor = conexion.cursor()

   # for producto, precio, stock, categoria in productos:
   for nombre, datos in productos.items():
      try:
        
         # cursor.execute("INSERT INTO productos (producto, precio, stock, categoria) VALUES (?, ?, ?, ?)", (producto, precio, stock, categoria))
         cursor.execute("INSERT INTO productos (nombre, precio, stock, categoria, descripcion) VALUES (?, ?, ?, ?, ?)",
                   (nombre, datos['precio'], datos['stock'], datos['categoria'], datos['descripcion']))
     
      except sqlite3.IntegrityError:
          print(f" ❌ Ya existe el producto  {nombre}. No se cargó.")

   conexion.commit() 

productos_venta = {
           "Aloe Vera": {"cantidad": 1, "monto_total": 25000.20, "fecha": "2025-12-03"},
           "Strelitzia Reginae":{"cantidad": 10, "monto_total": 1050000.00 , "fecha": "2025-11-23"},
           "Strelitzia Nicolai": { "cantidad": 10, "monto_total": 1020000.00, "fecha": "2025-12-03"},
           "Cicca":{ "cantidad": 1,"monto_total": 78000.00, "fecha": "2025-11-23"},
           "Orquidea": { "cantidad": 1, "monto_total": 50000.99,  "fecha": "2025-11-29"},
           "Pindo": {"cantidad": 1, "monto_total":43999.99 , "fecha": "2025-11-29"},
           "Pandurata HG": {"cantidad": 10, "monto_total": 1200000.50, "fecha": "2025-12-03"},
           "Alocasia": {"cantidad": 6,"monto_total": 480000.00, "fecha": "2025-12-02"},
           "Pandurata HC": {"cantidad": 20, "monto_total": 2200000.00,  "fecha": "2025-12-02"},
           "Platycerium" : {"cantidad": 10, "monto_total": 870000.00, "fecha": "2025-12-03"},
           "Potus": {"cantidad": 30, "monto_total": 600000.00, "fecha": "2025-12-01"},
           "Alegria": {"cantidad":  20, "monto_total": 500000.00, "fecha": "2025-12-02"},
           "Spatyphilium": {"cantidad": 10, "monto_total": 450000, "fecha": "2025-11-05"},
           "Geranio": { "cantidad": 7,"monto_total": 140000.00, "fecha": "2025-11-04"}, 
           "Mango": {"cantidad": 1, "monto_total": 30000.00,  "fecha": "2025-12-01"},
           "Palta": {"cantidad": 1, "monto_total": 12000.00,  "fecha": "2015-12-01"}
           }

def carga_inicial_ventas(conexion):
   conexion = sqlite3.connect("inventario_mabk.db")
   cursor = conexion.cursor()
   for producto_nombre, datos in productos_venta.items():
      try:     
         # cursor.execute("INSERT INTO productos (producto, precio, stock, categoria) VALUES (?, ?, ?, ?)", (producto, precio, stock, categoria))
         cursor.execute("INSERT INTO ventas (producto_nombre, cantidad, monto_total, fecha) VALUES ( ?, ?, ?, ?)",
                   (producto_nombre, datos['cantidad'], datos['monto_total'], datos['fecha']))
      except sqlite3.IntegrityError:
          print(f" ❌ Ya existe el producto  {producto_nombre}. No se cargó.")
   print("Datos iniciales de ventas cargados exitosamente.")
   conexion.commit()
   
# ====== Funcion para Create productos con datos o datos por defaukt
def insertar_producto_db(conexion, nombre, precio, stock, categoria, descripcion):
    try:
        conexion = sqlite3.connect("inventario_mabk.db")
        cursor = conexion.cursor()
        query = """
           INSERT INTO productos (nombre, precio, stock, categoria, descripcion)
           VALUES (?, ?, ?, ?, ?)
      """
        cursor.execute(query, (nombre, precio, stock, categoria, descripcion))
        conexion.commit()
        print("✅ Producto añadido correctamente")
    except sqlite3.Error as e:
        print("❌ Error al agregar producto:", e)
        conexion.rollback()

#=========================  FUNCIONES ***** READ (LISTAR/VER/BUSCAR)
# Inventario Producto id, nombre, precio, stock, categoria, descripcion formateada
def listar_inventario_bd(conexion):

    try:  
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre, precio, stock, categoria, descripcion FROM productos")
       
        return cursor.fetchall()
        
    except sqlite3.Error as e:
        print("❌ Error:", e)
        return []
    
 # Invetario Id producto, nombre, precio, stock, categoria, descripcion y alertas de cada uno   

# Inventario Producto id, nombre, precio, stock, categoria, descripcion formateada con ALERTAS
def listar_inventario_alertas_bd(conexion):

    try:  
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre, precio, stock, categoria, descripcion FROM productos")
     
        return cursor.fetchall()
    except sqlite3.Error as e:
        print("❌ Error al listar:", e)
        return []

# Inventaro con capital por Producto
def capital_inventario_productos_db(conexion):
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre, precio, stock FROM productos")
        productos = cursor.fetchall()
        return productos
    except sqlite3.Error as e:
                print("❌ Error al listar:", e)
                return []

# Funcion  MOSTRAR STOCK SIN ALERTAS 

def listar_stock_bd(conexion):

    try:  
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre, stock FROM productos")
  
        return cursor.fetchall()
    
    except sqlite3.Error as e:
        print("❌ Error:", e)
        return []
       
# FUNCION MOSTRAR PRECIOS SIN ALERTAS
def listar_precio_bd(conexion):

    try:  
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre, precio FROM productos")
        return cursor.fetchall()
    
    except sqlite3.Error as e:
        print("❌ Error:", e)
        return []
    
# Funcion Mostrar Productos y su categoria en formato lista SIN ALERTAS BORRAR?
def listar_categoria_bd(conexion):

    try:  
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre, categoria FROM productos")
        return cursor.fetchall()
    
    except sqlite3.Error as e:
        print("❌ Error:", e)
        return []
    
# Funcion Mostrar Productos y su descripcion en formato lista SIN ALERTAS BORRAR?
def listar_descripcion_bd(conexion):

    try:  
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre, descripcion FROM productos")
        return cursor.fetchall()
    
    except sqlite3.Error as e:
        print("❌ Error:", e)
        return []
    
# Funcion mostrar los productos segun su codigo SIN ALERTAS BORRAR?
def listar_codigo_bd(conexion):

    try:  
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre FROM productos")
        return cursor.fetchall()
    
    except sqlite3.Error as e:
        print("❌ Error:", e)
        return []

# LISTAR la lista de PRODUCTOS DISPONIBLES
def listar_productos_bd(conexion):

    try:  
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre FROM productos")
        return cursor.fetchall()
    
    except sqlite3.Error as e:
        print("❌ Error:", e)
        return []

#  LISTAR PRODUCTOS PRECIOS, con ALERTAS
def productos_precios_alertas_db(conexion):
    
    try:
          conexion = sqlite3.connect('inventario_mabk.db')
          cursor = conexion.cursor()
          cursor.execute("SELECT id_producto, nombre, precio FROM productos")
          return cursor.fetchall()
    except sqlite3.Error as e:
        print("❌ Error:", e)
        return []
         
#  LISTAR PRODUCTO en relación con CODIGOS Y ALERTAS
def productos_codigos_alertas_db(conexion):

    try:
          conexion = sqlite3.connect('inventario_mabk.db')
          cursor = conexion.cursor()
          cursor.execute("SELECT id_producto, nombre FROM productos")
          return cursor.fetchall()
          
    except sqlite3.Error as e:
                print("❌ Error al listar:", e)
                return []
    

# LISTAR PRODUCTO en relacion CATEGORIA CON ALERTAS
def productos_categorias_alertas_db(conexion):
   
    try:
          conexion = sqlite3.connect('inventario_mabk.db')
          cursor = conexion.cursor()
          cursor.execute("SELECT id_producto, nombre, categoria FROM productos")
          return cursor.fetchall()
    except sqlite3.Error as e:
          print("❌ Error al listar:", e)
          return []
                
#  LISTAR LOS PRODUCTOS CON SU STOCK Y ALERTAS
def productos_stock_alertas_db(conexion):
          
    try:
          conexion = sqlite3.connect('inventario_mabk.db')
          cursor = conexion.cursor()
          cursor.execute("SELECT id_producto, nombre, stock FROM productos")
          return cursor.fetchall()
          
    except sqlite3.Error as e:
                print("❌ Error al listar:", e)
                return []

# LISTAR LOS PRODUCTOD Y SU DESCRIPCION  CON ALERTAS
def productos_desc_alertas_db(conexion):

    try:
          conexion = sqlite3.connect('inventario_mabk.db')
          cursor = conexion.cursor()
          cursor.execute("SELECT id_producto, nombre, descripcion FROM productos")
          return cursor.fetchall()
          
    except sqlite3.Error as e:
                print("❌ Error al listar:", e)
                return []

# ====================================
  
# FUNCIONES DE BUSQUEDA DE DATOS

# ******* BUSCAR un PRODCUTO por NOMBRE
def buscar_producto_nombre_db(conexion, buscar_nombre):
    global datos_para_tabular
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre, precio, stock, categoria, descripcion FROM productos WHERE (nombre) = (?)", (buscar_nombre,))
        #producto =cursor.fetchall()
        #return producto
        return cursor.fetchone()
    except sqlite3.Error as e:
        print("❌ Error al buscar por nombre:", e)
        return []
    
# ******** BUSCAR un ** PRODUCTO por ** ID
def buscar_producto_id_db(conexion, id_producto):
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre, precio, stock, categoria, descripcion FROM productos WHERE id_producto = ?", (id_producto,))
        producto = cursor.fetchone()
        return producto
        #return cursor.fetchall()
    except sqlite3.Error as e:
        print("❌ Error al buscar por código:", e)
        return None

# ************** Buscar CÓDIGO de un producto
def buscar_cod_producto_db(conexion, buscar_nombre):
   
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre FROM productos WHERE (nombre) = (?)", (buscar_nombre,))  
        producto = cursor.fetchone()
        return producto
    except sqlite3.Error as e:
        print("❌ Error al buscar por nombre:", e)
        return None
    
# ************** Buscar Nombre Producto por id
def buscar_prod_id_db(conexion, buscar_id):
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre FROM productos WHERE (id_producto) = (?)", (buscar_id,))  
        producto = cursor.fetchone()
      
        return producto
    
    except sqlite3.Error as e:
        print("❌ Error al buscar por ID:", e)
        return None


#*******************  BUSCAR PRECIO de un producto
# Por NOMBRE
def buscar_precio_producto_nombre_db(conexion, buscar_nombre):
    
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, precio FROM productos WHERE (nombre) =(?) ", (buscar_nombre,))
       
        prod_precio =  cursor.fetchone()
      
        return prod_precio
       
    except sqlite3.Error as e:
        print("❌ Error al buscar por nombre:", e)
        return []
    
# Por codigo/ID
def buscar_precio_producto_id_db(conexion, id_producto):
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, precio FROM productos WHERE id_producto = ?", (id_producto,))
        prod_precio = cursor.fetchone()
       
        return prod_precio
    except sqlite3.Error as e:
        print("❌ Error al buscar por código:", e)
        return []

# ***************** Buscar stock de un producto
# Por nombre
def buscar_stock_producto_nombre_db(conexion, buscar_nombre):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, stock FROM productos WHERE nombre = ?", (buscar_nombre,))
        prod_stock = cursor.fetchone()
        return prod_stock  # Devuelve (nombre, stock) o None si no existe
    except sqlite3.Error as e:
        print("❌ Error al buscar por nombre:", e)
        return None

# Por codigo/ID
def buscar_stock_producto_id_db(conexion, id_producto):
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, stock FROM productos WHERE id_producto = ?", (id_producto,))
        prod_stock=  cursor.fetchone()
      
        return prod_stock
    except sqlite3.Error as e:
        print("❌ Error al buscar por código:", e)
        return []
    
# ************** buscar CATEGORIA de un producto
# Por nombre
def buscar_cat_producto_nombre_db(conexion, buscar_nombre):
  
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, categoria FROM productos WHERE nombre = ?", (buscar_nombre,))
       
        prod_categoria =cursor.fetchone()
     
        return prod_categoria
       
    except sqlite3.Error as e:
        print("❌ Error al buscar por nombre:", e)
        return []
# Por codigo/ID
def buscar_cat_producto_id_db(conexion, id_producto):
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre, categoria FROM productos WHERE id_producto = ?", (id_producto,))
        prod_categoria = cursor.fetchone()
      
        return prod_categoria
    except sqlite3.Error as e:
        print("❌ Error al buscar por código:", e)
        return []

# ************* buscar Descripción de un PRODUCTO

# Por nombre
def buscar_desc_producto_nombre_db(conexion, buscar_nombre):
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
      
        cursor.execute("SELECT id_producto, nombre, descripcion FROM productos WHERE nombre = ?", (buscar_nombre,))
        prod_descripcion = cursor.fetchone()
      
        return prod_descripcion
       
    except sqlite3.Error as e:
        print("❌ Error al buscar por nombre:", e)
        return []
# Por codigo/ID
def buscar_desc_producto_id_db(conexion, id_buscar):
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
      
        cursor.execute("SELECT id_producto, nombre, descripcion FROM productos WHERE id_producto = ?", (id_buscar,))
        producto_descripcion = cursor.fetchone()
    
        return producto_descripcion
       
    except sqlite3.Error as e:
        print("❌ Error al buscar por ID:", e)
        return []

# =========== buscar precio y stock de un producto por nombre
def buscar_producto_por_nombre_db(conexion, producto_validado):
    try:
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
      
        cursor.execute(
        "SELECT id_producto, nombre, precio, stock FROM productos WHERE nombre = ?",
        (producto_validado)
    )
       
        prod = cursor.fetchone()
        return prod
    
    except sqlite3.Error as e:
        print("❌ Error al buscar por nombre:", e)
        return None
# ======= funciones DB UPDATE
# Update producto con sus datos
def actualizar_producto_db(conexion, id_producto, nuevo_precio, nuevo_stock, nueva_categoria, nueva_descripcion):
    try:
        conexion = sqlite3.connect("inventario_mabk.db")
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE productos
            SET precio = ?, stock = ?, categoria = ?, descripcion = ?
            WHERE id_producto= ?
        """, (nuevo_precio, nuevo_stock, nueva_categoria, nueva_descripcion, id_producto))
        conexion.commit()
        if cursor.rowcount == 0:
            print("❌ No existe un producto con ese código.")
        else:
            print("✅ Producto actualizado correctamente.")
            
    except sqlite3.Error as e:
        print("❌ Error al actualizar el producto:", e)
        
# ACtualizar PRECIO 
def actualizar_precio_db(conexion, id_producto, nuevo_precio):
    try:
        conexion = sqlite3.connect("inventario_mabk.db")
        cursor = conexion.cursor()
        
        cursor.execute(
                "UPDATE productos SET precio = ? WHERE id_producto = ?", # Sin la coma extra
                (nuevo_precio, id_producto) # Los parámetros deben ir en una tupla
            )
        conexion.commit()
        if cursor.rowcount == 0:
            print("❌ No existe un producto con ese código.")
        else:
            print("✅ Precio del Producto actualizado correctamente.")
           
    except sqlite3.Error as e:
        print(f"❌ Error al actualizar el producto: {e}") # Usa f-string para formatear

# ACTUALIZAR STOCK DE UN PRODUCTO   
def actualizar_stock_db(conexion, id_producto, nuevo_stock):   
#def actualizar_stock_db( id_producto, nuevo_stock):
    try:
        conexion = sqlite3.connect("inventario_mabk.db")
        
        cursor = conexion.cursor()
        """
        # funciona con mi otro codigo
        cursor.execute("UPDATE productos SET stock = ? WHERE id_producto = ?", (nuevo_stock, id_producto))
        """
        cursor.execute(
        "UPDATE productos SET stock = ? WHERE id_producto = ?",
        (int(nuevo_stock), int(id_producto))
    )
        conexion.commit()
        
        if cursor.rowcount == 0:
            print("❌ No existe un producto con ese código.")
        else:
            print("✅ Stock del Producto actualizado correctamente.")
       
    except sqlite3.Error as e:
        print("❌ Error al actualizar el producto:", e)
    
def  actualizar_stock_nombre_db( buscar_nombre, nuevo_stock):
    try:
        conexion = sqlite3.connect("inventario_mabk.db")
     
        cursor = conexion.cursor()
        cursor.execute("UPDATE productos SET stock = ? WHERE nombre = ?", (nuevo_stock, buscar_nombre))
        conexion.commit()
        if cursor.rowcount == 0:
            print("❌ No existe un producto con ese nombre.")
        else:
            print("✅ Stock del Producto actualizado correctamente.")
       
    except sqlite3.Error as e:
        print("❌ Error al actualizar el producto:", e)

# Actualizar CATEGORIA de un producto
def actualizar_categoria_db(conexion, id_producto, nueva_categoria):
    try:
        conexion = sqlite3.connect("inventario_mabk.db")
        cursor = conexion.cursor()
        cursor.execute("UPDATE productos SET categoria = ? WHERE id_producto = ?", (nueva_categoria, id_producto) )
        conexion.commit()
        if cursor.rowcount == 0:
            print("❌ No existe un producto con ese código.")
        else:
            print("✅ Categoría del Producto actualizado correctamente.")
            
    except sqlite3.Error as e:
        print("❌ Error al actualizar el producto:", e)

# Actualizar DESCRIPCIÒN de un producto
def actualizar_descripcion_db(conexion, id_producto, nueva_descripcion):
    try:
        conexion = sqlite3.connect("inventario_mabk.db")
        cursor = conexion.cursor()
        cursor.execute("UPDATE productos SET descripcion = ? WHERE id_producto = ?", (nueva_descripcion, id_producto) )
        conexion.commit()
        if cursor.rowcount == 0:
            print("❌ No existe un producto con ese código.")
        else:
            print("✅ Descripciòn del Producto actualizado correctamente.")
            
    except sqlite3.Error as e:
        print("❌ Error al actualizar el producto:", e)
        
# ======== Funciones DB DELETE
# Eliminar producto en DB por ID
def eliminar_producto_db(conexion, buscar_id):
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT nombre, stock, precio, descripcion, categoria
            FROM productos
            WHERE id_producto = ?
        """, (buscar_id,))
        producto = cursor.fetchone()

        if producto is None:
            print("❌ No existe un producto con ese Id/Código.")
            return False

        nombre, stock, precio, descripcion, categoria = producto

        cursor.execute("""
            INSERT INTO productos_eliminados (nombre, stock, precio, descripcion, categoria, fecha)
            VALUES (?, ?, ?, ?, ?, datetime('now'))
        """, (nombre, stock, precio, descripcion, categoria))

        cursor.execute("DELETE FROM productos WHERE id_producto = ?", (buscar_id,))
        conexion.commit()
        return True

    except sqlite3.Error as e:
        print("❌ Error al eliminar:", e)
        return False


# Eliminar producto en DB por nombre
def eliminar_producto_nombre_db(conexion, nombre):
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT nombre, stock, precio, descripcion, categoria
            FROM productos
            WHERE nombre = ?
        """, (nombre,))
        producto = cursor.fetchone()

        if producto is None:
            print("❌ No existe un producto con ese nombre.")
            return False

        nombre, stock, precio, descripcion, categoria = producto

        cursor.execute("""
            INSERT INTO productos_eliminados (nombre, stock, precio, descripcion, categoria, fecha)
            VALUES (?, ?, ?, ?, ?, datetime('now'))
        """, (nombre, stock, precio, descripcion, categoria))

        cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre,))
        conexion.commit()
        return True

    except sqlite3.Error as e:
        print("❌ Error al eliminar:", e)
        return False

# eliminar la tabla inventario
def eliminar_tabla_productos_bd(conexion):
    # Conecta a la base de datos
    #conexion = sqlite3.connect('inventario.db')
    try:
       conexion = sqlite3.connect('inventario_mabk.db')
       cursor = conexion.cursor()

       # Elimino todos los productos o registros de la tabla 'productos'
       cursor.execute("DELETE FROM productos")
       conexion.commit() # Guardo los cambios
       print(" ✅ Todos los productos han sido eliminados exitosamente.")
    except Exception as e:
       print(f" ❌ Ocurrió un error: {e}")
       conexion.rollback() 
       # Deshace los cambios si hubo un error
    finally:
       cursor.close()
       conexion.close()
       
  
# ==================== Funciones para reportes 

# Ver graficos de stock y capital POR producto EN EL INVENTARIO DISPONIBLE
def grafica_stock_producto_db(conexion):
    try:
            # Grafica de stock por producto
            conexion = sqlite3.connect('inventario_mabk.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre, stock FROM productos")
            dato_grafica = cursor.fetchall()
            return dato_grafica
    except sqlite3.Error as e:
                print("❌ Error:", e)
                return []        
        
def grafica_capital_producto_db(conexion):
    try:
            # Ver gráfi co de capital POR producto
            # Calculo de Totales por Producto
            # se peuden tomar los calculos de capitales_producto_totales()
            conexion = sqlite3.connect('inventario_mabk.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre, precio, stock FROM productos")
            return cursor.fetchall()
    except sqlite3.Error as e:
                print("❌ Error:", e)
                return []

# ====================== REPORTE Bajo Stock
def obtener_bajo_stock_bd(conexion, limite): 
    global productos_bajo_stock  
    try:  
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre, precio, stock, categoria, descripcion FROM productos")
        productos = cursor.fetchall()
       
        productos_bajo_stock = []
        for producto in productos:
            id_producto, nombre, precio, stock, categoria, descripcion = producto
            if stock <= limite:
              productos_bajo_stock.append(producto)
            else:
              print(" No Hay productos con Bajo Stock mas bajo que {limite} unidades.")
        return productos_bajo_stock
    except sqlite3.Error as e:
        print("❌ Error:", e)
        return []
    

def reporte_productos_eliminados(conexion):
     try:  
        conexion = sqlite3.connect('inventario_mabk.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos_eliminados ORDER BY fecha DESC")
        resultados = cursor.fetchall()
        return resultados
     except sqlite3.Error as e:
        print("❌ Error:", e)
        return []
    
    
