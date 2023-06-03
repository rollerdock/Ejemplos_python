
num1= int(input("Introduce el numero 1"))
num2= int(input("Introduce el numero 2"))
print("Que operación quieres realizar ? +,-,*,/")
operacion= input("operacion : ")



if operacion == "+":
    print("El resultado es: ",num1+num2)
elif operacion == "-":
    print("El resultado es: ",num1-num2)
elif operacion == "*":
    print("El resultado es: ",num1*num2)
elif operacion == "/":
    print("El resultado es: ",num1/num2)
