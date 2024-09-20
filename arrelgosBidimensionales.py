# Ejercicios arreglos bidimensionales


import numpy as np

a_random = np.random.randint(0,100, size=(3,3))
print (a_random)

# Promedio elementos
print("Promedio elementos: ")
promedio = np.mean(a_random)
print (promedio)

# suma elementos
print("Suma elementos: ")
suma = np.sum(a_random)
print(suma)

# Elemento mayor 
print("Elemento mayor del arreglo: ")
mayor = np.max(a_random)
print(mayor)

# Elemento menor
print("Elemento mayor del arreglo: ")
menor = np.min(a_random)
print(menor)

## Diagonal
print("Elementos de la diagonal principal: ")
diagonal = np.diag(a_random)
print(diagonal)