"""
Este script le permite al usuario hacer la carga y limpieza 
del conjunto de validación y prueba.



"""

#Definimos una función para hacer la carga de datos
def cargar_datos():
    ''''
    Carga de datos de entrenamiento y validación.
    Si DROP==TRUE, 
        
    Return:
    --------
    Dos data frames. 
    
    train_data (pd.DataFrame): Conjunto de datos de entrenamiento.
    test_data (pd.DataFrame): Conjunto de datos de prueba.
    ''''
    # Conjunto de entrenamiento
    train_data = pd.read_csv("house-prices-data/train.csv")
    #Conjunto de prueba
    test_data = pd.read_csv("house-prices-data/test.csv")
    
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
    variables_incompletas=['FireplaceQu', 'BsmtQual', 'BsmtCond', 'BsmtFinType1', 'BsmtFinType1', 'BsmtFinType2']
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
    

    
