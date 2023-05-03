from io import open
import os
import shutil
import pathlib
"""
######################## EJEMPLO DE COPYFILE ######################################################

ruta_original = str(pathlib.Path().absolute()) + "/Avanzado/FICHEROS/fichero-texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/Avanzado/FICHEROS/fichero-texto1.txt"
shutil.copyfile(ruta_original,ruta_nueva)

"""
#ruta_original= "C:/Users/jaspl/git/Ejemplos_python/Avanzado/fichero-texto_nuevo.txt"
#ruta_original = str(pathlib.Path().absolute()) + "/Avanzado/fichero-texto_nuevo.txt"
#ruta_nueva = str(pathlib.Path().absolute()) + "/Avanzado/FICHEROS/fichero-texto1.txt"

#shutil.move(ruta_original, ruta_nueva)

#print(ruta_nueva)
#print(ruta_original)
########################################EJEMPLO DE BORRADO #############################################

# os.remove (ruta_nueva)

############################################# EJEMPLO DE COMO SACAR RUTA ABSOLUTA #######################
print(os.path.abspath("./"))

############################################ COMPROBAR SI UN FICHERO EXISTE ####################################
ruta_nueva = str(pathlib.Path().absolute()) + "/Avanzado/FICHEROS/fichero-texto1.txt"
if os.path.isfile(ruta_nueva):
    print("Existe el archivo.")
    