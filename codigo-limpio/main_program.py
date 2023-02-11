"""Limpieza, preprocesamiento y prediccion de precio de casas.

El presente script le permitirá al usuario, de manera parsimoniosa,
seguir la cadena de pasos: Limpieza -> preprocesamiento
                           -> realizar predicciones.
es decir, un pipeline para predecir.


"""
import logging
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
import yaml
import pandas as pd
from src import load_clean as cln
from src import preprocessing as prc
from src import visualization as vs

# Abrir yaml
with open("./config.yaml", encoding="utf-8") as file:
    config = yaml.safe_load(file)

VARS_TO_DROP = config['main']['VARS_TO_DROP']
VARS_INCOMPLETAS = config['main']['VARS_INCOMPLETAS']
LABEL_ENCODING = config['main']['LABEL_ENCODING']


# Obtener ruta donde se alamcenaran los datos
# Almacenar rutas para guardar datos limpios y procesados
clean_path = [config['data']['TRAIN_CLEAN'], config['data']['TEST_CLEAN']]
train_proc_path = config['data']['TRAIN_PROCESSED']
test_proc_path = config['data']['TEST_PROCESSED']
test_proc_path = config['data']['TEST_PROCESSED']


# Pipeline de inferencia

def pipeline_prediccion(paths_to_save):
    """
    Este es un pipiline de inderencia/prediccion para el problema de
    house-pricing.

    Args:
    -----
    paths_to_save (List): Rutas donde se almacenarán artefactos del modelo en
                          el orden siguiente:
                          [train_limpios, test_limpios,
                           train_procesados, test_procesados]
    Return:
    -------

    """
    # Cargar conjunto de entrenamiento y prueba
    train_set = cln.cargar_datos(config['data']['TRAIN_PATH']), 
    test_set = cln.cargar_datos(config['data']['TEST_PATH'])

    # Deshacerse de variables que no se incluiran en el modelo
    try:
        #  Mensaje de inicializacion de proceso de droppear
        logging.info("Algunas columnas del conjunto de "
                     "train y test desaparecerán...")
        train_set.drop(VARS_TO_DROP, axis=1, inplace=True)
        test_set.drop(VARS_TO_DROP, axis=1, inplace=True)
        logging.info("Tarea concluida con ÉXITO.")
    except KeyError:
        # Mandar mensaje tipo ERROR al results.log
        logging.error("Verifica que las variables por droppear,sean"
                      " columnas en el conjunto de train y test")

    # Limpieza
    # Rellenar valores faltantes de variables categoricas
    try:
        logging.info("Se comenzarán a imputar los "
                     "valores de variables categoricas...")
        train_filled = cln.fill_categorical_na(data=train_set,
                                               vars_incompletas=VARS_INCOMPLETAS,
                                               valor_nuevo="No")

        test_filled = cln.fill_categorical_na(data=test_set,
                                              vars_incompletas=VARS_INCOMPLETAS,
                                              valor_nuevo="No")
        logging.info("Tarea concluida con ÉXITO.")
    # Si no se llenaron fue porque VARS_INCOMPLETAS tiene
    # un nombre que no aparece en las columnas de los sets.
    except KeyError:
        logging.error("No se han podido rellenar variables categoricas."
                      "Verificar que las variables incompletas sean "
                      "columnas del conjunto de "
                      "entrenamiento y test")

    # Rellenar valores faltantes de variables numericas
    try:
        train_clean = cln.fill_num_na(data=train_filled)
        test_clean = cln.fill_num_na(data=test_filled)
    # Parar. Error debido a que el try anterior no se ejecutó.
    except UnboundLocalError:
        logging.error("No se ha podido rellenar los valores de vars"
                      "numericas porque las categoricas no se rellenaron.")
    # Guardar datos
    train_clean.to_csv(f"{paths_to_save[0][0]}train", index=False)
    test_clean.to_csv(f"{paths_to_save[0][1]}test", index=False)

    # Preprocesamiento
    # Tranformar los datos limpios.
    train_proc = train_clean
    test_proc = test_clean

    # Codificacion de variables ordinales

    # Para variables ordinales con categorias en comun
    logging.info("Se aplicará un ordinal.encoding para variables ordinales")
    train_proc = prc.ordinal_encoding(train_proc)
    test_proc = prc.ordinal_encoding(test_proc)
    logging.info("Tarea conclcuida con ÉXITO.")

    # Para variables categoricas
    logging.info("Se aplicará un label.encoding para variables categóricas")
    train_proc = prc.codificar_categoricas(train_proc, LABEL_ENCODING)
    test_proc = prc.codificar_categoricas(test_proc, LABEL_ENCODING)
    logging.info("Tarea conclcuida con ÉXITO.")

    # Guardar datos de entrenamiento y prueba procesados
    logging.info("Guardando datos de train y test procesados...")
    train_proc.to_csv(f"{paths_to_save[1]}train", index=False) # Guardar datos de train
    test_proc.to_csv(f"{paths_to_save[2]}test", index=False) # Guardar datos de test
    logging.info("Tarea conclcuida con ÉXITO.")

    # Ajustar modelo
    logging.info("Ajustando un modelo Random Forest...")
    target_var = train_proc['SalePrice']
    features = train_proc.drop(['SalePrice'], axis=1)

    # Crear objeto RandomForestRegressor
    modelo_candidato = RandomForestRegressor(max_leaf_nodes=250)
    logging.info(f"Los hiperparámetros del modelo que esta ajustando "
    f"son {modelo_candidato.get_params()}")
    # Ajustar modelo
    modelo_candidato.fit(features, target_var)
    score = cross_val_score(modelo_candidato, features, target_var, cv=10)

    # Imprime mensaje exitoso y error.
    logging.info("Ajuste exitoso\n\n")
    logging.info(f"El modelo candidato tiene, en cada fold, un error de {score}\n")

    # Generar predicciones
    logging.info("Generando predicciones...")
    price = modelo_candidato.predict(test_proc)
    submission = pd.DataFrame({"SalePrice": price})

    # Guardar predicciones en formato csv
    submission.to_csv(f"{config['data']['PREDICCIONES']}predicciones",
                      index=False)
    logging.info(f"Listo! Hemos guardado las predicciones en {config['data']['PREDICCIONES']}")


