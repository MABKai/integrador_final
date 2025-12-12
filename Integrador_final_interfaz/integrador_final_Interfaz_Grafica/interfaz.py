# interfaz.py
from productos import*
from productos_db import *
from ventas_db import *
from ventas import *
import tkinter as tk
from tkinter import ttk, messagebox
from interfaz_aux import (
    obtener_productos, actualizar_producto, agregar_producto,
    eliminar_producto, agregar_producto_placeholder, buscar_productos,
    actualizar_precio, actualizar_stock, actualizar_categoria, actualizar_descripcion
)

from interfaz_aux import (
    obtener_productos, actualizar_producto, agregar_producto,
    eliminar_producto, agregar_producto_placeholder, buscar_productos,
    actualizar_precio, actualizar_stock, actualizar_categoria, actualizar_descripcion
)

def mostrar_inventario(conexion):
    root = tk.Tk()
    root.title("Inventario")

    # Tabla
    tree = ttk.Treeview(root, columns=("ID", "Nombre", "Precio", "Stock", "Categoría", "Descripción"), show="headings")
    tree.pack(fill="both", expand=True)

    for col in ("ID", "Nombre", "Precio", "Stock", "Categoría", "Descripción"):
        tree.heading(col, text=col)
        tree.column(col, width=120)

    def cargar_productos(productos=None):
        tree.delete(*tree.get_children())
        if productos is None:
            productos = obtener_productos(conexion)
        for prod in productos:
            desc_truncada = prod[5][:30] + "..." if len(prod[5]) > 30 else prod[5]
            tree.insert("", "end", values=(prod[0], prod[1], prod[2], prod[3], prod[4], desc_truncada))
      
    cargar_productos()
    # Funciones CRUD
    # --- Funciones de edición ---
    # Agregar producto con sus datos
    
    def agregar_nuevo():
     add_win = tk.Toplevel(root)
     add_win.title("Agregar producto completo")

     # Campos a ingresar
     campos = ["Nombre", "Precio", "Stock", "Categoría", "Descripción"]
     entradas = {}

     for i, campo in enumerate(campos):
        tk.Label(add_win, text=campo+":").grid(row=i, column=0, padx=5, pady=5)
        if campo == "Descripción":
            entradas[campo] = tk.Text(add_win, width=40, height=5)
            entradas[campo].grid(row=i, column=1, padx=5, pady=5)
        else:
            entradas[campo] = tk.Entry(add_win)
            entradas[campo].grid(row=i, column=1, padx=5, pady=5)

     def guardar_nuevo():
        try:
            agregar_producto(
                conexion,
                entradas["Nombre"].get(),
                entradas["Stock"].get(),
                entradas["Precio"].get(),
                entradas["Categoría"].get(),
                entradas["Descripción"].get("1.0", "end").strip()
            )
            cargar_productos()
            messagebox.showinfo("Éxito", "Producto agregado correctamente.")
            add_win.destroy()
        except ValueError as e:
            messagebox.showerror("Error de validación", str(e))

     tk.Button(add_win, text="Agregar producto", command=guardar_nuevo).grid(
        row=len(campos), column=0, columnspan=2, pady=10
    )

    
    
    def editar_producto_completo():
        item = tree.selection()
        if not item:
            messagebox.showwarning("Atención", "Seleccione un producto.")
            return
        valores = tree.item(item, "values")
        id_producto, nombre, precio, stock, categoria, descripcion = valores

        edit_win = tk.Toplevel(root)
        edit_win.title(f"Editar producto {nombre}")

        campos = {"Precio": precio, "Stock": stock, "Categoría": categoria, "Descripción": descripcion}
        entradas = {}
        for i, (campo, valor) in enumerate(campos.items()):
            tk.Label(edit_win, text=campo+":").grid(row=i, column=0)
            if campo == "Descripción":
                entradas[campo] = tk.Text(edit_win, width=40, height=5)
                entradas[campo].insert("1.0", valor)
                entradas[campo].grid(row=i, column=1)
            else:
                entradas[campo] = tk.Entry(edit_win)
                entradas[campo].insert(0, valor)
                entradas[campo].grid(row=i, column=1)

        def guardar():
            try:
             actualizar_producto(conexion,  id_producto,
                                entradas["Precio"].get(),
                                entradas["Stock"].get(),
                                entradas["Categoría"].get(),
                                entradas["Descripción"].get("1.0", "end").strip())
             cargar_productos()
             messagebox.showinfo("Éxito", f"Producto {nombre} actualizado.")
             edit_win.destroy()
            except ValueError as e:
                messagebox.showerror("Error de validación", str(e))

        tk.Button(edit_win, text="Guardar", command=guardar).grid(row=len(campos), column=0, columnspan=2)

    # --- Funciones específicas ---
    def editar_precio():
        item = tree.selection()
        if not item: return
        valores = tree.item(item, "values")
        id_producto, nombre, precio = valores[0], valores[1], valores[2]
        nuevo = simple_input("Nuevo precio", precio)
        if nuevo:
            try:
              actualizar_precio(conexion,  id_producto, nuevo)
              cargar_productos()
            except ValueError as e:
                messagebox.showerror("Error de validación", str(e))
            

    def editar_stock():
        item = tree.selection()
        if not item: return
        valores = tree.item(item, "values")
        id_producto, nombre, stock = valores[0], valores[1], valores[3]
        nuevo = simple_input("Nuevo stock", stock)
        if nuevo:
         try:
            actualizar_stock(conexion,  id_producto, nuevo)
            cargar_productos()
         except ValueError as e:
                messagebox.showerror("Error de validación", str(e))

    def editar_categoria():
        item = tree.selection()
        if not item: return
        valores = tree.item(item, "values")
        id_producto, nombre, categoria = valores[0], valores[1], valores[4]
        nuevo = simple_input("Nueva categoría", categoria)
        if nuevo:
            try:
             actualizar_categoria(conexion,  id_producto, nuevo)
             cargar_productos()
            except ValueError as e:
                messagebox.showerror("Error de validación", str(e))

    def editar_descripcion():
        item = tree.selection()
        if not item: return
        valores = tree.item(item, "values")
        id_producto, nombre, descripcion = valores[0], valores[1], valores[5]
        nuevo = simple_input("Nueva descripción", descripcion)
        if nuevo:
            try:
               actualizar_descripcion(conexion,  id_producto, nuevo)
               cargar_productos()
            except ValueError as e:
                messagebox.showerror("Error de validación", str(e))
  
    # --- Agregar rápido ---
    def agregar_rapido():
        nombre = simple_input("Nombre del producto", "")
        if nombre:
            try:
                agregar_producto_placeholder(conexion, nombre)
                cargar_productos()
            except ValueError as e:
                messagebox.showerror("Error de validación", str(e))

    # --- Eliminar con guardado ---
    def eliminar():
        item = tree.selection()
        if not item: return
        valores = tree.item(item, "values")
        id_producto, nombre = valores[0], valores[1]
        if eliminar_producto(conexion,  id_producto):
            try:
              cargar_productos()
              messagebox.showinfo("Éxito", f"Producto {nombre} eliminado y guardado en productos_eliminados.")
            except ValueError as e:
                messagebox.showerror("Error de validación", str(e))
   
    # --- Buscar/Filtrar ---
    def buscar():
        campo = campo_combo.get()
        valor = buscar_entry.get()
        if valor:
            try:
             productos = buscar_productos(conexion, campo.lower(), valor)
             cargar_productos(productos)
            except ValueError as e:
                messagebox.showerror("Error de validación", str(e))

    # --- Helpers ---
    def simple_input(titulo, valor_inicial=""):
        win = tk.Toplevel(root)
        win.title(titulo)
        tk.Label(win, text=titulo+":").pack()
        entry = tk.Entry(win); entry.insert(0, valor_inicial); entry.pack()
        result = {"val": None}
        def ok():
            result["val"] = entry.get()
            win.destroy()
        tk.Button(win, text="OK", command=ok).pack()
        win.wait_window()
        return result["val"]

    # --- Botones ---
    tk.Button(root, text="Agregar producto", command=agregar_nuevo).pack(pady=5)
    tk.Button(root, text="Editar completo", command=editar_producto_completo).pack(pady=5)
    tk.Button(root, text="Editar precio", command=editar_precio).pack(pady=5)
    tk.Button(root, text="Editar stock", command=editar_stock).pack(pady=5)
    tk.Button(root, text="Editar categoría", command=editar_categoria).pack(pady=5)
    tk.Button(root, text="Editar descripción", command=editar_descripcion).pack(pady=5)
    tk.Button(root, text="Agregar Producto/Default", command=agregar_rapido).pack(pady=5)
    tk.Button(root, text="Eliminar producto", command=eliminar).pack(pady=5)

    # --- Buscar ---
    buscar_frame = tk.Frame(root)
    buscar_frame.pack(pady=10)
    tk.Label(buscar_frame, text="Buscar por:").grid(row=0, column=0)
    campo_combo = ttk.Combobox(buscar_frame, values=["id", "nombre", "precio", "stock", "categoria", "descripcion"])
    campo_combo.current(1)
    campo_combo.grid(row=0, column=1)
    buscar_entry = tk.Entry(buscar_frame); buscar_entry.grid(row=0, column=2)
    tk.Button(buscar_frame, text="Buscar", command=buscar).grid(row=0, column=3)

    root.mainloop()

