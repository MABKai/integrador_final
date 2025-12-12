# interfaz_aux.py
import sqlite3
# Dicicioandrio global
#Para guardar tempporalmente los nuevos productos
#agreagdos por default o con los datos completos"
productos_agregados = {}
# ------------------------------
# VALIDACIONES
# ------------------------------

def validar_nombre(nombre):
    if not nombre or not nombre.replace(" ", "").isalpha():
        raise ValueError("El nombre debe contener solo letras y no estar vacío.")
    return nombre.strip()

def validar_precio(precio):
    try:
        precio = float(precio)
        if precio < 0:
            raise ValueError("El precio debe ser positivo.")
        return precio
    except:
        raise ValueError("El precio debe ser un número válido.")

def validar_stock(stock):
    try:
        stock = int(stock)
        if stock < 0:
            raise ValueError("El stock debe ser positivo.")
        return stock
    except:
        raise ValueError("El stock debe ser un número entero válido.")

def validar_categoria(categoria):
    if not categoria or not categoria.replace(" ", "").isalpha():
        raise ValueError("La categoría debe contener solo letras y no estar vacía.")
    return categoria.strip()

def validar_descripcion(descripcion):
    if not descripcion.strip():
        raise ValueError("La descripción no puede estar vacía.")
    return descripcion.strip()

# ------------------------------
# CRUD AUXILIARES
# ------------------------------

def obtener_productos(conexion):
    conexion = sqlite3.connect('inventario_mabk.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT id_producto, nombre, precio, stock, categoria, descripcion FROM productos")
    return cursor.fetchall()

def actualizar_producto(conexion,  id_producto, precio, stock, categoria, descripcion):
    precio = validar_precio(precio)
    stock = validar_stock(stock)
    categoria = validar_categoria(categoria)
    descripcion = validar_descripcion(descripcion)
    conexion = sqlite3.connect('inventario_mabk.db')
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE productos
        SET precio=?, stock=?, categoria=?, descripcion=?
        WHERE i id_producto=?
    """, (precio, stock, categoria, descripcion,  id_producto))
    conexion.commit()

def agregar_producto(conexion, nombre, precio, stock, categoria, descripcion):
    nombre = validar_nombre(nombre)
    precio = validar_precio(precio)
    stock = validar_stock(stock)
    categoria = validar_categoria(categoria)
    descripcion = validar_descripcion(descripcion)
    conexion = sqlite3.connect('inventario_mabk.db')
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO productos (nombre, precio, stock, categoria, descripcion)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, precio, stock, categoria, descripcion))
    conexion.commit()
      # Guardar también en el diccionario
    productos_agregados[nombre] = {
        "precio": precio,
        "stock": stock,
        "categoria": categoria,
        "descripcion": descripcion
    }

def agregar_producto_placeholder(conexion, nombre):
    nombre = validar_nombre(nombre)
    conexion = sqlite3.connect('inventario_mabk.db')
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO productos (nombre, precio, stock, categoria, descripcion)
        VALUES (?, 0, 0, '', 'A modificar')
    """, (nombre,))
    conexion.commit()
      # Guardar también en el diccionario
    productos_agregados[nombre] = {
        "precio": 0,
        "stock": 0,
        "categoria": "Sin categoría",
        "descripcion": ""
    }

def eliminar_producto(conexion,  id_producto):
    conexion = sqlite3.connect('inventario_mabk.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, precio, stock, categoria, descripcion FROM productos WHERE id_producto=?", ( id_producto,))
    producto = cursor.fetchone()
    if producto:
        # Guardar en productos_eliminados
        cursor.execute("""
            INSERT INTO productos_eliminados (nombre, precio, stock, categoria, descripcion)
            VALUES ( ?, ?, ?, ?, ?)
        """, producto)
        # Eliminar de productos
        cursor.execute("DELETE FROM productos WHERE id_producto=?", ( id_producto,))
        conexion.commit()
        return True
    return False

# ------------------------------
# MODIFICACIONES ESPECÍFICAS
# ------------------------------

def actualizar_precio(conexion,  id_producto, precio):
    precio = validar_precio(precio)
    conexion = sqlite3.connect('inventario_mabk.db')
    cursor = conexion.cursor()
    cursor.execute("UPDATE productos SET precio=? WHERE  id_producto=?", (precio,  id_producto))
    conexion.commit()

def actualizar_stock(conexion,  id_producto, stock):
    stock = validar_stock(stock)
    conexion = sqlite3.connect('inventario_mabk.db')
    cursor = conexion.cursor()
    cursor.execute("UPDATE productos SET stock=? WHERE  id_producto=?", (stock,  id_producto))
    conexion.commit()

def actualizar_categoria(conexion,  id_producto, categoria):
    categoria = validar_categoria(categoria)
    conexion = sqlite3.connect('inventario_mabk.db')
    cursor = conexion.cursor()
    cursor.execute("UPDATE productos SET categoria=? WHERE id_producto=?", (categoria, id_producto))
    conexion.commit()

def actualizar_descripcion(conexion, id_producto, descripcion):
    descripcion = validar_descripcion(descripcion)
    conexion = sqlite3.connect('inventario_mabk.db')
    cursor = conexion.cursor()
    cursor.execute("UPDATE productos SET descripcion=? WHERE  id_producto=?", (descripcion, id_producto))
    conexion.commit()

# ------------------------------
# BÚSQUEDAS
# ------------------------------

def buscar_productos(conexion, campo, valor):
    conexion = sqlite3.connect('inventario_mabk.db')
    cursor = conexion.cursor()
    query = f"SELECT id_producto, nombre, precio, stock, categoria, descripcion FROM productos WHERE {campo} LIKE ?"
    cursor.execute(query, ('%' + valor + '%',))
    return cursor.fetchall()
