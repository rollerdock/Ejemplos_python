# Vamos a crear una calculadora

class calculadora():

    Num1 = 0
    Num2 = 0
    
    def sumar(self):
        print ("El resultado es : ",self.Num1+self.Num2)
    def restar(self):
        print ("El resultado es : ",self.Num1-self.Num2)
    def multiplicar(self):
        print ("El resultado es : ",self.Num1*self.Num2)
    def dividir(self):
        print ("El resultado es : ",self.Num1/self.Num2)

    def arranca(self):
        print ("Esto es una calculadora super básica \n Empecemos! ")
        self.Num1 = int(input("Introduce el primer numero: "))

        sel = input (" Que operación quieres realizar:\n sumar '+' \n Restar '-' \n Multiplicar '*' \n Dividir '/' \n selección : ")
        self.Num2 = int(input("Introduce el segundo numero: "))

        if sel == "+":
            p.sumar()
        elif sel == "-": 
            p.restar()   
        elif sel == "*":
            p.multiplicar()
        elif sel == "/":
            p.dividir()

p = calculadora()
p.arranca()





