#1 cear app.py
#2importar numpy como np
import numpy as np
# #3 imprimir version numpy
# print(np.__version__)
# #4 hacer una matriz de 10 nula
# matrizcero=(np.zeros(10))
# print(matrizcero)
# #5 array memory size
# memotamaño= matrizcero.itemsize * matrizcero.size
# print(memotamaño)
# #6 imprime info sobre add() con funcion np.info()
# print(np.info(np.add))
# #7 cambiar quinto elemento por 1
# matrizcero [4]=1
# print(matrizcero)
# #8 crear vector con rango de valores #el rango termina un valor antes, asi que tiene que ser un numero superior en una unidad
# x=np.arange(10,50)
# print(x)
#9 crea vector con num entre 0 y 9 y haz reverse
# aros=np.arange(0,10)
# sora= aros[::-1]
# print(sora)
#10 crea matriz 3x3 con valores entre 0 y 8 e imprimelo
# mates=np.array ([0, 1, 2, 3, 4, 5, 6, 7, 8])
# mat3=mates.reshape((3,3))
# print(mat3)
#11 indica las posiciones de los numeros que no son 0 en el siguiente array:  #si pongo arr=np.nonzero(np.array([1,2,0,0,4,0])) e imprimo, me sale igual
# arr=np.array([1,2,0,0,4,0])
# indice=np.nonzero(arr)
# print(indice)
#12 crea matriz identidad 3x3 e imprimelo
# plaf=np.eye(3)
# print(plaf)
#13 crea una variable llamada arr cuyo valor debe ser una matriz con 3 valores aleatorios
# arr=np.random.random(3)
# print(arr)
#14 crea variable arr que tenga 10 valores aleatorios e imprima el valor maximo
# arr=np.random.random(10)
# print(arr)
# print(np.max(arr))
#15 variable arr con 10 num aleatorios y haz el valor medio(media)
# arr=np.random.random(10)
# print(arr)
# print(np.mean(arr))
#16 crea matriz con todos los valores = 1 y cambia el centro por todo 0 e imprime
# matoz=np.ones((5,5))
# matoz[1:-1,1:-1]=0
# print(matoz)
#17 crea matriz con todos los valores = 1 y cambia los bordes por todo 0 e imprime
# plisu=np.ones((5,5))
# bordea = np.pad(plisu, pad_width=1, mode='constant', constant_values=0)
# print(bordea)
#18 comprueba código dado (hay que imprimir algo)
# 0 * np.nan
# np.nan == np.nan
# np.inf > np.nan
# np.nan - np.nan
# np.nan in set([np.nan])
#0.3 == 3 * 0.1
#19 crea matriz 3x3 con valores entre 0 y 8 e imprime la diagonal
# mat=np.array ([0, 1, 2, 3, 4, 5, 6, 7, 8])
# mat3=mat.reshape((3,3))
# print(mat3)
# digon=np.diag(mat3)
# print(digon)
#20 crea una matriz 8x8 y rellena con un patron de tablero ajedrez
bic=np.zeros((8,8))
# bic[::2,::2] = 1
# bic[1::2,1::2]=1
bic[::2, ::2] = bic[1::2, 1::2] = 1
print(bic)