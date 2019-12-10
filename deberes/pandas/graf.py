# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
"""
Editor de Spyder

Este es un archivo temporal.
"""
datos_raw = "species.csv"
datos_df = pd.read_csv(datos_raw)
pd.read_csv()


frecuencia_tipo_animal_df = pd.crosstab(
        index=datos_df["Category"],
        columns="Animales por categoria"
        )

numero_registros = datos_df["SpeciesID"].count()
print(numero_registros)
# =============================================================================
# plt.pie(
#         frecuencia_tipo_animal_df, 
#         labels=frecuencia_tipo_animal_df.index
#         )
# =============================================================================
# =============================================================================
# plt.xlabel("Categoria")
# plt.show()
# =============================================================================

grupo_natividad = datos_df.groupby('Nativeness')
print(grupo_natividad.describe())

# print(datos_df.columns)


especies_nativas = datos_df.groupby('Nativeness')['Common Names'].count()
print(especies_nativas)

# especies_nativas.plot(kind='bar', stacked=True, title="Especies según su natividad")
# print('otro grafico')
especies_nativas.plot(kind='pie', stacked=True, title="Especies según su natividad")

print(pd.unique(datos_df["Nativeness"]))
print(datos_df["Nativeness"].isnull().sum
      ())








# PAGINAS
# https://code.likeagirl.io/an%C3%A1lisis-y-visualizaci%C3%B3n-de-datos-con-pandas-matplotlib-85ee4d7b4cad
# https://datacarpentry.org/python-ecology-lesson-es/02-starting-with-data/
# https://blog.adrianistan.eu/estadistica-python-pandas-numpy-scipy-parte-i
