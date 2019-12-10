# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
"""
Created on Sun Dec  8 21:42:35 2019

@author: DELL
"""


datos_raw = "C://Users//DELL//Documents//Analy//py-chinacalle-paredes-analy//deberes//pandas//siniestrosRAW.xlsx"

#columnas = ['CAUSA',	'Total',	'Enero',
#            'Febrero',	'Marzo',	'Abril',	'Mayo',	'Junio',	
#            'Julio',	'Agosto',	'Septiembre',	'Octubre',	'Noviembre',	'Diciembre']

columnas = "A:N"
#indices = ['TOTAL', 'ATROPELLOS', 'CAÍDA DE PASAJEROS', 'CHOQUES', 'ESTRELLAMIENTOS', 'ROZAMIENTOS',
#'VOLCAMIENTOS', 'PÉRDIDA DE PISTA', 'OTROS']
indices = [0]
siniestros_causa_df = pd.read_excel(
        datos_raw, 
        sheet_name="SiniestrosCausa", 
 #       usecols=columnas,
        keep_default_na = False,
        index_col= indices
        )

siniestros_provincias_df = pd.read_excel(
        datos_raw, 
        sheet_name="SiniestrosProvincias", 
 #       usecols=columnas,
        keep_default_na = False,
        index_col= indices
        )

siniestros_causa_df['Enero']
siniestros_causa_df_usar = siniestros_causa_df.transpose()

 print(siniestros_provincias_df.columns)
 
 aux = 'asd sa'
 aux = aux.upper()

siniestros_provincias_df.rename(
        columns= lambda item: item.upper(),
        inplace= True
        )

siniestros_provincias_df.columns.map(mayuscular)
siniestros_provincias_df['EMBRIAGUEZ O DROGA']
def mayuscular(elemento):
    return elemento.upper()


# NO USAR ASI
frecuencia_accidentes_df = pd.crosstab(
        index=siniestros_causa_df['Enero'],
        columns=siniestros_causa_df['Febrero']
        )

numero_registros = siniestros_df["CLASE DE ACCIDENTE"].count()
print(numero_registros)

grupo_accidente = siniestros_df2.groupby(1)
print(grupo_accidente.describe())

# print(datos_df.columns)


especies_nativas = siniestros_df2.groupby('ATROPELLOS')['CLASE DE ACCIDENTE'].count()
print(especies_nativas)

especies_nativas.plot(kind='bar', stacked=True, title="Siniestros por atropellos")

siniestros_df.describe()
siniestros_df2.describe()

siniestros_df.plot(kind='bar', stacked=True, title="Siniestros por Clase", subplots=True)

