

usuarios = [[4,"Chanchito"],[1,"felipe"],[5,"Pulga"]]

usuarios.sort(key=lambda el: el[0],reverse=False)

print(usuarios)


# nombre = []

# # for usuario in usuarios:
# #         nombre.append(usuario[1])

# # print(nombre)
print("##################################################################")

nombres=[]
nombres = [usuario[1] for usuario in usuarios]
print(nombres)
