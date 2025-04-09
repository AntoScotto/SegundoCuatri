#lista vacia:
lista_vacia =[]

#lista con elementos
numeros=[1,2,3,4,5]
lista_mixta=[10,'hola', True, {1,2}] 

#agregar 
numeros.append(6)#agrega al final
numeros.insert(2,99) #posicion, numero
numeros.extend([7,11]) 

print(numeros)

#borrar
numeros.remove(99)
#numeros.pop se borra el ultimo numero de la lista.
print(numeros)