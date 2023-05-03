matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filas=len(matriz)
Columnas=len(matriz[0])

for filas in matriz:
    print(matriz[filas][Columnas])
    
    for Columnas in matriz:
        print(matriz[filas][Columnas])