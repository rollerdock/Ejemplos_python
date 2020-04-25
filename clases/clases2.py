
class Galleta():
    chocolate = False

    def __init__(self):
        print("se acaba de crear una galleta")


    def chocolatear(self):
        self.chocolate = True

    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta de choco")
        else:
            print("No tengo chocolate")

g= Galleta()
g.chocolatear()
g.tiene_chocolate()


