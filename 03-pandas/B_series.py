# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

serie_a = pd.Series(lista_numeros)
serie_b = pd.Series(tupla_numeros)
serie_c = pd.Series(np_numeros)

serie_d = pd.Series([
        True,
        False,
        12,
        12.12,
        "Analy",
        None,
        (),
        [],
        {"nombre": "Analy"}
        ])

serie_d[3]

lista_ciudades = [
        "Ambato", 
        "Cuenca",
        "Loja",
        "Quito"
                  ]

serie_ciudad = pd.Series(
        lista_ciudades,
        index=[
                "A",
                "C",
                "L",
                "Q",
                ]
        )

serie_ciudad["Q"]
serie_ciudad[3]


valores_ciudad = {
        "Ibarra": 1234,
        "Guayaquil": 12,
        "Cuenca": 2344,
        "Quito": 5445,
        "Loja": 4564.
        }


serie_valor_ciudad = pd.Series(valores_ciudad)




serie_valor_ciudad['Ibarra']

serie_valor_ciudad[0]


ciudades_menores_5000 = serie_valor_ciudad < 5000

serie_5 = serie_valor_ciudad[ciudades_menores_5000]

serie_valor_ciudad = serie_valor_ciudad * 1.10

serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"] - 50

"Lima" in serie_valor_ciudad
"Loja" in serie_valor_ciudad

rsquare = np.square(serie_valor_ciudad)

rsen = np.sin(serie_valor_ciudad)

ciudades_uno = pd.Series({
        "Montañita": 300,
        "Guayaquil": 10000,
        "Quito": 2000
        })

ciudades_dos = pd.Series({
        "Loja": 300,
        "Guayaquil": 10000,
        })

ciudades_uno["Loja"] = 0
presupuesto = ciudades_uno + ciudades_dos

def existe_llave(key, arreglo):
    return key in arreglo
  
for key in ciudades_uno.keys():
    if existe_llave(key, ciudades_dos):
        continue
    else:
        ciudades_dos[key] = 0      

for key in ciudades_dos.keys():
    if existe_llave(key, ciudades_uno):
        continue
    else:
        ciudades_uno[key] = 0   
        
algo = ciudades_dos.keys()
algo

ciudad_add = ciudades_uno.add(ciudades_dos)
ciudades_concatenadas = pd.concat([
        ciudades_uno,
        ciudades_dos
        ])
    

ciudades_concatenadas = pd.concat([
        ciudades_uno,
        ciudades_dos
        ], verify_integrity = True)


ciud_append = ciudades_uno.append(
        ciudades_dos,
        verify_integrity = True
        )

ciudades_uno.max()
pd.Series.max(ciudades_uno)
np.max(ciudades_uno)


ciudades_uno.min()
pd.Series.min(ciudades_uno)
np.min(ciudades_uno)

# Estadística
ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)

ciudades_uno.head(2)
ciudades_uno.tail(2)

ciudades_uno.sort_values().head(2)
ciudades_uno.sort_values(ascending=False).head(2)
ciudades_uno.sort_values().tail(2)