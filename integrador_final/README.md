# Marcela, Alejandra Brahim, DNI 20010395 mar.ale.bra@gmail.com
README
📦 CRUD de Inventario en Python con SQLite3
📝 Descripción

Este proyecto implementa un sistema CRUD para gestionar un inventario de productos 

utilizando Python y SQLite. Incluye las siguientes funcionalidades:

Productos: creación, búsqueda, modificación, listado y eliminación por nombre o ID. Una observación: conversando del proyecto con conocidos, me dijeron que al ser ajenos al mundi IT, no se ubicaban con ID sino con Código, por eso utilizo los dos.

Ademas tiene una Tablas Ventas: registro de ventas con cantidad, monto total y fecha.

Historial de Productos Agregados: que es un diccionario que guarda cada alta con 

fecha de manera temporral y detalles.

Historial de productos eliminados: tabla que guarda cada baja de productos consus 

datos y con fecha.

Reportes: stock bajo, rango de precios, resumen general del inventario.

La idea es unificarlo con una sector principal en el cuál se dé a eligir al cliente 

entre las secciones: 
    
Inventario (este CRUD), Servicios ( en proceso),  Clientes ( realizado). 

Cada usuario ingresaría con su contraseña. 

Este trabajo se basa en plantas como productos, servicios pensé entre otras 

actividades: mantenimiento, paisajismo, asesoramiento, promociones. Clientes: CRUD y 

base de datos donde se guardan nombre apellido, telefono, direccion, mail, dni con su 

respectivo CRUD (Create, Update, delete, Read, Busquedas, con sus validaciones,pir 

nombre, DNI (id)...)

Por razones que me han superado (inconvenientes con servici elètrico por obra,                                
falta de servcio de telered unico prestadota de internet en donde estoy de 8 a 22 
Pablo Nogues, servicio aun restringgido por supuesta caìda de antena del Claro prestadora 
de mi telèfono mòvil, emoresas denunciadas en defensa del comnsumidor, servicios 
ya pedidos de baja) no pude implementar el material que tengo  terminado ni concluir
el codigo que esta en proceso ni ligar como lo pensaba hacer para entregar el martes pasado.
Al menos intentaré hacer esta breve, incompleta entrega.

🗂️ Tablas principales

Tabla productos
    CREATE TABLE IF NOT EXISTS productos (
            id_producto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            nombre TEXT NOT NULL UNIQUE,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL,
            categoria TEXT NOT NULL,
            descripcion TEXT NOT NULL
      );

Tabla de ventas
    
    CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto_nombre TEXT NOT NULL UNIQUE,
            cantidad INTEGER NOT NULL,
            monto_total REAL NOT NULL,
            fecha TEXT NOT NULL,
            FOREIGN KEY (producto_nombre) REFERENCES productos(nombre)
        );

Tabla de porductos eliminados

    CREATE TABLE IF NOT EXISTS productos_eliminados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL,
    categoria TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (producto_nombre) REFERENCES productos(nombre)
        );

Datos guardados temporamente a los efectos de listar Reportes

  Productos Agregados

  Bajo stock

  Codigos repetidos


 ⚙️ Funcionalidades CRUD

*Crear producto introduciedo  stock, precio,categoria y descripcion.


*Crear producto de manera rapida para lueg modificar stock, precio categorìa yódescripcion con valores por defaukt


*Búsqueda de un producy, el valor del orecio unitario, stock, descriociòn o categorìa por id/nombre.


*Listar productos, productos con su stock o precios,o categorias o descirpcion, utilizando tabulate.

*Modificar producto, o su categorìam descripcion,stock o recio.

*Eliminar producto por nombre e ID, mostrando el producto para eliinarse, y guardandolo en la tabla productos eliminados.

*Listar tabla de productos con su capital, con alertas de datos invàlidos o bajo stock y listado de prodcttos con sus datos,

****En los casos de listado de un producto con tdoos sus datos o la tabla productos con datos completos, la descripciòn al ser extensa y "romper" el formato tabulate ocupando el espacio horizaontal  implementé una función de modo truncado.

La idea es usar algún método para "clickear" sobre el texto, para que se abriera la descripción en una ventana mostrando el texto completo a los efectos de leerlo o modificarlo, pero no me dió el tiempo sin servicio de internet.


En las actividades que se se muestra un producto sólo con su descpción, y una tabla de todos los productos con sus descripciones, para que el texto de la misma no ocupe todo el espacio horizontal, procedo con una función a "envolver" el texto dentro de un determinado número de caracteres así se conserva las columnas de la tabla del listado.


📊 Reportes

Stock bajo: listar productos con cantidad menor a un umbral.

Rango de precios: filtrar productos entre valores mínimo y máximo.

Resumen general: total de productos, stock acumulado y valor total del inventario.

Historial de agregados/eliminados: consultar tablas auxiliares para auditoría.

Gráficas de productos en relación con el stock, con el precio unitario, capital total por producto, stock vendido por producto, capita total vendido por producto

▶️ Ejecución

Clonar o descargar el proyecto.

Instalar dependencias (matplotlib, regex, colorama, tabulate, datatime, numpy, pandas):

bash
pip install colorama tabulate
Ejecutar el archivo principal:

bash
python main.py

Interactuar con el menú CRUD para gestionar productos y ventas. 

Esta implementada una carga inicial para cada una de las tablas

a los efectos de que sea màs sencillo utilizar el CRUD.


** La idea era que los productos agregados,se mostraran en la tabla actualizada con un color por ejemplo verde, como los items modificados en la tabla actualizada de productos o mproducto vendido en la tabla ventas.
*** Era la intencion de que cuando se clickeara sobre la descripcion en la tabla y esta estuvieratruncada, se abriera en un prompt/ventana auxiliar a los efectos que el usuario la pudiera leer integra o modificar.
