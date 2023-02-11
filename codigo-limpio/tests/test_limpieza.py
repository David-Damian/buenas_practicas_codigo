"""
Script para testear las funciones de limpieza de datos
que estan en src/load_clean
"""
import numpy as np
import logging
import yaml
import pytest
from src import load_clean as cln


@pytest.fixture(scope="module")
def path():
    '''
    Fixture - La función test_cargar_datos() va a utilizar
    el retorno del path() como un argumento.
    '''
    # Abrir yaml para obtener ruta de los datos.
    with open("../config.yaml", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    pth = config['test']['TRAIN_PATH']
    return pth


def test_cargar_datos(path):
    '''
     Probar si los datos de entrenamiento estan
     en data/raw/ y que haya suficientes datos
     de entrenamiento
    '''
    try:
        data = cln.cargar_datos(path)
    except FileNotFoundError as file_err:
        logging.error(f"Los datos de entrenamiento no están "
                      "en el {path()}")
        raise file_err

    # probar si hay suficientes datos de entrenamiento
    try:
        assert cln.cargar_datos(path).shape[0] * 0.8>1000
    except AssertionError as ass_err:
        logging.error("Testing cargar_datos: No hay datos suficientes "
                       "para entrenar el modelo")
        raise ass_err


@pytest.fixture(scope="module")
def train_set(path):
    '''
    Fixture - La funciones fill_categorical_na() y
    test_fill_num_na van a utilizar el retorno de
    esta funcion como un argumento.

    Return:
    ------
    train_data(pd.DataFrame): Datos de entrenamiento.
    '''
    train_data = cln.cargar_datos(path)
    return train_data


@pytest.fixture(scope="module")
def vars_incompletas():
    '''
    Fixture - La función fill_categorical_na()
    va a utilizar el retorno de esta funcion
    como un argumento.
    -------------------------------------------
    Return:
    ------
    vars_incompletas(List): Columnas que tienen NAs
                            y entraran al modelo
    '''
    # Abrir yaml para obtener ruta de los datos.
    with open("../config.yaml", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    vars_incompletas = config['main']['VARS_INCOMPLETAS']
    return vars_incompletas


def test_fill_categorical_na(train_set, vars_incompletas):
    '''
    Probar si todas las variables a droppear
    pertenecen al set de train.
    '''
    try:
        columnas_train = train_set.columns
        assert np.isin(vars_incompletas, columnas_train).sum()==len(vars_incompletas)
    except AssertionError as ass_err:
        logging.error("No todas las columnas pertenecen al set de entrenamiento")
        raise ass_err
    try:
        # probar si se rellenan correctamente
        # los na de vars_incompletas
        train_filled = cln.fill_categorical_na(train_set, vars_incompletas, "No")
        vars_filled = train_filled[vars_incompletas]
        assert vars_filled.isna().sum().sum()==0
    except AssertionError as ass_err:
        logging.error("No se han rellenado todos los NA de las variables "
                      "incompletas.")
        raise ass_err


def test_fill_num_na(train_set):
    '''
    Probar si la fill_num_na() rellena  los NAs
    de variables numericas.
    '''
    try:
        num_train_filled = cln.fill_num_na(train_set)
        num_vars_after_fill = num_train_filled.select_dtypes(include=[np.float64, np.int64])
        assert num_vars_after_fill.isna().sum().sum()==0
    except AssertionError as ass_err:
        logging.error("No se han rellenado todos los NA de las variables "
                      "tipo float o int")
        raise ass_err
