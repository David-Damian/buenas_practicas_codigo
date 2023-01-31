"""
Este script le permite al usuario hacer la carga y limpieza 
del conjunto de validación y prueba.



"""
import yaml
import pandas as pd

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
    #Obtener directorio de trabajo actual
    cwd = os.getcwd()
    

    # Abrir yaml
    with open("../config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Conjunto de entrenamiento
    train_data = pd.read_csv(config['data']['TRAIN_PATH'])

    #Conjunto de prueba
    test_data = pd.read_csv(config['data']['TEST_PATH'])
    
    return train_data, test_data

def fill_datos_faltantes(data):
    '''
    Rellena los datos faltantes en el conjunto de entrenamiento o prueba.

    Args:
    -----
    data(pd.DataFrame) :    Conjunto de entrenamiento o prueba.

    Return:
    -------
    Un par de dataframes:
    train_transformed(pdDataFrame): Conjunto de datos transformado.
    ---
    '''
    #Rellenar los datos NA con No
    for var in variables_incompletas:
        data[var].fillna("No", inplace=True)

    # Rellena los datos faltantes de variables float o int con la media o moda.
    for col in data.columns:
        if((data[col].dtype == 'float64') or (data[col].dtype == 'int64')):
            data[col].fillna(data[col].mean(), inplace=True)
        else:
            data[col].fillna(data[col].mode()[0], inplace=True)
    return data
    

    
