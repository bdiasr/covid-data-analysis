import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import geopandas as gpd 
from shapely import wkt
from shapely import geometry
from shapely.geometry import Point, base
import mapclassify


df = pd.read_csv('dados-ms.csv', delimiter=";", encoding="latin1")

all_cities_df = pd.read_csv('dados-ms.csv', delimiter=";", encoding="latin1", usecols=['estado', 'municipio', 'evolucaoCaso', 'idade'])

#data frame apenas com municipios 
def citiesdf():
    cities_df = pd.read_csv('dados-ms.csv', delimiter=";", encoding="latin1", usecols=['municipio'])
    return cities_df


#Aplicando filtros no dataFrame Cancelado, NaN e apenas do mato grosso do sul
case_filter_cancelado = all_cities_df[all_cities_df['evolucaoCaso'] == 'Cancelado'].index
all_cities_df.drop(case_filter_cancelado, inplace=True)
all_cities_df = all_cities_df.dropna(axis=0,how='all', subset=['evolucaoCaso'])
case_filter_ms = all_cities_df[all_cities_df['estado'] != 'MATO GROSSO DO SUL'].index
all_cities_df.drop(case_filter_ms, inplace=True)

#Poligono do Brasil 
uf_br0 = gpd.read_file('Files/gadm36_BRA_0.shp')
#Estados do Brasil 
uf_br1 = gpd.read_file('Files/gadm36_BRA_1.shp')
#Municipios do Brasil
uf_br2 = gpd.read_file('Files/gadm36_BRA_2.shp')
#Distritos do Brasil
uf_br3 = gpd.read_file('Files/gadm36_BRA_3.shp')

#Filtrar o Estado do Mato Grosso do Sul 
uf_br1_ms = uf_br1[uf_br1.GID_1 == 'BRA.11_1']

#Filtrar os Municipios do Mato Grosso do Sul
uf_br2_ms = uf_br2[uf_br2.GID_1 == 'BRA.11_1']

#cidades do MS
uf_br2_ms_cities = uf_br2_ms[['NAME_2', 'geometry']]

#converter polygon para point
uf_br2_ms_cities_points = uf_br2_ms_cities.copy()

#uf_br2_ms_cities_points.geometry = uf_br2_ms_cities_points['geometry'].centroid

#Agora, vamos criar um Pandas DataFrame a partir desse GeoPandas DataFrame
uf_br2_ms_cities_df = pd.DataFrame(uf_br2_ms_cities_points)

#Agora, vamos criar uma nova coluna no dataframe com os casos de covid, que vai relacionar o municipio e sua coordenada 
all_cities_df['geometry'] = 'NaN'  #incluir a coluna geometry, pois indexarei as coordenadas nela 

uf_br2_ms_cities_df.rename(columns={'NAME_2': 'municipio'}, inplace=True) # uniformizando os nomes no DataFrame

# Separaremos o data frame all_cities_df em outros: Cura, internados na UTI, internados, óbitos e Em Tratamento domicilar 
# a principal razão dessa separação é a otimização do problema 
cure_cities_df = all_cities_df.loc[(all_cities_df['evolucaoCaso']) == 'Cura'] 
hospitalized_cities_df = all_cities_df.loc[(all_cities_df['evolucaoCaso']) == 'Internado']
hospitalizedICU_cities_df = all_cities_df.loc[(all_cities_df['evolucaoCaso']) == 'Internado em UTI']
death_cities_df = all_cities_df.loc[(all_cities_df['evolucaoCaso']) == 'Óbito']
home_treatment_cities_df =  all_cities_df.loc[(all_cities_df['evolucaoCaso']) == 'Em tratamento domiciliar']

# Agora, vamos adicionar as coordenadas nos respectivos data frames
'''
# Para o data base com óbitos
for i in range(len(death_cities_df)):
    aux = death_cities_df.iloc[i, 1]

    for j in range(len(uf_br2_ms_cities_df)):
        if(aux == uf_br2_ms_cities_df.iloc[j, 0]):
            coord_aux = uf_br2_ms_cities_df.iloc[j, 1]
            death_cities_df.iloc[i, 4] = coord_aux 
'''
'''
# Para o dataFrame de internados
for i in range(len(hospitalized_cities_df)):
    aux = hospitalized_cities_df.iloc[i, 1]

    for j in range(len(uf_br2_ms_cities_df)):
        if(aux == uf_br2_ms_cities_df.iloc[j, 0]):
            coord_aux = uf_br2_ms_cities_df.iloc[j, 1]
            hospitalized_cities_df.iloc[i, 4] = coord_aux 
'''
'''
# Para o dataFrame de internados na UTI
for i in range(len(hospitalizedICU_cities_df)):
    aux = hospitalizedICU_cities_df.iloc[i, 1]

    for j in range(len(uf_br2_ms_cities_df)):
        if(aux == uf_br2_ms_cities_df.iloc[j, 0]):
            coord_aux = uf_br2_ms_cities_df.iloc[j, 1]
            hospitalizedICU_cities_df.iloc[i, 4] = coord_aux 
'''
'''
# Para o dataFrame de em tratamento domicilar 
for i in range(len(home_treatment_cities_df)):
    aux = home_treatment_cities_df.iloc[i, 1]

    for j in range(len(uf_br2_ms_cities_df)):
        if(aux == uf_br2_ms_cities_df.iloc[j, 0]):
            coord_aux = uf_br2_ms_cities_df.iloc[j, 1]
            home_treatment_cities_df.iloc[i, 4] = coord_aux 
'''
'''
# Para o dataFrame de curados 
for i in range(len(cure_cities_df)):
    aux = cure_cities_df.iloc[i, 1]

    for j in range(len(uf_br2_ms_cities_df)):
        if(aux == uf_br2_ms_cities_df.iloc[j, 0]):
            coord_aux = uf_br2_ms_cities_df.iloc[j, 1]
            cure_cities_df.iloc[i, 4] = coord_aux 
'''

