#declaracion de una lista
lista = [2,4,6,8,10,12]

print("-------------------------")

#declaracion de una lista con diferente tipos de datos
print("declaracion de una lista con diferente tipos de datos")
lista2 = ["dos",4,"seis",8,"diez",12]

print("-------------------------")

print ("declaracion de una lista")
print (lista)    
print (lista2)

print("-------------------------")

#acceder alugar determinado de una lista (lista[3])
print("acceder alugar determinado de una lista (lista[3]")
print((lista)[3])
print((lista)[0])

print("-------------------------")

#agregar nuevo elemento a una lista
print("agregar nuevo elemento a una lista")
lista3 = ["dos",4,"seis",8]
lista3.append("NUEVO MUNDO")
print (lista3)

print("-------------------------")

#agregar lista a lista existente
print("agregar lista a lista existente")
lista4 = ["dos",4,"seis",8,"nuevo mundo"]
lista4.extend([2,4])
print (lista4)

print("-------------------------")

#insertar valor a posicion determinada
print("insertar valor a posicion determinada")
lista5 = ["dos",4,"seis",8,"nuevo mundo"]
lista4.insert(3,"nuevo valor")
print (lista5)

print("-------------------------")

#eliminar valor de una posicion 
print("eliminar valor de una posicion ")
lista6 = ["dos",4,"seis",8,"nuevo mundo"]
#del lista6[:2]elimina posiciones seleccionados de la lista
del lista6[1]
print (lista6)

print("-------------------------")

#eliminar una coincidencia
print("eliminar una coincidencia ")
lista7 = ["dos",4,"seis",8,"nuevo mundo"]
lista7.remove("nuevo mundo")
print (lista7)

print("-------------------------")

#invertir orden de lista
print("invertir orden de lista ")
lista8 = [1,2,3,4,5,6,7,8,9]
lista8.reverse()
print (lista8)

print("-------------------------")

#organizar lista de menor   a mayor
print("organizar lista de menor  a mayor ")
lista9 = [1,5,3,6,4,9,2,7,10,8]
lista9.sort()
print (lista9)

print("-------------------------")

#sacar valor minimo de una lista
print("sacar valor minimo de una lista ")
lista10 = [1,5,3,6,4,9,2,7,10,8]
print (min(lista10))

print("-------------------------")

#sacar valor maximo de una lista
print("sacar valor maximo de una lista ")
lista11 = [1,5,3,6,4,9,2,7,10,8]
print (max(lista11))