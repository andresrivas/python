#string son cadena de caracteres
# type define o muestra el tipo de dato
# dir imprime todo lo que tiene la variable
nombre = "Juan"
apellido = "Cardenas"
print(type(nombre))
print (dir (nombre))
#concatenacion de cadenas
print (nombre + apellido)

#multiplicacion de cadenas
print(nombre*3)

#obtener tamaño de cadena
print(len(nombre))
print(len(apellido))
print(len(nombre + apellido))

#acceder a una posicion determinada
print(nombre[3])

#convertir todo a minusculas
print(nombre.lower())

#convertir todo a mayusculas
print(nombre.upper())