if __name__ == "__main__":

    # Inicializar logger
    logging.basicConfig(filename='./logs/results.log',
                        level=logging.INFO,
                        filemode='w',
                        format='%(filename)s - %(name)s - %(levelname)s - %(message)s')

    # Verificar que hay datos de train y test en el directorio data/raw/
    # y que no esten vacíos. En ese caso, ejecutar el EDA.
    try:
        logging.info("Verificando que hay datos de train y test en data/raw...")

        # Abrir yaml para obtener ruta de los datos.
        with open("./config.yaml", encoding="utf-8") as file:
            config = yaml.safe_load(file)
        train = pd.read_csv(config['data']['TRAIN_PATH'])
        test = pd.read_csv(config['data']['TEST_PATH'])
        logging.info("Operacion EXITOSA\n")

        # Verificar que los datos no son archivos vacíos
        if not (train.empty and test.empty):
            logging.info("Los datos de train y test no estan vacíos.")
            # Ejecutar script del EDA
            try:
                logging.info("Construcción de gráficas para EDA comenzadas...")
                vs.eda()
                logging.info("Gráficas terminadas con ÉXITO.")
                # Verificar que cuando se ejecuta va.eda no haya error del tipo:
                raise FileNotFoundError
            # Si falla, pare y mande msj de error
            except FileNotFoundError:
                logging.error("Las graficas no se almacenaron en figures/."
                              "Revise el archivo config.yaml y verifique "
                              "que la ruta para almacenarlas exista.")

    except FileNotFoundError:
        logging.error("No hay datos de entrenamiento o test"
                      " en este path: data/raw."
                      "Busca en otro lugar y colócalos en ese path,"
                      " por lo pronto no podemos proceder.")

    # Ejecutar pipeline de prediccion
    try:
        logging.info("Pipeline comenzado...")
        pipeline_prediccion(paths_to_save=[clean_path,
                                                train_proc_path, test_proc_path])
        logging.info("Tarea concluida con ÉXITO.")
    except:
        logging.error("EL pipeline no se terminó.")
