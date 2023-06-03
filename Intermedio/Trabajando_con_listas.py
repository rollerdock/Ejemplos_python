


cantantes = ["david bisbal","sergio dalma","fito"]

# Añadir elementos al final#
cantantes.append("atos y waor")

print("anadir al final : " + str(cantantes))

# Añadir elementos en posición especifica#
cantantes.insert(1,"shakira")
print("anadir al en posición determinada  : " + str(cantantes))


# Borrar en una posición especifica
cantantes.pop(1)
print("Borrar en posición determinada  : " + str(cantantes))


#Borra exactamente un valor , ojo tiene que ponerse exactamente!
cantantes.remove('atos y waor')
print("Borrar el elemento atos y waor  : " + str(cantantes))

#Invierte el orden
cantantes.reverse()
print ("invierte el orden : " + str(cantantes))

#busca dentro de la lista con el in, se puede hacer con un if y un true o imprimiendo
print("Busca drake dentro de la lista y devuelve boleano : " + str(('drake' in cantantes)) )
# si devuelve True es que está el elemnto y si devuelve false es que no está

# Cuenta elementos

print("cuenta elementos: " + str(len(cantantes)))

# Saber cuanta veces aparece el elemneto en la lista


cantantes.insert(0,"atos y waor")
cantantes.insert(4,"atos y waor")

print ("Cuentas cuantas veces aparece atos y waor : " + str((cantantes.count("atos y waor"))))

print(cantantes)


# Para unir listas usamos el metodo extend

viejos_cantantes = ["manolo escobar","Marisol","El Fari"]

cantantes.extend(viejos_cantantes)

print(cantantes)

