import numpy as np
# Nahum flores NC 0065
# Ejemplos numpy Numerical Python 
print("--- Especiado Linealmente en array --- 0065")
arre=np.linspace(start=0,stop=1,num=5)
print(arre)
print("--- Matriz identidad en 2D en array --- 0065")
matrix=np.eye(3)
print(matrix)
print("--- Genera numeros al azar(aleatorios) en 2D en array --- 0065")
numale=np.random.random((3,4)) # genera 12 numeros aleatorios
print(numale)

print("--- Genera 9 numeros aleatorios entre 0 y 1  --- 0065")
numale=np.random.random((3,3)) # genera 9 numeros aleatorios
print(numale)
# como generar 8 numeros aleatorios comprendidos entre 1 y 20
# con numpy es un arreglo de 3 por 3
print(" genera 9 numeros aleatorios entre 1 y 20")
arre = np.random.randint(1, 21, size=9).reshape(3, 3)
print(arre)
print("Nahum Flores NC 0065")