try:
    nombre = input ("¿Cual es tu nombre?: ")
    
    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre
        
    print(nombre_usuario)
except:
    print("Algo ha fallado")
else:
    print("todo ha ido correctamente")
finally:
    
    print("Fin de la iteración")
    