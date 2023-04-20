# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

# Recordar utilizar la ruta relativa, no la absoluta para ingestar los datos desde los CSV.
# EJ: 'datasets/xxxxxxxxxx.csv'

from xml.dom.minidom import Entity
import pandas as pd
import numpy as np


def Ret_Pregunta01():
    ''' Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros cuya entidad sean Colombia o México retornando ese valor en un dato de tipo tupla (catidad de registros Colombia, catidad de registros México).
    Pista: averiguar la funcion Shape '''
    #Tu código aca:
    df1 = pd.read_csv('datasets\Fuentes_Consumo_Energia.csv')
    df1_mex = df1[df1['Entity'] == 'Mexico']
    df1_col = df1[df1['Entity'] == 'Colombia']
    tupla_mex_col = (df1_mex.shape[0], df1_col.shape[0])
    return tupla_mex_col


def Ret_Pregunta02():
    ''' Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe eliminar las columnas 'Code' y 'Entity' y luego informar la cantidad de columnas
    retornando ese valor en un dato de tipo entero. '''
    #Tu código aca:
    #return 'Funcion incompleta'
    df2 = pd.read_csv('datasets\Fuentes_Consumo_Energia.csv')
    delete_columns = ['Entity', 'Code']
    df2 = df2.drop(labels=delete_columns, axis=1)
    return df2.shape[1]


def Ret_Pregunta03():
    ''' Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros de la columna Year sin tener en cuenta aquellos con valores faltantes
    retornando ese valor en un dato de tipo entero. '''
    #Tu código aca:
    df3 = pd.read_csv('datasets\Fuentes_Consumo_Energia.csv')
    df3 = df3.dropna(subset=['Year'])
    return df3.shape[0]


def Ret_Pregunta04():
    ''' Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    El ExaJulio es una unidad diferentes al TWh, es decir, no tiene sentido sumarlos o
    buscar proporciones entre ellos, la fórmula de conversión es:
    277.778 Teravatios/Hora (TWh) = 1 Exajulio
    Los campos terminados en "_EJ" corresponden a mediciones en Exajulios,
    y los terminados en "_TWh" corresponden a Teravatios/Hora.
    La consigna es crear un nuevo campo, que se denomine "Consumo_Total"
    y que guarde la sumatoria de todos los consumos expresados en Teravatios/Hora
    (convirtiendo a esta medida los que están en Exajulios)
    Esta función debe informar el consumo total para la entidad 'World' y año '2019',
    redondeado a 2 decimales, retornando ese valor en un dato de tipo float. '''
    #Tu código aca:
    df4 = pd.read_csv('datasets\Fuentes_Consumo_Energia.csv')

    df4_ej = ['Coal_Consumption_EJ','Gas_Consumption_EJ','Oil_Consumption_EJ']
    df4__twh = ['Geo_Biomass_Other_TWh','Hydro_Generation_TWh','Nuclear_Generation_TWh','Solar_Generation_TWh','Wind_Generation_TWh']

    df4['ej_tot_twh'] = df4[df4_ej].apply(lambda x: sum(x) * 277.778, axis=1)
    df4['twh_tot_twh'] = df4[df4__twh].apply(sum, axis=1)
    df4['tot_cons'] = df4['ej_tot_twh'] + df4['twh_tot_twh']

    return round(df4.loc[(df4['Entity'].isin(['World'])) & (df4['Year'].isin([2019])), 'tot_cons'].iloc[0], 2)


def Ret_Pregunta05():
    ''' Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar el año de mayor generación de energía hídrica (Hydro_Generation_TWh)
    para la entidad 'Europe' retornando ese valor en un dato de tipo entero. '''
    #Tu código aca:
    df5 = pd.read_csv('datasets\Fuentes_Consumo_Energia.csv')
    df5_eu = df5[df5['Entity'] == 'Europe']

    return df5_eu.loc[df5_eu['Hydro_Generation_TWh'] == df5_eu['Hydro_Generation_TWh'].max(), 'Year'].iloc[0]


