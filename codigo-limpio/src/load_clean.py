"""
Este script le permite al usuario hacer la carga y limpieza 
del conjunto de validación y prueba.



"""
import yaml
import pandas as pd
import sys
sys.path.append('/visualization/')

#Hacer la carga de datos
def cargar_datos():
    """
    Carga de datos de entrenamiento y validación.
        
    Return:
    --------
    Dos data frames. 
    
    train_data (pd.DataFrame): Conjunto de datos de entrenamiento.
    test_data (pd.DataFrame): Conjunto de datos de prueba.
    """

    # Abrir yaml
    with open("../config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Conjunto de entrenamiento
    train_data = pd.read_csv(config['data']['TRAIN_PATH'])

    #Conjunto de prueba
    test_data = pd.read_csv(config['data']['TEST_PATH'])
    
    return train_data, test_data

def fill_categorical_na(data, vars_incompletas, valor_nuevo):
    '''
    Rellena los datos faltantes para variables categoricas
    en un set de datos.

    Args:
    -----

    vars_incompletas(List) :    Lista de variables con valores NA.
    valor_nuevo: Valor que actualiza el dato con NA.

    Return:
    -------
    transf_data(pdDataFrame): Conjunto de datos de entrada con
                              imputación de nuevo valores.
    ---
    '''
    data=data.copy()

    #Rellenar los datos NA con 'valor_nuevo'.
    for var in vars_incompletas: data[var].fillna(valor_nuevo, inplace=True)

    return data

def fill_num_na(data):
    '''
    Rellena los datos faltantes para variables numéricas.
    A variables de tipo int o float64 se les imputa la media,
    en otro caso, la moda.

    Args:
    -----
    data(pd.DataFrame): Conjunto de datos. 

    Return:
    -------
    transf_data(pdDataFrame): Conjunto de datos de entrada con
                              imputación de nuevo valores.
    ---
    '''
    data=data.copy()

    #Rellenar los datos NA.
    for col in data.columns:
        if((data[col].dtype == 'float64') or (data[col].dtype == 'int64')):
            data[col].fillna(data[col].mean(), inplace=True)
        else:
             data[col].fillna(data[col].mode()[0], inplace=True)

    return data

    

    
