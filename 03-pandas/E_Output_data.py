# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:54:01 2019

@author: Estudiante
"""

import pandas as pd
import numpy as np
import os
import sqlite3
import xlsxwriter


path_guardado_bin = 'C://Users//Estudiante//Documents//GitHub//py-chinacalle-paredes-analy//03-pandas//data//artwork_data_completo.pickle'
df5 = pd.read_pickle(path_guardado_bin)
df = df5.iloc[49980:50519,:].copy()
#  Tipos archivos
#  JSON
#  EXCEL
#  SQL

### EXCEL ##
path_guardado = 'C://Users//Estudiante//Documents//GitHub//py-chinacalle-paredes-analy//03-pandas//data//df_completo.xlsx'
df.to_excel(path_guardado)
df.to_excel(path_guardado, index=False)
columnas = ['artist','title','year']
df.to_excel(path_guardado, columns=columnas)

### Multiples hojas de trabajo ###

path_multiple = 'C://Users//Estudiante//Documents//GitHub//py-chinacalle-paredes-analy//03-pandas//data//df_multiple.xlsx'
writer = pd.ExcelWriter(path_multiple,
                        engine='xlsxwriter')

df.to_excel(writer, sheet_name = 'Primera')

df.to_excel(writer, sheet_name = 'Segunda',
            index=False)

df.to_excel(writer, sheet_name = 'Tercera',
            columns=columnas)

writer.save()


### Multiples hojas de trabajo ###

num_artistas = df['artist'].value_counts()
path_colores = 'C://Users//Estudiante//Documents//GitHub//py-chinacalle-paredes-analy//03-pandas//data//df_colores.xlsx'

writer = pd.ExcelWriter(path_colores,
                        engine='xlsxwriter')

num_artistas.to_excel(writer, 
                      sheet_name='Artistas')


hoja_artistas = writer.sheets['Artistas']

rango_celdas = 'B2:B{}'.format(len(num_artistas.index) + 1)

formato_artistas = {
        "type": "2_color_scale",
        "min_value": "10",
        "min_type": "percentile",
        "max_value": "99",
        "max_type": "percentile"}

hoja_artistas.conditional_format(rango_celdas,
                                 formato_artistas)

writer.save()


workbook = xlsxwriter.Workbook('C://Users//Estudiante//Documents//GitHub//py-chinacalle-paredes-analy//03-pandas//data//grafico3.xlsx')
worksheet = workbook.add_worksheet()

# Add the worksheet data to be plotted.

data = [10, 40, 50, 20, 10, 50]
worksheet.write_column('A1', data)


datos_anios = (list(df['year'].values))
datos_anios = [anio for anio in datos_anios if str(anio) != 'nan']
num_anios = df['year'].value_counts()
worksheet.write_column('A1', datos_anios)

# Create a new chart object.
grafico = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
rango_celdas_anios = 'A1:A{}'.format(len(num_anios.index) + 1)
rango_final = "=Sheet1!"+rango_celdas_anios
grafico.add_series({'values': rango_final})

# Insert the chart into the worksheet.
worksheet.insert_chart('C1', grafico)

workbook.close()
