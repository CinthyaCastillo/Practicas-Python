# Longitud de una frase 

palabra = input("Ingrese una palabra: ") # Se define la variable palabra 
letras = []

for letra in palabra : # Se separan las letras que componen la palabra para asignarle la longitud
    letras.append(letra)

longitud = len(palabra)

if 4 <= longitud <= 8 : # Se definen las condocionales con sus respectivos resultados 
   print("La palabra es correcta.")
elif longitud <= 3 :
    print("Hacen falta letras. La palabra que ingresaste solo tiene {}.".format(longitud))
else :
    print("Sobran letras. La palabra que ingresaste tiene {} letras".format(longitud))


# Encuentra el cuadrantre

x = float(input("Ingrese una coordenada X: ")) # Se definen las variables a ingresar
y = float(input("Ingrese una coordenada Y: "))

if x > 0 and y > 0:   # Se determinan los cuadrantes en las condicioneales 
    cuadrante = "Cuadrante I"
elif x < 0 and y > 0:
    cuadrante = "Cuadrante II"
elif x < 0 and y < 0:
    cuadrante = "Cuadrante III"
elif x > 0 and y < 0:
    cuadrante = "Cuadrante IV"
elif x == 0 and y == 0:
    cuadrante = "punto origen"
else:
    cuadrante = "eje. Intenta con otra coordenada"

print(f"El punto ({x}, {y}) se encuentra en el {cuadrante}.") # Se muestra el resultado
