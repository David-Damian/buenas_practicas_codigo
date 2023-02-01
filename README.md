# Tranformando código sucio a código limpio
Parte importante del trabajo de un *data scientist* es desarrollar código para la solución de diversos problemas de manera automática.

En este repositorio se presenta la transformación de un *código sucio* a *código limpio* siguiendo algunos pasos detallados [aquí](https://radiant-biscotti-3f9910.netlify.app/04-codigo_limpio.html#escribir-documentaci%C3%B3n).

Los archivos en del *codigo-sucio* pretenden resolver el problema de [prediccion de precios de casas](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) de Kaggle.

## Objetivo
Como primer ejercicio y aplicación de los consejos sugeridos, se busca realizar el **mismo** proceso descrito en `./codigo-sucio/house_prices.ipynb` mediante la modularización de algunas funciones, inclusión de *loops* y otras estrategias de modo que el nuevo codigo sea más **legible, sencillo** y **conciso**.

Los nuevos archivos deben seguir la convención de [PEP8](https://peps.python.org/pep-0008/#block-comments) mediante el uso de [flake8](https://flake8.pycqa.org/en/latest/).

## Estructura del repositorio
Los directorios han sido marcados en negritas y

.<br />
├── LICENSE<br />
├── **README.md**          <- *Descripción del proyecto.* <br />
├── **codigo_limpio** <br />
│     └── **data** <br />
│          ....├─ clean             *Carpeta para almacenar datos limpios.* <br />
│          ....├─ predicciones      *Carpeta para almacenar predicciones.* <br />
│          ....├─ processed         *Datos procesados para ingestar al modelo de ML.* <br />
│          ....└─ raw               *Datos en bruto, sin procesar.* <br />
│      └── **src**                  *Source code for use in this project.* <br />
│         ....├── __init__.py       *Makes src a Python module.* <br />
│         ....├── load_clean.py     *Scripts to download or generate data.* <br />
│         ....├── preprocessing.py  *Script de preprocesamiento de datos.* <br />
│         ....├── visualization.py  *Script para generare graficas del EDA.* <br />
│         ....└── ordinal_dict.json *Script para generare graficas del EDA.* <br />
│   ├── **figures**                *Almacenar graficas del EDA.* <br />
│   ├── **notebooks**              *Jupyter notebooks.* <br />
│   ├── config.yaml *Archivo de configuracion para algunos scripts* <br />
│   ├──main_program.py         *Make this project python3 main_program.py* <br />
├── **codigo-sucio**            *Directorio con datos y jupyternotebook a corregir*
<br />

## Prerequisitos
* `Git`: Para clonar este repositorio
* `Python 3.6` y las librerías   `scikit-learn`, `pandas`, `yaml` y `json`.


## Ejecución
- Clona este repositorio
- En la línea de comandos, posicionate en la ruta donde esta almacenado este repositorio.
- Dirigete al directorio `codigo_limpio` ejecutando el comando `cd ./codigo_limpio/`.
- Ejecuta el el archivo `main_program.py` mediante el comando `python3 main_program.py`.

## Referencias
* [flake8](https://flake8.pycqa.org/en/latest/)
* [pylint](https://docs.pylint.org/)
* [Accesar a cada elemento de un diccionario en Pyhthon](https://stackoverflow.com/questions/12353288/getting-values-from-json-using-python)


