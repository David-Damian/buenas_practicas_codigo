"""
Script para testear el pipeline de procesamiento y
generacion de predicciones
"""
import os
import logging
import pytest
import yaml
import main_program as pipeline

@pytest.fixture(scope="module", name= 'data_pth')
def path():
    '''
    Fixture - La función test_pipeline_prediccion() va a utilizar
    el retorno de esta funcion como un argumento.
    '''
    # Abrir yaml para obtener ruta de los datos.
    with open("./config.yaml", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    pth = [config['test']['TRAIN_PATH'], config['test']['TEST_PATH']]
    return pth

@pytest.fixture(scope="module", name='path_predictions')
def paths_to_save_():
    '''
    Fixture - La función test_pipeline_prediccion() va a utilizar
    el retorno de esta funcion como un argumento.
    '''
    # Abrir yaml para obtener ruta de los datos.
    with open("./config.yaml", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    clean_path = [config['test']['TRAIN_CLEAN'], 
                  config['test']['TEST_CLEAN']]
    train_proc_path = config['test']['TRAIN_PROCESSED']
    test_proc_path = config['test']['TEST_PROCESSED']
    predict_path = config['test']['PREDICTIONS_PATH']
    paths_to_save = [clean_path, train_proc_path,
                     test_proc_path, predict_path]
    return paths_to_save


def test_pipeline_prediccion(data_pth, path_predictions):
    '''
    Probar si el pipeline genera predicciones y las guarda
    en el lugar correcto.
    '''
    try:
        pipeline.pipeline_prediccion(data_pth, path_predictions)
        path_pipeline = path_predictions[3]
        path_datos = path_predictions[1]
        assert len(os.listdir(path_pipeline)) > 0
        assert len(os.listdir(path_datos)) == 4
    except AssertionError as ass_err:
        logging.error("No se han guardado las predicciones")