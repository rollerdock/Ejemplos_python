#Multiples excepciones

try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es: " + str(numero*numero))

except TypeError:
    print("Debes de convertir tus cadenas a enteros")
    
#except ValueError:
 #   print("Introduce un numero valido")
    
except Exception as e: #ponemos la excepción en una variable
    print("El error es ", type(e).__name__)
    
    
    
    