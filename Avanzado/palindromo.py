import dataclasses


#Un palindromo es una palabra ofrase que se escribe igual de delante para atras que de atras para delante.

# Abba
# Reconocer
# Amo la paloma


pa = "Amo la paloma"
a= pa.lower()

def ComPalindromo(a):
    longitud = len(a)
    cadena = ""
    while longitud>0:
        cadena = cadena + a[longitud-1]
        longitud -= 1
    a = a.replace(" ","")    
    texto = cadena.replace(" ","")
    if texto == a:
        print("Es un palindromo")
    else:
        print("No es un palindromo")
        
        



ComPalindromo(a)

#print(es)



