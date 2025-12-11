# productos_validaciones.py
# Marcela, Alejandra Brahim, DNI 20010395 mar.ale.bra@gmail.com
"""
contiene las funciones de validacion
validacion: Stock, Precio, Categoria, Descripcion, numeros, Productos,
"""

import re

# ==================== FUNCIONES DE VALIDACIÓN DE INGRESOS/DATOS
# Validacion de nombres de productos/categoiras"

# Validaci+on de ingresos numericos int (stock, codigo actividades)
# ============  ==============================================
def validar_id(id_buscar):
  """
   Por medio de la libreria re, valido el numero introducido como codigo,que sea numero y positivo. Refuerzo con que sea mayor o igual a cero.
   Ademas valido que no este vacío ni sean espacios el dato ingresado y que no sea un codigo repetido.
   Si es valido, lo retorno despues de guardarlo en la lista de codigos existentes.
   Mientras no sea álido,pide el reingreso
  """
  global codigo_validado
  while True:
      
        # Expresión regular para validar números enteros (positivos o negativos)
        #codigo_nuevo = input("Ingrese el codigo nuevo: ")
        patron = re.compile(r'^-?\d+$')
        if patron.match(id_buscar):
            try:
                codigo_validado = int(id_buscar)
                print("✅ Dato válido.")
                return codigo_validado

            except ValueError:
                print("❌ Dato ingresado inválido.")
                id_buscar = input("Ingrese ID: ")
        else:
            print("❌ Ingreso inválido. Por favor, ingrese solo números enteros.")
            id_buscar = input("Ingrese ID: ")

# ============ Validación de Stock ============================================
def validar_stock(nuevo_stock):
    """
    Por medio de la libreria re, valido el stock, que sea numerico y positivo. En este caso que sea entero sin decimales. Pide al usuario que ingrese un número entero válido.
    Vuelve a pedir el ingreso hasta que se cumplan las condiciones.

    Hasta que no sea válido, pide re ingreso
    Argmento, el numero ingresado por el usuario en este caso es stock
    return: el numero int osea el  stock valdiado

    """

    global stock_validado
    while True:
        #stock_nuevo = input(" Ingrese stock: ")
        # Expresión regular para validar números enteros (positivos o negativos)
        patron = re.compile(r'^-?\d+$')
        nuevo_stock = str(nuevo_stock)
        if patron.match(nuevo_stock):
            try:
              #  stock_validado = int(nuevo_stock)
              nuevo_stock = int(nuevo_stock)
              #  if stock_validado >= 1 and stock_validado <= 10:
              if nuevo_stock >= 1 and nuevo_stock <=10:
                 alerta = "⚠️ Stock Bajo"
                 print(alerta)
              print("✅ Stock Ingresado.")
              return nuevo_stock
            except ValueError:
                print("❌Error:dato ingresado inválido.")
                nuevo_stock = 0
                nuevo_stock = input(" Ingrese stock: ")
        else:
            print("❌Error: Ingreso inválido. Por favor, ingrese solo números enteros.")
            nuevo_stock= input(" Ingrese stock: ")


def validar_precio(nuevo_precio):
    """
    Pide al usuario que ingrese un número flotante válido.
    Vuelve a pedir el ingreso hasta que se cumplan las condiciones.
    Argumento: el precio ingresado por el usuario
    Return: el numero osea precio float validado
        # Expresión regular para validar números de punto flotante (enteros o con decimales)
        # ^: inicio de la cadena
        # -?: signo opcional
        # \d+: uno o más dígitos
        # (\.\d+)? : un punto seguido de uno o más dígitos, todo esto es opcional

    """
    global precio_validado
    while True:
        
        patron = re.compile(r'^-?\d+(\.\d+)?$')
        if patron.match(nuevo_precio):
            try:
                precio_validado = float(nuevo_precio)
                return precio_validado
            except ValueError:
                # Esto no debería ocurrir si el patrón regex es correcto, pero es una buena práctica
                print("Error: entrada inválido.")
                nuevo_precio = input(" Precio del Producto: ")
        else:
            print("Error: Ingreso inválido.")
            nuevo_precio= input(" Precio del Producto: ")


# validacion de numeros enteros para opciones o indices
def validacion_numerica(busca_indice):
   """
    funcion que valida un numero in.
    Argumento es el numero a validar por ejemplo el índice o id
    devuelve el nunmero validado
    solicta reingreso hasta que sea un ingreso correcto
   """
   global posicion_validada
   while not busca_indice or not busca_indice.isdigit():
            print("❌Error: No puede contener letras o caracteres especiales o estar vacio.")
            busca_indice= input("Introduce número: ")
   try:
      posicion_validada = int(busca_indice)
      while not posicion_validada > 0:
                    print("❌ Error: El número debe ser positivo.")
                    busca_indice= input("Introduce número: ): ")
      print (" ✅ Dato Válido. ")
      return posicion_validada
  
   except ValueError:
      print("❌ Dato inválido).")
      busca_indice= input("Introduce número positivo: ")

