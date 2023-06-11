
global exit
exit=0
nom=" "
dni = 000000

while exit==0:

    def Tomadatos():
        global nom, dni
        nom= input("Tu nombre: ")
        dni= (input("Tu dni: "))
        return nom,dni

    def imprime(nom,dni):
        print("Tu Nombre es  " + nom + " Y tu DNI es : " + str(dni))


    Tomadatos()

    imprime(nom,dni)
    condicion = str(input("Quieres seguir ? Intro para un nuevo registro y \"exit\" para salir"))
    if condicion == str(1):
        exit = 1




