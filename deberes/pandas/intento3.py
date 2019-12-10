# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
"""
Created on Sun Dec  8 22:47:51 2019

@author: DELL
"""

path = 'C://Users//DELL//Documents//Analy//py-chinacalle-paredes-analy//deberes//pandas//base.csv'

siniestros_df = pd.read_csv(
        path, 
#        index_col = 'id',
        keep_default_na= False,
        na_values=[" "],
#        na_filter=0
        )
siniestros_df = siniestros_df.fillna(0)

provincias = siniestros_df['PROVINCIA']

provincias = provincias.drop_duplicates()
indices = provincias.array
provincias = provincias.reindex(indices, fill_value=indices)
indices = np.arange(1,26)
provincias_usar = pd.Series(provincias)
for item in provincias:
    print(item)
    
frecuencia_provincia = pd.crosstab(
        index=siniestros_df["PROVINCIA"],
        columns= "Número de siniestros por provincia"
        )
print(frecuencia_provincia)


fig = plt.figure(figsize=(21,21))
plt.pie(
        frecuencia_provincia, 
        labels=frecuencia_provincia.index,
        autopct="%1.1f%%"
        )
plt.title('Siniestros de tránsito por provincia')
plt.show()

##

type(siniestros_df['NUM_FALLECIDO'])
pd.to_numeric(siniestros_df['NUM_FALLECIDO'])

fallecidos_por_provincias_df = siniestros_df.groupby(
        ['PROVINCIA']
        )['NUM_FALLECIDO' ].sum()
fallecidos_por_provincias_df

fallecidos_por_zonas_provincias_df = siniestros_df.groupby(
        ['ZONA','PROVINCIA']
        )['NUM_FALLECIDO' ].sum()

fallecidos_por_provincias_df.plot(kind='bar', stacked=True, title="Siniestros por zonas")

fallecidos_por_zonas_provincias_df

fallecidos_por_zonas_provincias_df['URBANA']

figura_zonas = plt.figure(figsize=(30,10))
plt.subplot2grid((2,3),(0,0))
fallecidos_por_zonas_provincias_df['URBANA'].plot(kind='bar', alpha= 0.5)
plt.title('Fallecidos en zonas urbanas')

plt.subplot2grid((2,3),(0,1))
fallecidos_por_zonas_provincias_df['RURAL'].plot(kind='bar', alpha= 0.5)
plt.title('Fallecidos en zonas rurales')
plt.show()

figura_zonas_2 = plt.figure(figsize=(30,10))
ax = plt.gca()
#urbana_df = fallecidos_por_zonas_provincias_df['URBANA']
#fallecidos_por_zonas_provincias_df['URBANA'].keys()
#fallecidos_por_zonas_provincias_df['URBANA'].columns()
fallecidos_por_zonas_provincias_df['URBANA'].plot(
        kind='line',
        x=fallecidos_por_zonas_provincias_df['URBANA'].keys(),
        y= 'NUM_FALLECIDO',
        legend='Fallecidos en zonas urbanas',
#        ax=ax
        )
# fallecidos_por_zonas_provincias_df.columns()
fallecidos_por_zonas_provincias_df['RURAL'].plot(
        kind='line',
        x=fallecidos_por_zonas_provincias_df['URBANA'].keys(),
        y= 'NUM_FALLECIDO',
#        ax=ax, 
        legend='reverse',
        color='green')
plt.title('Fallecidos en zonas rurales y urbanas')
plt.show()

fallecidos_por_zonas_provincias_df['RURAL'].plot(kind='line', legend='True')

####
figura_causas= plt.figure(figsize=(20,20))
siniestros_df.assign(columna_extra = 1).groupby(
        ['columna_extra', 'CAUSA']
        ).size().to_frame().unstack().plot(
                kind='bar',
                stacked= True,
                legend= False,
                figsize=(15,15),
#                autopct="%1.1f%%"
                )
plt.title('Causa de los siniestros de tránsito')
plt.xlabel('Causa')
plt.xticks([])
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
plt.show()

leyenda = plt.gca().get_legend_handles_labels()
#leyenda_reversa = reversed(leyenda)
#leyenda_reversa = leyenda
#leyenda_reversa[0] = leyenda_reversa[0][::-1]
#leyenda_reversa[1] = leyenda_reversa[1][::-1]
#

#for i in range(0, len(leyenda_reversa[1])):
#    leyenda_reversa[1][i] = leyenda_reversa[1][len(leyenda_reversa[1])-1-i]

#labels = reversed(siniestros_df['CAUSA'].unique())
labels = siniestros_df['CAUSA']
# labels = labels.drop_duplicates()[::-1]

plt.legend(leyenda, labels, loc='lower right')
plt.show()


