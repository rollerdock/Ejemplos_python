lista = [8,7,6,5,4,3,2,1,1]
def Recorrerlista (listado):
    result = " "
    for item in listado:
        result += str(item)
        result += " "
        cuenta = result.count
    return  result,cuenta
    
 
 
print(Recorrerlista(lista))

busca = input ("Que número quieres buscar: ")
cuenta = lista.count(int(busca))

print (  "hay " + str(cuenta) + " numeros " + busca )

lista.sort()

print(Recorrerlista(lista))











