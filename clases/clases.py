class Persona:
    def __init__(self): 
        
        print ("Creo un objeto")

    

    def caracteristicas(self,otro):
        
        self.otro = 103
        print("Has pasado caracteristicas",self.otro,otro)
        
print("fuera de la clase")



p=Persona()
p.caracteristicas(100)