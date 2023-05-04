
# Podemos usar la expresión [::-1] para invertir un string
# a = a[::-1]


a = "Volveran las oscuras golondrinas"
lista = ["Volveran","las","oscuras","palomas"]

# a = a[::-1]
# print(a)
frase_al_reves = ""
for char in a:
    frase_al_reves = char + frase_al_reves

lista.reverse()


print(frase_al_reves)
print(lista)


