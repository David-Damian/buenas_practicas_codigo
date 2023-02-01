"""Limpieza, preprocesamiento y prediccion de precio de casas.

El presente script le permitirá al usuario, de manera parsimoniosa,
seguir la cadena de pasos: Limpieza -> preprocesamiento
                           -> realizar predicciones.
es decir, un pipeline para predecir.


"""
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
import yaml
import pandas as pd
from src import load_clean as cln
from src import preprocessing as prc
from src import visualization as vs

VARS_TO_DROP = ['Id', 'Alley', 'PoolQC', 'MiscFeature', 'Fence', 'MoSold',
                'YrSold', 'MSSubClass', 'GarageType', 'GarageArea',
                'GarageFinish', 'YearRemodAdd', 'LandSlope', 'BsmtUnfSF',
                'BsmtExposure', '2ndFlrSF', 'LowQualFinSF', 'Condition1',
                'Condition2', 'Heating', 'Exterior1st', 'Exterior2nd',
                'HouseStyle', 'LotShape', 'LandContour', 'Functional',
                'BsmtFinSF1', 'BsmtFinSF2', 'FireplaceQu', 'WoodDeckSF',
                'GarageQual', 'GarageCond', 'OverallCond', 'GarageYrBlt',
                'HeatingQC', 'LotConfig'
                ]
VARS_INCOMPLETAS = ['BsmtQual', 'BsmtCond', 'BsmtFinType1',
                    'BsmtFinType1', 'BsmtFinType2']
LABEL_ENCODING = ['Street', 'BldgType', 'SaleType', 'CentralAir']


# Obtener ruta donde se alamcenaran los datos

# Abrir yaml
with open("./config.yaml", encoding="utf-8") as file:
    config = yaml.safe_load(file)

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
    train_set, test_set = cln.cargar_datos()[0], cln.cargar_datos()[1]

    # Deshacerse de variables que no se incluiran en el modelo
    train_set.drop(VARS_TO_DROP, axis=1, inplace=True)
    test_set.drop(VARS_TO_DROP, axis=1, inplace=True)

    # Limpieza

    # Rellenar valores faltantes de variables categoricas
    train_filled = cln.fill_categorical_na(data=train_set,
                                           vars_incompletas=VARS_INCOMPLETAS,
                                           valor_nuevo="No")
    test_filled = cln.fill_categorical_na(data=test_set,
                                          vars_incompletas=VARS_INCOMPLETAS,
                                          valor_nuevo="No")

    # Rellenar valores faltantes de variables numericas
    train_clean = cln.fill_num_na(data=train_filled)
    test_clean = cln.fill_num_na(data=test_filled)

    # Guardar datos
    train_clean.to_csv(f"{paths_to_save[0][0]}train", index=False)
    test_clean.to_csv(f"{paths_to_save[0][1]}test", index=False)

    # Preprocesamiento
    # Tranformar los datos limpios.
    train_proc = train_clean
    test_proc = test_clean

    # Codificacion de variables ordinales

    # Para variables ordinales con categorias en comun
    train_proc = prc.ordinal_encoding(train_proc)
    test_proc = prc.ordinal_encoding(test_proc)

    # Para variables categoricas
    train_proc = prc.codificar_categoricas(train_proc, LABEL_ENCODING)
    test_proc = prc.codificar_categoricas(test_proc, LABEL_ENCODING)

    # Guardar datos de entrenamiento y prueba procesados

    # Guardar datos

    train_proc.to_csv(f"{paths_to_save[1]}train", index=False)
    test_proc.to_csv(f"{paths_to_save[2]}test", index=False)

    # Ajustar modelo

    target_var = train_proc['SalePrice']
    features = train_proc.drop(['SalePrice'], axis=1)

    # Crear objeto RandomForestRegressor
    modelo_candidato = RandomForestRegressor(max_leaf_nodes=250)

    # Ajustar modelo
    modelo_candidato.fit(features, target_var)
    score = cross_val_score(modelo_candidato, features, target_var, cv=10)

    # Imprime mensaje exitoso y error.
    print("Ajuste exitoso\nHaz ajustado un Random Forest\n\n")
    print(f"El modelo candidato tiene, en cada fold, un error de {score}\n")

    # Generar predicciones
    price = modelo_candidato.predict(test_proc)
    submission = pd.DataFrame({"SalePrice": price})

    # Guardar predicciones en formato csv
    submission.to_csv(f"{config['data']['PREDICCIONES']}predicciones",
                      index=False)


if __name__ == "__main__":
    # Ejecutar script del EDA
    vs.eda()

    # Ejecutar pipeline de prediccion
    pipeline_prediccion(paths_to_save=[clean_path,
                                       train_proc_path, test_proc_path])
