from io import open
import pathlib
"""
#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/Avanzado/FICHEROS/fichero-texto.txt"

archivo = open(ruta,"a+")

# escribir dentro del archivo

archivo.write("*********** Soy un texto guay ************ \n ")

#cerrar archivo

archivo.close()
"""


#Abrir archivo

ruta = str(pathlib.Path().absolute()) + "/Avanzado/FICHEROS/fichero-texto.txt"

archivo_lectura = open(ruta,"r")

# Leer contenido 

"""
contenido = archivo_lectura.read()


for elemento in archivo_lectura:
    #print(contenido)
    
    # Leer contenido y grardarlo en lista 
    
    lista = archivo_lectura.readline()
    
    # print(lista)

"""
lista = archivo_lectura.readlines()

for frase in lista:
    print("- " + frase)
    
    
archivo_lectura.close()    