#Armazenar o conteudo desse conjunto de dados num dataFrame
#cure_cities_df.to_csv('curados.txt', header=False, index=False)
#death_cities_df.to_csv('mortos.txt', header=True, index=False)
#hospitalized_cities_df.to_csv('internados.txt', header=True, index=False)
#hospitalizedICU_cities_df.to_csv('internados_na_UTI.txt', header=True, index=False)
#home_treatment_cities_df.to_csv('tratamento_domicilar.txt', header=True, index=False)
#cure_cities_df.to_csv('curados.txt', header=True, index=False)

#print(cure_cities_df)

# Com base nos nossos diferentes DataFrames, iremos plotar diferentes informações no estado do Mato Grosso do Sul 
# Definimos nossa base do mapa do estado
estado_ms = uf_br2_ms_cities.plot(color = 'white', edgecolor='black') 

cities = pd.read_csv('cidades.txt', delimiter=',')

# Gera o mapa de mortes por COVID no estado do Mato grosso do Sul 
def map_death():

    casos  = death_cities_df

    # Para o dataFrame de internados na UTI 
    for i in range(len(casos)):
        aux = casos.iloc[i, 1]
        for j in range(len(cities)):
            if(aux == cities.iloc[j, 0]):
                coord_aux = cities.iloc[j, 1]
                casos.iloc[i, 4] = coord_aux 

    #tratar os casos em que nao tem conteudo na coluna
    casos = casos.dropna(axis=0,how='all', subset=['geometry'])

    # Descreve a quantidade de internados por municipio 
    quant_casos = casos['municipio'].value_counts()
    
    quant_casos = pd.DataFrame(quant_casos)
    quant_casos_total = quant_casos.sum() #Quantidade total
    quant_casos['percent'] = 0
    quant_casos['geometry'] = 'NaN'

    
    for i in range(len(quant_casos)):
        quant_casos.iloc[i, 1] = (quant_casos.iloc[i, 0]/quant_casos_total)*100

    
    for i in range(len(casos)):
        aux = casos.iloc[i, 1]
        for j in range(len(quant_casos)):
            if (aux == quant_casos.index[j]):
                    aux2 = casos.iloc[i, 4]
                    quant_casos.iloc[j, 2] = aux2
    
    
    quant_casos = quant_casos.drop(["Ladário", "Paraíso das Águas"])
    print(quant_casos)
    
    quant_casos['geometry'] = gpd.GeoSeries.from_wkt(quant_casos['geometry'])
    gdf = gpd.GeoDataFrame(quant_casos, geometry='geometry')

    gdf.plot(ax = estado_ms, column='percent', legend=True, cmap='YlOrRd',
    legend_kwds={'label': "Porcentagem de óbitos na UTI por COVID-19 no estado do Mato Grosso do Sul", 'orientation': "horizontal"})
    plt.show()

# Gera o mapa de internações por COVID no estado do Mato grosso do Sul 
def map_hospitalized():

    hospitalized_cities_df = all_cities_df.loc[(all_cities_df['evolucaoCaso']) == 'Internado']
    casos  = hospitalized_cities_df
    #uf_br2_ms_cities_df.to_csv('cidades.txt', header=True, index=False)
    cities = pd.read_csv('cidades.txt', delimiter=',')

    # Para o dataFrame de internados
    for i in range(len(casos)):
        aux = casos .iloc[i, 1]
        for j in range(len(cities)):
            if(aux == cities.iloc[j, 0]):
                coord_aux = cities.iloc[j, 1]
                casos.iloc[i, 4] = coord_aux 

    #tratar os casos em que nao tem conteudo na coluna
    casos = casos.dropna(axis=0,how='all', subset=['geometry'])

    #casos.to_csv('internados.txt', header=True, index=False)

    # Descreve a quantidade de internados por municipio 
    quant_casos = casos['municipio'].value_counts()
    
    quant_casos = pd.DataFrame(quant_casos)
    quant_casos_total = quant_casos.sum() #Quantidade total
    quant_casos['percent'] = 0
    quant_casos['geometry'] = 'NaN'

    
    for i in range(len(quant_casos)):
        quant_casos.iloc[i, 1] = (quant_casos.iloc[i, 0]/quant_casos_total)*100

    
    for i in range(len(casos)):
        aux = casos.iloc[i, 1]
        for j in range(len(quant_casos)):
            if (aux == quant_casos.index[j]):
                aux2 = casos.iloc[i, 4]
                quant_casos.iloc[j, 2] = aux2
    
    #Não temos as coordenadas dessas cidades 
    quant_casos = quant_casos.dropna()
    quant_casos = quant_casos.drop(["Ladário", "Batayporã"])

    quant_casos['geometry'] = gpd.GeoSeries.from_wkt(quant_casos['geometry'])
    gdf = gpd.GeoDataFrame(quant_casos, geometry='geometry')

    gdf.plot(ax = estado_ms, column='percent', legend=True, cmap='YlOrRd',legend_kwds={'label': "Porcentagem de internação por COVID-19 no estado do Mato Grosso do Sul", 'orientation': "horizontal"})
    plt.show()
    
