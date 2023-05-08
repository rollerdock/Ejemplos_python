import sqlite3

# Crear conexión con la base de datos
conexion = sqlite3.connect(
    'C:/Users/jaspl/PYTHON/Ejemplos_python/Avanzado/Bases_de_datos/pruebas.db')

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute(
    'CREATE TABLE IF NOT EXISTS productos(id INTEGER PRIMARY KEY AUTOINCREMENT,titulo VARCHAR(255),descripcion TEXT,precio INTEGER)')
conexion.commit()

# Insertar datos
cursor.execute(
    "INSERT INTO productos VALUES (null, 'calcetines', 'Unos calcetines muy bonitos', 12)")
conexion.commit()

# Cerrar conexión

# Leer datos de la tabla
cursor.execute('SELECT * FROM productos')
datos = cursor.fetchall()

# Imprimir los datos
for fila in datos:
    print(fila)

# Cerrar conexión
conexion.close()


# ideas paara precticar:
# rear las funciones conectar,cerrar,crear tabla, insertar en tabla, leer en tabla
