
lista = [1,2,3,4,5,6,7,8,9,10,11,12]

try:
    numero = int(input("Introduce el numero a buscar: "))
    def Numesta(numero):
        while int(numero) not in lista:
            numero = input("Introduce el numero a buscar: ")
    
        if int(numero) in lista:
            print("El numero está!")
            
        else:
            numero = int(input("No está en la lista,Introduce un valor valido: "))
except:
    numero = input ("Hay un error, introduce un valor valido:  ")
    Numesta(numero)
else:
    print(f"El numero {numero} no esta es la lista")
    Numesta(numero)
finally:
    print("Sin errores")