# Gera o mapa de internação na UTI por COVID no estado do Mato Grosso do Sul 
def map_hospitalizedICU():

    casos  = hospitalizedICU_cities_df

    # Para o dataFrame de internados na UTI 
    for i in range(len(casos)):
        aux = casos.iloc[i, 1]
        for j in range(len(cities)):
            if(aux == cities.iloc[j, 0]):
                coord_aux = cities.iloc[j, 1]
                casos.iloc[i, 4] = coord_aux 

    #tratar os casos em que nao tem conteudo na coluna
    casos = casos.dropna(axis=0,how='all', subset=['geometry'])

    # Descreve a quantidade de internados por municipio 
    quant_casos = casos['municipio'].value_counts()
    #print(quant_casos)
    
    quant_casos = pd.DataFrame(quant_casos)
    quant_casos_total = quant_casos.sum() #Quantidade total
    quant_casos['percent'] = 0
    quant_casos['geometry'] = 'NaN'

    
    for i in range(len(quant_casos)):
        quant_casos.iloc[i, 1] = (quant_casos.iloc[i, 0]/quant_casos_total)*100

    
    for i in range(len(casos)):
        aux = casos.iloc[i, 1]
        for j in range(len(quant_casos)):
            if (aux == quant_casos.index[j]):
                    aux2 = casos.iloc[i, 4]
                    quant_casos.iloc[j, 2] = aux2
    
    quant_casos = quant_casos.drop(["Figueirão"])

    quant_casos['geometry'] = gpd.GeoSeries.from_wkt(quant_casos['geometry'])
    gdf = gpd.GeoDataFrame(quant_casos, geometry='geometry')

    gdf.plot(ax = estado_ms, column='percent', legend=True, cmap='YlOrRd',
    legend_kwds={'label': "Porcentagem de internação na UTI por COVID-19 no estado do Mato Grosso do Sul", 'orientation': "horizontal"})
    plt.show()

def map_home_treatment():

    casos  = home_treatment_cities_df

    # Para o dataFrame de internados na UTI 
    for i in range(len(casos)):
        aux = casos.iloc[i, 1]
        for j in range(len(cities)):
            if(aux == cities.iloc[j, 0]):
                coord_aux = cities.iloc[j, 1]
                casos.iloc[i, 4] = coord_aux 

    #tratar os casos em que nao tem conteudo na coluna
    casos = casos.dropna(axis=0,how='all', subset=['geometry'])

    # Descreve a quantidade de internados por municipio 
    quant_casos = casos['municipio'].value_counts()
    
    quant_casos = pd.DataFrame(quant_casos)
    quant_casos_total = quant_casos.sum() #Quantidade total
    quant_casos['percent'] = 0
    quant_casos['geometry'] = 'NaN'

    
    for i in range(len(quant_casos)):
        quant_casos.iloc[i, 1] = (quant_casos.iloc[i, 0]/quant_casos_total)*100

    
    for i in range(len(casos)):
        aux = casos.iloc[i, 1]
        for j in range(len(quant_casos)):
            if (aux == quant_casos.index[j]):
                    aux2 = casos.iloc[i, 4]
                    quant_casos.iloc[j, 2] = aux2
    
    #print(quant_casos)
    quant_casos.to_csv('casa.txt', header=True, index=False)
    quant_casos = quant_casos.drop(["Figueirão", "Batayporã", "Fátima do Sul", "Ladário"])

    
    quant_casos['geometry'] = gpd.GeoSeries.from_wkt(quant_casos['geometry'])
    gdf = gpd.GeoDataFrame(quant_casos, geometry='geometry')

    gdf.plot(ax = estado_ms, column='percent', legend=True, cmap='YlOrRd',
    legend_kwds={'label': "Porcentagem de tratamento domicilar por COVID-19 no estado do Mato Grosso do Sul", 'orientation': "horizontal"})
    plt.show()

map_home_treatment()
#map_death()