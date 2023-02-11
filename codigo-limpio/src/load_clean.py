""" Paquete de limpieza de datos.
Este script le permite al usuario hacer la carga y limpieza del conjunto
de validación y prueba.

Este archivo puede importarse como modulo y contiene las siguientes funciones:

    * cargar_datos: Carga de datos de entrenamiento y validación.
    * fill_categorical_na: Rellena valores faltantes en vars. categoricas.
    * fill_num_na: Rellena valores faltantes en variables numéricas.

"""
import yaml
import pandas as pd

# Hacer la carga de datos
def cargar_datos(pth):
    """
    Funcion para carga de datos.
    ---------------------------------------------
    Return:
    --------
    data (pd.DataFrame): Conjunto de datos de como dataframe.
    """

    # Almacenar data como dataframe
    data = pd.read_csv(pth)

    return data




def fill_categorical_na(data, vars_incompletas, valor_nuevo):
    '''
    Rellena los datos faltantes para variables categoricas
    en un set de datos.

    Args:
    -----
    vars_incompletas(List) :    Lista de variables con valores NA.
    valor_nuevo: Valor que actualiza el dato con NA.
    --------------------------------------------------------------
    Return:
    -------
    transf_data(pdDataFrame): Conjunto de datos de entrada con
                              imputación de nuevo valores.
    ---
    '''
    try:
        # Copia de los datos de entrada
        data = data.copy()
        # Rellenar los datos NA con 'valor_nuevo'.
        for var in vars_incompletas:
            data[var].fillna(valor_nuevo, inplace=True)
        return data
    except:
        pass



def fill_num_na(data):
    '''
    Rellena los datos faltantes para variables numéricas.
    A variables de tipo int o float64 se les imputa la media,
    en otro caso, la moda.

    Args:
    -----
    data(pd.DataFrame): Conjunto de datos
    ----------------------------------------------------------
    Return:
    -------
    transf_data(pdDataFrame): Conjunto de datos de entrada con
                              imputación de nuevo valores.
    '''
    # Copia de los datos de entrada
    data = data.copy()
    # Rellenar los datos NA.
    for col in data.columns:
        if data[col].dtype in ('float64', 'int64'):
            data[col].fillna(data[col].mean(), inplace=True)
        else:
            data[col].fillna(data[col].mode()[0], inplace=True)
    return data
