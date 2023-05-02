
# Escribir un programa que añada valores a la lista mientras que si logitud sea menor a 120 y luego mostrar la lista .
# Hacerlo con while y con for
lista = [ ]
contador = 0
wf = input ("Elige si quieres que lo haga con while o for, escribe while o for : ")

if wf == "while" :
    print ("has elegido while")    
    while (len(lista) < 120) :
        lista.append(f"Elemento {contador} ")
        contador += 1
        
else: # bloque for

    print ("has elegido for")
    for numero in range(0,120):
        lista.append(f"Elemento {contador} ")
        contador +=1

print (lista)


