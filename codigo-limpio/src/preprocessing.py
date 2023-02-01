"""
describir
"""
from sklearn.preprocessing import OrdinalEncoder

def codificar_categoricas(data, vars, categorias):
    """
    Proceso de one-hot-encoding para un conjunto de variables categóricas
    que tienen las mismas categorías.

    Args:
    ----
    data (pd.DataFrame): Conjunto de datos que se transformará.
    vars (List): Lista de variables categóricas.
    categorias(List): Lista de categorías en común.

    Return:
    ------
    data_coded(pd.DataFrame): Conjunto de datos con nuevas variables
                              despues del one-hot-encoding
    """
    data = data.copy() 
    for var in vars:
        for category in categorias:
            OE = OrdinalEncoder(categories=categorias)
            data[var] = OE.fit_transform(data[[category]])

    data_coded = data

    return data_coded

def ingenieria_variables(data):
    """
    Aplica ingeniería de variables específica, predefinada por el
    autor, a un conjunto de datos (train/test)

    Args:
    -----
    data (pd.DataFrame): Conjunto de datos (train/test) al que se
                        le aplicará cierta ingeniería de variables.
    Return:
    -------
    data_transf (pd.DataFrame): Conjunto de datos después de aplicar
                                la ingeniería de variables
    """
    # Multiplicar algunas columnas
    data_transf = data.copy()

    data_transf['BsmtRating'] = (data['BsmtCond'] 
                                      * data['BsmtQual'])
    data_transf['ExterRating'] = (data['ExterCond'] 
                                       * data['ExterQual'])
    data_transf['BsmtFinTypeRating'] = (data['BsmtFinType1'] 
                                        * data['BsmtFinType2'])
    
    # Sumar algunas columnas
    data_transf['BsmtBath'] = (train_data['BsmtFullBath'] 
                               +train_data['BsmtHalfBath'])

    data_transf['Bath'] = (train_data['FullBath'] 
                           + train_data['HalfBath'])
                
    data_transf['PorchArea'] = (train_data['OpenPorchSF'] 
                                + train_data['EnclosedPorch'] 
                                + train_data['3SsnPorch'] 
                                + train_data['ScreenPorch'])

    return data_transf

