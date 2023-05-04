class PC:
    def __init__(self, microprocesador, memoria, color):
        self.microprocesador = microprocesador
        self.memoria = memoria
        self.color = color

mipc = PC("i5", 16, "Negro")
mipc.color = "Azul"
mipc.memoria = 32
mipc.microprocesador = "i7"

mipc2 = PC("i5", 16, "Rojo")
mipc2.color = "Rojo"
mipc2.memoria = 16
mipc2.microprocesador = "i3"

@classmethod
def arranca(cls):
    print("El PC acaba de encender y es de color:", cls.color)

print(mipc.color, mipc.memoria, mipc.microprocesador)
print(mipc2.color, mipc2.memoria, mipc2.microprocesador)