fallecidos_por_provincias_df = siniestros_df.groupby(
        ['PROVINCIA']
        )['NUM_FALLECIDO' ].sum()

fallecidos_por_provincias_df.plot(kind='bar', stacked=True, title="Siniestros por zonas")

causas_de_siniestros = siniestros_df.groupby(
        ['PROVINCIA','CAUSA']
        )['TOTAL_VICTIMAS'].sum()

tab = pd.crosstab(siniestros_df['PROVINCIA'],['TOTAL_VICTIMAS'])
pd.crosstab()

figura_zonas = plt.figure(figsize=(30,10))
fig, axs = plt.subplots(4,2)
#for provincia in provincias:
#plt.subplot2grid((1,3),(0,0))
#iterador = iterador + 1
axs[0,0].plot(causas_de_siniestros['COTOPAXI'].plot(kind='bar',
            stacked= True,
            legend= True))

plt.title(f"Siniestros por causa de la provincia COTOPAXI")
axs[0,0].set_title(f"Siniestros por causa de la provincia COTOPAXI")

plt.subplot2grid((1,3),(0,1))
causas_de_siniestros['MANABÍ'].plot(kind='bar',
            stacked= True,
            legend= True)
plt.title(f"Siniestros por causa de la provincia MANABÍ")

plt.subplot2grid((1,3),(1,0))
causas_de_siniestros['SANTO DOMINGO DE LOS TSÁCHILAS'].plot(kind='bar',
            stacked= True,
            legend= True)
plt.title(f"Siniestros por causa de la provincia SANTO DOMINGO DE LOS TSÁCHILAS")

plt.subplot2grid((1,3),(1,1))
causas_de_siniestros['PICHINCHA'].plot(kind='bar',
            stacked= True,
            legend= True)
plt.title(f"Siniestros por causa de la provincia PICHINCHA")
plt.show()


llaves = pd.Series(provincias.keys())
llaves

figura_zonas = plt.figure(figsize=(50,180))
for i in range(1, int(len(provincias)/4)):
    plt.subplot(12,2,i)
    causas_de_siniestros[provincias[llaves[i]]].plot(kind='bar',
            stacked= True,
            legend= True)
    plt.title(f"Siniestros por causa de la provincia ${provincias[llaves[i]]}")
    
figura_zonas = plt.figure(figsize=(40,180))
for i in range((len(provincias)/4), int((len(provincias)/4)*2)):
    plt.subplot(12,2,i)
    causas_de_siniestros[provincias[llaves[i]]].plot(kind='bar',
            stacked= True,
            legend= True)
    plt.title(f"Siniestros por causa de la provincia ${provincias[llaves[i]]}")
    
for provincia in provincias:
    figura_zonas = plt.figure(figsize=(20,20))
    causas_de_siniestros[provincia].plot(kind='bar',
            stacked= True,
            legend= True)
    plt.title(f"Siniestros por causa de la provincia ${provincia}")
    plt.savefig("imagen.png")
    plt.show()
    

    
#######

siniestros_df.groupby('state')['name'].nunique().plot(kind='bar')
plt.show()


####
figura_zonas = plt.figure(figsize=(20,20))
frecuencia_siniestros_dias = siniestros_df.groupby(
        ['DIA', 'CAUSA']).size().unstack().plot(
                kind='bar', stacked=True,
                figsize=(20,20)
                )
plt.show()

frecuencia_dias = pd.crosstab(
        index= siniestros_df["DIA"],
        columns="frecuencia_dia"
        )
plt.pie(
        frecuencia_dias, 
        labels=frecuencia_dias.index,
        autopct = "%1.1f%%")
plt.xlabel("Dias de la semana")


causas_de_siniestros = siniestros_df.groupby(
        ['DIA','PROVINCIA']
        )['TOTAL_VICTIMAS'].sum()
total_victimas = siniestros_df['TOTAL_VICTIMAS'].sum()
total_victimas
siniestros_df.groupby(
        ['DIA','PROVINCIA']
        )['TOTAL_VICTIMAS'].size().unstack().plot(
        kind='bar',
        stacked= True,
        figsize=(20,20)
        )
plt.show()

###


siniestros_df.groupby(
        ['PROVINCIA']
        )['NUM_FALLECIDO'].size().unstack().plot(
        kind='bar',
        stacked= True,
        figsize=(20,20)
        )
plt.show()



###

fig = plt.figure(figsize=(10,5))
siniestros_df.DIA[siniestros_df.NUM_FALLECIDO > 0].value_counts(
        normalize= True
        ).plot(
                kind= 'line',
                alpha=0.5
                )
plt.title('Fallecidos por dia de la semana')
plt.show()


