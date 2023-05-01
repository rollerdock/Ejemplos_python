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

print (  f"hay  {cuenta}  numeros {busca} ")

lista.sort()

print(f"{Recorrerlista(lista)}")

print(f"la lista tiene {len(lista)}  numeros")











