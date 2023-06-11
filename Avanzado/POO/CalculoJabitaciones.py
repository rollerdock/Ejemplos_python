import os
os.system('clear')

class Ventanas:
    def __init__ (self,nombre,altoVent,largoVent):
        self.nombre = nombre
        self.altoVent = altoVent
        self.largoVent = largoVent

# altoVent = 100
# largoVent = 120
salir = "S"
while salir == "S":

    salir = input("Deseas crear una nueva ventana ? \"S\" o \"salir\" ")
    if salir == "S":
            nombre_ventana = input("Nombre ventana: ")
            altoVent = input("Alto: ")
            largoVent = input("largo: ") 
            ventana = Ventanas(nombre_ventana,altoVent,largoVent)
            #ventana.altoVent= altoVent
            #ventana.largoVent = largoVent
            # ventana.nombre = nombre_ventana
            

    else:
        print("OK, adios")
        salir = True

def superficie (altoVent,largoVent):
    superficie = int(ventana.altoVent)*int(ventana.largoVent)
    return superficie
    
  #  superficie = ventana.altoVent * ventana*largoVent
#print(f"La ventana de {ventana.nombre} tiene {ventana.altoVent} de alto y {ventana.largoVent} de largo y una superficie de {ventana.altoVent*ventana.largoVent}")
print(f"La ventana tiene {ventana.altoVent} de alto y {ventana.largoVent} de largo y {superficie(ventana.altoVent,ventana.largoVent)} de superficie ")
