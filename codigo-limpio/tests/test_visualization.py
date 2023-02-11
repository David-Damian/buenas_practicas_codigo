"""
Script para testear las funciones de limpieza de datos
que estan en src/visualization
"""
import os
import logging
import yaml
import pytest
from src import visualization as vs


@pytest.fixture(scope="module", name='train_path')
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

def test_eda(train_path):
    try:
        with open("../config.yaml", encoding="utf-8") as file:
            config = yaml.safe_load(file)
        path = config['test']['FIGURES_PATH']
        # Generar graficas
        vs.eda(train_path, path)
        # Verificar que se guardaron
        assert len(os.listdir(path)) == 3
    except AssertionError as ass_err:
        logging.error("No se han guardado las gráficas.")
        raise ass_err
