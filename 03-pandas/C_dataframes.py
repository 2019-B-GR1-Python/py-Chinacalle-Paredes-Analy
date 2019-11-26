# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:42:09 2019

@author: anycielago
"""

import numpy as np
import pandas as pd

arr_pandas = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pandas)

s1 = df1[0]
s2 = df1[1]
s3 = df1[2]


serie_nueva = pd.Series([11,12])
df1[4] = serie_nueva


total_df = df1.count(axis=1)
df1[total_df[0]] = pd.Series([15,16])

df1[6] = s1 * s2

datos_fisicos_uno = pd.DataFrame(
        arr_pandas,
        columns=[
                'Estatura (cm)',
                'Peso (kg)',
                'Edad (anios)'
                ]
        )


datos_fisicos_uno['Peso (kg)']

datos_fisicos_dos = pd.DataFrame(
        arr_pandas,
        columns = [
                'Estatura (cm)',
                'Peso (kg)',
                'Edad (anios)'
                ],
        index = ['Any', 'Cielago']
        )


df1.index = ['Any', 'Cielago']

df1.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']













