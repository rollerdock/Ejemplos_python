###############################################################################################
print("######################## Comprensión de listas ######################################")

# usuarios = [[4,"Chanchito"],[1,"felipe"],[5,"Pulga"]]
# usuarios.sort(key=lambda el: el[0],reverse=False)
# print(usuarios)
# nombre = []
# # for usuario in usuarios:
# #         nombre.append(usuario[1])
# # print(nombre)
# nombres=[]
# nombres = [usuario[1] for usuario in usuarios]
# print(nombres)

usuarios = [[4,"Chanchito"],[1,"felipe"],[5,"Pulga"]]
nombres2 = []
#nombres2 = [expresion for item (que estamos iterando) in items (la lista ) ]
nombres2 = [usuario for usuario in usuarios if (usuario[0] > 2)]

# Ojo porque como a la expresión if (usuario[0] > 2)] le pases usuario[1] al ser un "chart" te dará error.
print(nombres2)
nombres2 = [usuario[1] for usuario in usuarios if (usuario[0] > 2)]
print("##################################################################")

print(nombres2)

print(" ##################### Ejemplos con map y filter #########################")

print("########################## Función map ###################################")

nombres3=[]

nombres3 = list(map(lambda usuario: usuario[1],usuarios))

print(nombres3)

print("######################## función filter #########################################")

nombres4 = []
nombres4 = list(filter(lambda usuario: usuario[0]>2,usuarios))
print(nombres4)