def Ret_Pregunta06(m1, m2, m3):
    ''' Esta función recibe tres array de Numpy de 2 dimensiones cada uno, y devuelve el valor booleano
    True si es posible realizar una multiplicación entre las tres matrices (n1 x n2 x n3),
    y el valor booleano False si no lo es
    Ej:
        n1 = np.array([[0,0,0],[1,1,1],[2,2,2]])
        n2 = np.array([[3,3],[4,4],[5,5]])
        n3 = np.array([1,1],[2,2])
        print(Ret_Pregunta06(n1,n2,n3))
            True            -> Valor devuelto por la función en este ejemplo
        print(Ret_Pregunta06(n2,n1,n3))
            False            -> Valor devuelto por la función en este ejemplo '''
    #Tu código aca:
    m1_shape = m1.shape
    m2_shape = m2.shape
    m3_shape = m3.shape
    
    if m1_shape[1] == m2_shape[0] and m2_shape[1] == m3_shape[0]:
        return True
    else:
        return False


def Ret_Pregunta07():
    ''' Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "GGAL - Cotizaciones historicas.csv". Este csv contiene información de cotización de la 
    acción del Banco Galcia SA. Esta función debe tomar la columna máximo y 
    devolver la suma de los valores de esta, con 4 decimales después del punto, redondeado. '''
    #Tu código aca:
    df7 = pd.read_csv('datasets\GGAL - Cotizaciones historicas.csv')
    max_aperture = sum(df7['maximo'])
    return round(max_aperture, 4)


def Ret_Pregunta08():
    ''' Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de entidades diferentes que están presentes en el dataset
    retornando ese valor en un dato de tipo entero. '''
    #Tu código aca:
    df8 = pd.read_csv('datasets\Fuentes_Consumo_Energia.csv')

    entities = []
    for index, row in df8.iterrows():
        if row['Entity'] not in entities:
            entities.append(row['Entity'])
    
    return len(entities)


def Ret_Pregunta09():
    ''' Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Tabla1_ejercicio.csv" y "datasets/Tabla2_ejercicio.csv".
    Esta función debe retornar: score_promedio_femenino y score_promedio_masculino en formato tupla, teniendo en cuenta que no debe haber valores repetidos. '''
    #Tu código aca:
    df9_1 = pd.read_csv('datasets\Tabla1_ejercicio.csv', sep=';')
    df9_2 = pd.read_csv('datasets\Tabla2_ejercicio.csv', sep=';')

    # df9_1.drop_duplicates(subset=['pers_id'], keep='first', inplace=True)
    # df9_2.drop_duplicates(subset=['pers_id'], keep='first', inplace=True)
    # df9_1 = df9_1.reset_index(drop=True)
    # df9_2 = df9_2.reset_index(drop=True)

    df9_merged = pd.merge(df9_1, df9_2, on='pers_id', how='right').drop_duplicates()
    df9_1['score'] = df9_merged['score']

    promedio_femenino = df9_merged.loc[df9_merged['sexo'] == 'F', 'score'].mean()
    promedio_masculino = df9_merged.loc[df9_merged['sexo'] == 'M', 'score'].mean()

    return (round(promedio_femenino, 2), (round(promedio_masculino, 2)))


def Ret_Pregunta10(lista):
    ''' Esta función recibe como parámetro un objeto de la clase Lista() definida en el archivo Lista.py.
    Debe recorrer la lista y retornan la cantidad de nodos que posee. Utilizar el método de la clase
    Lista llamado getCabecera()
    Ejemplo:
        lis = Lista()
        lista.agregarElemento(1)
        lista.agregarElemento(2)
        lista.agregarElemento(3)
        print(Ret_Pregunta10(lista))
            3    -> Debe ser el valor devuelto por la función Ret_Pregunta10() en este ejemplo '''
    #Tu código aca:
    return lista.contarElementos()