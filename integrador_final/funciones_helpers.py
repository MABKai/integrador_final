# Funciones ayudantes
"""
Contiene funciones que no son pertenencientes
al CRUD propiamente ni a validaciones
ni a la creacion de las tablas etc

"""
#from main import *
#from productos_db import *
#from productos_validaciones import *

# ================= Salida por Pantalla ========
ANCHO = 80  # Defino Ancho
separador = "=" * ANCHO # Defino el separador

def imprimir_titulo(titulo, funcion_a_llamar):
    """
    Imprime un título formateado y luego ejecuta una función.

    Los argumentos son
        titulo (str): El texto del título.
        funcion_a_llamar (callable): La función que se ejecutará después del título del que necesitamos en el momento
    """
    print(separador)
    print("\n" * 2)  # doble espacio
    print(titulo.center(ANCHO))
    print("\n")
    funcion_a_llamar()
    print(separador)
    print("\n" * 2)  # doble espacio

def imprimir_tituloSimple(titulo):
    """
    Imprime un título formateado y luego ejecuta una función.

    Los argumentos son
        titulo (str): El texto del título.
        funcion_a_llamar (callable): La función que se ejecutará después del título del que necesitamos en el momento
    """
    print(separador)
    print("\n" * 2)
    print(titulo.center(ANCHO))
    print("\n")
"""
Para que la descripcion NO rompa la tabla al listar inventario, inventario con alertas y capital
o el liestar decsriocion y descriocion con los alertas
"""
def formatear_descripcion(descripcion, longitud_maxima=5):
    """
    Formatea la descripción ya que es un campo con texto muy
    largo.
    Si es mayor que la longitud máxima, la trunca y añade puntos suspensivos.
    """
    if len(descripcion) > longitud_maxima:
        return descripcion[:longitud_maxima] + "..."
    return descripcion

def envolver_texto(texto, ancho_maximo):
    palabras = texto.split()
    linea_actual = ""
    lineas = []
    for palabra in palabras:
        if len(linea_actual) + len(palabra) + 1 <= ancho_maximo:
            linea_actual += palabra + " "
        else:
            lineas.append(linea_actual.strip())
            linea_actual = palabra + " "
    if linea_actual.strip():
        lineas.append(linea_actual.strip())
    return "\n".join(lineas)