# Validación de nombre de producto =========================
def validar_producto(nombre):
    global producto_validado
    """
    valido con la libreria re, que el nombre ingresado
    no este vacío ni tenga caracteres numéricos ni raros,
    ni que sea repetido con el bucle hasta que no se
    ingrese un nombre válido, sigue pidiendolo.
    
    Argumento es el nombre del producto
    return el nombre validado
    
    """
    while not nombre or nombre.isspace() or not re.fullmatch(r'[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ ]+', nombre):
        print("  ❌ Ingreso inválido.")
        nombre = input("Introduce producto válido: ").strip().lower().title()

    print("✅ Producto válido.")
    producto_validado = (nombre).strip().lower().title()
    # Retorno el nombre validado
    return producto_validado


# Validación de categoria ======================================================
def validar_categoria(nueva_categoria):
    """
    valido con la libreria re, que el nombre ingresado
    no este vacío ni tenga caracteres numéricos ni raros,
    ni que sea repetido con el bucle hasta que no se
    ingrese un nombre válido, sigue pidiendolo.
    Argumento es la nueva categoria ingresada por el usuario
    Return la categoria validada
    """
    global categoria_validada
   
    while not nueva_categoria or nueva_categoria.isspace() or not re.fullmatch(r'[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ ]+', nueva_categoria):

        print("  ❌ Ingreso inválido.")
        nueva_categoria =  input("Introduce categoria válida: ").strip().lower().title()

    print("✅ Categoría válida.")
    categoria_validada = nueva_categoria
    # Retorno el nombre validado
    return categoria_validada

def validar_descripcion(nueva_descripcion):
    """
    Valida la descripción de una planta usando regex para que contenga 
    al menos una letra, un número y no solo espacios o caracteres especiales.
    
    En este caso uso La expresión regular:
    como siempre ^: Inicio de la cadena.
    (?=.*[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]): Debe haber al menos una letra (mayúscula o minúscula, incluyendo acentos).
    (?=.*\d): Debe haber al menos un dígito
    [a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\d\s#%\-()\[\].,]+: Coincide con uno o más caracteres que sean letras, dígitos, espacios o los símbolos permitidos.
    $: Fin de la cadena.
    El argumento es el texto de la descripción ingresada pro el usuario
    Return: la descripcion validada
    """
    global descripcion_validada
    """
    patron = r"^(?=.*[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ])(?=.*\d)[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\d\s#%\-()\[\].,]+$"
    if not nueva_descripcion or not nueva_descripcion.strip() or not re.match(patron, nueva_descripcion) or len(nueva_descripcion) < 10:
    """
        # Este patrón incluye la verificación de varias condiciones.
    # Usa lookaheads para verificar condiciones sin consumirlas.
    # (?=.*[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]): Asegura la presencia de al menos una letra.
    # (?!^[\s\W_]+$): Niega si la cadena solo contiene espacios o caracteres especiales.
    # (?!^\d+$): Niega si la cadena solo contiene números.
    # .{5,}: Asegura que la cadena tiene al menos 5 caracteres.
    patron = re.compile(r'^(?=.*[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ])(?!^[\s\W_]+$)(?!^\d+$).{5,}$')
    while not(patron.match( nueva_descripcion)):   
        print("  ❌ Ingreso inválido.")
        nueva_descripcion =  input("Introduce descripción válida : ").strip().lower()
        if nueva_descripcion == "":
            break
    print("✅ Descripción válida.")
    descripcion_validada = nueva_descripcion
    # Retorno el nombre validado
    return descripcion_validada

# este funionaba pero debias volver a pedir el stock por 
# la primera linea despies del while

def validar_nuevo_stock(venta):

    """
    
    Pide al usuario que ingrese un stock válido.
    Valida que sea un número entero positivo.
    Si no es válido, vuelve a pedir ingreso hasta que lo sea.
    Devuelve el número validado como int.
    """

    while True:
        nuevo_stock = input("Ingrese stock vendido: ").strip()

        # Validar que sea un número entero con regex
        patron = re.compile(r'^\d+$')  # solo dígitos positivos
        if patron.match(venta):
            try:
                stock_vendido = int(venta)
                if stock_vendido < 0:
                    print("❌ Error: el stock no puede ser negativo.")
                    continue
                #if 1 <= stock <= 10:
                 #   print("⚠️ Stock Bajo")
                print("✅ Stock Ingresado.")
                return stock_vendido
            except ValueError:
                print("❌ Error: dato ingresado inválido.")
        else:
            print("❌ Error: Ingreso inválido. Por favor, ingrese solo números enteros.")

# probar
# valida sin dar alertas proque en cisrtos casos como en ventas no lo necesito 

def validar_nuevo_stock_vendido(valor):
    try:
        n = int(str(valor).strip())
        if n <= 0:
            print("❌ La cantidad vendida debe ser mayor a 0.")
            return None
        return n
    except ValueError:
        print("❌ Ingreso inválido. Solo números enteros.")
        return None
    
    
#probar
    
def validar_stock_vendido(valor):
    try:
        n = int(str(valor).strip())
        if n <= 0:
            print("❌ La cantidad vendida debe ser mayor a 0.")
            return None
        return n
    except ValueError:
        print("❌ Ingreso inválido. Solo números enteros.")
        return None
