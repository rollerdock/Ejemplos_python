#Crea un programa que pida dos números por teclado. El programa tendrá una función llamada “DevuelveMax” encargada de devolver el número más alto de los dos introducidos.

num1=int(input("Introduce el primer numero: "))
num2=int(input("Introduce el segundo numero: "))

def DevuelveMax(num1,num2):

    ret=int(0)

    if num1>num2:
        print(" num1 es mayor")
    
    else:
        print("num2 es mayor")

    return ret
    


retorno = DevuelveMax(num1,num2)
print(retorno)
