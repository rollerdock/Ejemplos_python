
class Coche:
    # Atributos o propiedades (variables)
    # caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2


# Métodos, son acciones que hace el objeto, en (coche) (funciones)


    def acelerar(self):
        self.vel += 1 

    def getVelocidad(self):
        return self.velocidad



# # Crear objetos

print(coche.marca, coche.color, coche.marca)

print(f"El coche es de la marca {coche1.marca} y modelo {coche1.modelo} \n")
print(f"Es de color {coche1.color}\n")
print(f"Tiene {coche1.ruedas} y {coche1.volante} volante\n")

coche.acelerar()
print(coche.marca, coche.color, coche.velocidad)

print(coche1.getVelocidad())