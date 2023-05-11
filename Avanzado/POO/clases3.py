import subprocess
subprocess.call('clear')


class Escuela():
    def __init__(self):
        self.nombre = "Mirasan"
        self.numalumnos = 300

    def sumaalumnos(self):
        self.numalumnos = self.numalumnos + 50
        print("Hay ", self.numalumnos)

    def resta(self):
        self.numalumnos = self.numalumnos - 50

    def total(self):

        print("En total hay ", self.numalumnos)


p = Escuela()
print(p.numalumnos)
p.sumaalumnos()
print("hay: ", p.numalumnos)
p.resta()
print("hay: ", p.numalumnos)
p.sumaalumnos()
print("hay: ", p.numalumnos)
p.sumaalumnos()
print("hay: ", p.numalumnos)
