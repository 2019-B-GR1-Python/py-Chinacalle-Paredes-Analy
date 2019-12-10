# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
"""
Created on Sun Dec  8 18:41:00 2019

@author: DELL
"""

datos_raw = "C://Users//DELL//Documents//Analy//py-chinacalle-paredes-analy//deberes//pandas//siniestrosRAW.xlsx"

#columnas = ['CLASE DE ACCIDENTE',	'Total',	'Enero',
#            'Febrero',	'Marzo',	'Abril',	'Mayo',	'Junio',	
#            'Julio',	'Agosto',	'Septiembre',	'Octubre',	'Noviembre',	'Diciembre']

columnas = "A:N"
#indices = ['TOTAL', 'ATROPELLOS', 'CAÍDA DE PASAJEROS', 'CHOQUES', 'ESTRELLAMIENTOS', 'ROZAMIENTOS',
#'VOLCAMIENTOS', 'PÉRDIDA DE PISTA', 'OTROS']
indices = [0]
siniestros_df = pd.read_excel(
        datos_raw, 
        sheet_name="SiniestrosClase", 
 #       usecols=columnas,
        keep_default_na = False,
        index_col= indices
        )

siniestros_df2 = siniestros_df.transpose()

# NO USAR ASI
frecuencia_accidentes_df = pd.crosstab(
        index=siniestros_df['Enero'],
        columns="Enero"
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

