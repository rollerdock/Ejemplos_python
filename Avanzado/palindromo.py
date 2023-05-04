


#Un palindromo es una palabra ofrase que se escribe igual de delante para atras que de atras para delante.

# Abba
# Reconocer
# Amo la paloma


a = "Amo la paloma"


def ComPalindromo(a):

    b = a
    a = a.replace(" ","")    
    a = a[::-1]
    a = a.lower() 
    
    b = b.replace(" ","")
    b = b.lower() 
    
    if b == a:
        print("Es un palindromo")
    else:
        print("No es un palindromo")
        
        



ComPalindromo(a)

#print(es)



