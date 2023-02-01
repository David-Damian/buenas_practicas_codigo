"""
describir
"""
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder

def codificar_ordinales(data,var,categorias):
    """
    Proceso de codificar un conjunto de variables ordinales, es decir
    en donde importa el orden, que tienen las mismas categorías.

    Args:
    ----
    data (pd.DataFrame): Conjunto de datos que se transformará.
    var (List): Lista de variables categóricas.
    categorias(List): Lista de categorías en común.

    Return:
    ------
    data_coded(pd.DataFrame): Conjunto de datos con nuevas variables
                              despues de la codificacion.
    """
    data_coded = data.copy()
    for vari in var:
        for category in categorias:
            encoder_ordinal = OrdinalEncoder(categories=categorias)
            data_coded[vari] = encoder_ordinal.fit_transform(data[[category]])

    return data_coded


def codificar_categoricas(data,var):
    """
    Proceso de codificar un conjunto de variables categoricas.

    Args:
    ----
    data (pd.DataFrame): Conjunto de datos que se transformará.
    var (List): Lista de variables categóricas.

    Return:
    ------
    data_coded(pd.DataFrame): Conjunto de datos con nuevas variables
                              despues de la codificación.
    """

    data_coded = data.copy()
    label_encoder = LabelEncoder()
    for vari in var:
        data_coded[vari] = label_encoder.fit_transform(data[vari])
    return data_coded


def ingenieria_variables(data):
    """
    Aplica ingeniería de variables específica, predefinada por el
    autor/usuario, a un conjunto de datos (train/test)

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
    data_transf['BsmtBath'] = (data['BsmtFullBath']
                               + data['BsmtHalfBath'])

    data_transf['Bath'] = (data['FullBath']
                           + data['HalfBath'])

    data_transf['PorchArea'] = (data['OpenPorchSF']
                                + data['EnclosedPorch']
                                + data['3SsnPorch']
                                + data['ScreenPorch'])

    return data_transf
