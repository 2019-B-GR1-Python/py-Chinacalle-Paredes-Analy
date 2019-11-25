import numpy as np
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
import random

matriz = []
matriz_original = []

def matriz_inicial(arr3, arr4, arr5, arr6):
    fig, axs = plt.subplots(2,2)
    axs[0,0].imshow(arr3)
    axs[0,1].imshow(arr4)
    axs[1,0].imshow(arr5)
    axs[1,1].imshow(arr6)
    matriz.append(arr3)
    matriz.append(arr4)
    matriz.append(arr5)
    matriz.append(arr6)

    matriz_original = matriz

def iniciar():
    mapache = misc.face()
    arr1, arr2 = np.vsplit(mapache, 2)
    arr3, arr4 = np.hsplit(arr1,2)
    arr5, arr6 = np.hsplit(arr2,2)
    matriz_inicial(arr3, arr4, arr5, arr6)
    


def mezclar():
    random.shuffle(matriz)
    return matriz

def mostrar_imagen():
    fig, axs = plt.subplots(2,2)
    (axs[0,0].imshow(matriz[0]))
    (axs[0,1].imshow(matriz[1]))
    (axs[1,0].imshow(matriz[2]))
    (axs[1,1].imshow(matriz[3]))

    plt.show()
    
def mover_piezas():
    movimiento = input()
    indice1, indice2 = movimiento.split(",")
    auxiliar_matriz = matriz[int(indice1)-1]
    matriz[int(indice1)-1] = matriz[int(indice2)-1]
    matriz[int(indice2)-1] = auxiliar_matriz
    mostrar_imagen()
    return matriz

def juego():
    iniciar()
    mostrar_imagen()
    mezclar()
    while matriz != matriz_original:
        mover_piezas()
