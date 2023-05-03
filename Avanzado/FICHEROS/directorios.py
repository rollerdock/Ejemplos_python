import os
import shutil

# crear carpeta
"""
if not os.path.isdir("C:/Users/jaspl/git/Ejemplos_python/Avanzado/FICHEROS/mi_carpeta"): # comprueba si existe
    os.mkdir("C:/Users/jaspl/git/Ejemplos_python/Avanzado/FICHEROS/mi_carpeta") # crea carpeta en directorio actual
    

else:
        print("Ya existe el directorio")
        
# os.rmdir("C:/Users/jaspl/git/Ejemplos_python/Avanzado/FICHEROS/mi_carpeta") # borra carpeta
ruta_original= "C:/Users/jaspl/git/Ejemplos_python/Avanzado/FICHEROS/mi_carpeta"
ruta_nueva= "C:/Users/jaspl/git/Ejemplos_python/Avanzado/FICHEROS/mi_carpeta/mi_carpeta"
if not os.path.isdir("C:/Users/jaspl/git/Ejemplos_python/Avanzado/FICHEROS/mi_carpeta/mi_carpeta"): # comprueba si existe
    #os.mkdir("C:/Users/jaspl/git/Ejemplos_python/Avanzado/FICHEROS/mi_carpeta") # crea carpeta en directorio actual
    shutil.copytree(ruta_original,ruta_nueva) # copia la carpeta en otra ruta


os.rmdir ("C:/Users/jaspl/git/Ejemplos_python/Avanzado/FICHEROS/mi_carpeta") # Borrar carpeta
"""




contenido = os.listdir("C:/Users/jaspl/Downloads")

for fichero in contenido:
    print(fichero + "\n")
    


