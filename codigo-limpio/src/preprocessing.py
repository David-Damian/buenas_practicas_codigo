""" Paquete de preprocesamiento de datos.
Este script le permite al usuario hacer un procesamiento de los datos
de entrenamiento y prueba predefinido.
Al modificar este codigo, otro preprocesamiento puede ser especificado.

Este archivo puede importarse como modulo y contiene las siguientes funciones:

    * ordinal_encoding: Codificación de variables ordinales en
                        ciertas categorias predefinidas.
    * codificar_categoricas: Codificacion de valores en vars. categoricas
                             a numericas.
    * ingenieria_variables: Transformacion de algunas variables.
"""
import json
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder


def ordinal_encoding(data):
    """
    Tranforma ciertas variables dadas categorias específifcas.
    Las variables y categorias se especifican en el archivo JSON
    ordinal_dict.json.

    Args:
    -----
    data (pd.DataFrame): Datos a transformar.

    Return:
    -------
    data_coded (pd.DataFrame): Datos transformados.
    """
    # Abrir JSON

    with open('src/ordinal_dict.json', encoding='utf-8') as codigos_json:
        codes = json.load(codigos_json)
        # Transformar datos
        data_coded = data.copy()
        for var, categories in codes.items():
            ordinal_encoder = OrdinalEncoder(categories=[categories])
            data_coded[var] = ordinal_encoder.fit_transform(data[[var]])
        codigos_json.close()

    return data_coded


def codificar_categoricas(data, cat_vars):
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
    for vari in cat_vars:
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
