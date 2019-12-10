# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
"""
Created on Tue Dec 10 07:19:43 2019

@author: USRBET
"""

### 2) Crear un vector de ceros de tamaño 10
arreglo_ceros = np.zeros(10)

### 3) Crear un vector de ceros de tamaño 10 y el de la posicion 5 sea igual a 1
arreglo_ceros_cinco = arreglo_ceros
arreglo_ceros_cinco[5] = 1

# 4) Cambiar el orden de un vector de 50 elementos, el de la posicion 1 es el de la 50 etc.
arreglo_cincuenta = np.arange(50)
arreglo_cincuenta = arreglo_cincuenta[::-1]


# 5) Crear una matriz de 3 x 3 con valores del cero al 8
arreglo_9 = np.arange(9)
matriz_3_3 = arreglo_9.reshape(3,3)

# 6) Encontrar los indices que no sean cero en un arreglo
arreglo = [1,2,0,0,4,0]
arreglo = np.array(arreglo)
respuesta = (arreglo > 0)

arreglo_indices_sin_cero = arreglo[respuesta]

# 7) Crear una matriz de identidad 3 x 3
matriz_identidad = np.eye(3,3)

#8) Crear una matriz 3 x 3 x 3 con valores randomicos
matriz_random = np.random.rand(3,3,3)

# 9) Crear una matriz 10 x 10 y encontrar el mayor y el menor
matriz_10_10 = np.random.rand(10,10)*10

np.max(matriz_10_10)
np.min(matriz_10_10)

# 10) Sacar los colores RGB unicos en una imagen (cuales rgb existen ej: 0, 0, 0 - 255,255,255 -> 2 colores)



#11) ¿Como crear una serie de una lista, diccionario o arreglo?

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

serie_lista = pd.Series(mylist)
serie_arreglo = pd.Series(myarr)
serie_dict = pd.Series(mydict)

# 12) ¿Como convertir el indice de una serie en una columna de un DataFrame?
#mylist = list('abcedfghijklmnopqrstuvwxyz')
#myarr = np.arange(26)
#mydict = dict(zip(mylist, myarr))
#ser = pd.Series(mydict) 
# Transformar la serie en dataframe y hacer una columna indice
serie_dict.index
df1 = pd.DataFrame(serie_dict.index)


# 13) ¿Como combinar varias series para hacer un DataFrame?
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df13 = pd.DataFrame([ser1, ser2])

# 14) ¿Como obtener los items que esten en una serie A y no en una serie B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

serie_a_no_b = ser1.append(
        ser2,
        verify_integrity= True,
        ignore_index= True
        )

if 1 not in ser2.values:
        print('asd')

def items_no_repetidos(valor):
    items = []
    if valor not in ser2.values:
        items.append(valor)
    return items

serie_a_no_b = ser1.map(items_no_repetidos)


#15) ¿Como obtener los items que no son comunes en una serie A y serie B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])


def items_no_repetidos_2_series(serie1, serie2):
    items = []
    for valor in serie1.values:
        if valor not in serie2.values:
            items.append(valor)
    for valor in serie2.values:
        if valor not in serie1.values:
            items.append(valor)
    return items

respuesta_no_comunes = items_no_repetidos_2_series(ser1, ser2)


#16) ¿Como obtener el numero de veces que se repite un valor en una serie?
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
repite_valor_16 = ser.value_counts()
repite_valor_16


#17) ¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
repite_valor_17 = ser.value_counts()
type(repite_valor_17.keys())
respuesta = repite_valor_17.keys()[0:2]

#for i in (0,(len(ser.values)-1)):
#    print(ser.values[i])
#    if ser.values[i] in respuesta:
#        print(ser.values[i])
#        
#for value in ser.values:
#    if value not in respuesta:
#        ser[ser.index.isin([value])]

respuesta_17 = ser.index.isin(respuesta)

ser[respuesta_17] = 0

#20) ¿Como anadir series vertical u horizontalmente a un DataFrame?
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))


df20 = pd.DataFrame([ser1,ser2])
df20_1 = pd.DataFrame(ser1)


#21)¿Obtener la media de una serie agrupada por otra serie?
# groupby tambien esta disponible en series.
ser1 = pd.Series(range(5))
ser2 = pd.Series(range(5))

resultado = ser1.groupby(['0'])('0')
"""
18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un shape definido?
ser = pd.Series(np.random.randint(1, 10, 35))
shape(7,5)
19) ¿Obtener los valores de una serie conociendo la posicion por indice?
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u
20) ¿Como anadir series vertical u horizontalmente a un DataFrame?
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
21)¿Obtener la media de una serie agrupada por otra serie?
groupby tambien esta disponible en series.

frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.tolist())
print(frutas.tolist())
#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']

# Los valores van a cambiar por ser random
# apple     6.0
# banana    4.0
# carrot    5.8
# dtype: float64

22)¿Como importar solo columnas especificas de un archivo csv?
https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv.
"""