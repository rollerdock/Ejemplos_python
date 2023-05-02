import datetime

dt= datetime.datetime.now()
print(dt)

# Crear una fecha usando la clase date
fecha = datetime.date(2023, 5, 2)
print(fecha)  # 2023-05-02

# Obtener la fecha actual
fecha_actual = datetime.date.today()
print(fecha_actual)  # Ejemplo de salida: 2023-05-02

# Crear una hora usando la clase time
hora = datetime.time(10, 30, 0)
print(hora)  # 10:30:00

# Crear una fecha y hora usando la clase datetime
fecha_hora = datetime.datetime(2023, 5, 2, 10, 30, 0)
print(fecha_hora)  # 2023-05-02 10:30:00

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.datetime.now()
print(fecha_hora_actual)  # Ejemplo de salida: 2023-05-02 11:00:00.123456

# Realizar operaciones con fechas y horas
fecha2 = datetime.date(2023, 5, 5)
diferencia = fecha2 - fecha
print(diferencia.days)  # 3


fecha = datetime.datetime.now()

# Formatear la fecha en el formato "dd/mm/yyyy"
fecha_formateada = fecha.strftime('%d/%m/%Y')
print(fecha_formateada)  # 02/05/2023