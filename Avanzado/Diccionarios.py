
# es obligatorio que el primer elemento sea un string
punto = {"x": 25, "y": 50}

# para referirnos a in elemento del diccionario :

print(punto["x"])

punto["z"] = 45  # Así añadimos un elemento al diccionario.

print(punto)

# la manera más correcta de devolver un valor de un diccionario es con get

print(punto.get("x"))

# si 66 no está devolverá "no existe" que es el valor por defecto
print(punto.get("66", "No existe"))
print(punto)

for valor in punto:
    print(valor, punto[valor])
