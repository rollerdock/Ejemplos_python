
class Coche:
    # Atributos o propiedades (variables)
    # caracteristicas del coche de la clase padre
    ruedas = 4
    volante = 1
    
    def __init__ (self,color,plazas,cv,vel,marca,modelo):
        self.color = color
        self.plazas = plazas
        self.cv = cv
        self.vel = vel
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        self.vel += 1 

    def getVelocidad(self):
        return self.vel


# # Métodos de clase , son acciones que hace la clase padre

# @classmethod

# def acelerar(cls):
#     self.velocidad += 1

# def frenar(cls):
#     self.velocidad -= 1



# # metodos de instancia

# def getColor(self):
#     print(coche.color)




# # Crear objetos

coche1 = Coche("rojo","2",300,350,"Lamborgini","Diablo")

print(f"El coche es de la marca {coche1.marca} y modelo {coche1.modelo} \n")
print(f"Es de color {coche1.color}\n")
print(f"Tiene {coche1.ruedas} y {coche1.volante} volante\n")

coche1.acelerar()
coche1.acelerar()
coche1.acelerar()

print(coche1.getVelocidad())