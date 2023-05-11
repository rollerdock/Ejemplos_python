

class Coche:
    # Atributos o propiedades (variables)
    # caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2


coche = Coche()
# Métodos, son acciones que hace el objeto, en (coche) (funciones)


def acelerar(self):
    self.velocidad += 1


def frenar(self):
    self.velocidad -= 1


def getVelocidad(self):
    return self.velocidad

# Fin definición clase

# Crear objetos


print(coche.marca, coche.color, coche.velocidad)


coche1.acelerar()
coche1.acelerar()

print(coche.marca, coche.color, coche.velocidad)
