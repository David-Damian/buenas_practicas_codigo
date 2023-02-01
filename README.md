# Tranformando código sucio a código limpio
Parte importante del trabajo de un *data scientist* es desarrollar código para la solución de diversos problemas de manera automática.
En este repositorio se presenta la transformación de un *código sucio* a *código limpio* siguiendo algunos pasos detallados [aquí](https://radiant-biscotti-3f9910.netlify.app/04-codigo_limpio.html#escribir-documentaci%C3%B3n).

Se puede verificar que todos los scripts con el formato `.py` cumplen con la convención de [PEP8](https://peps.python.org/pep-0008/#block-comments) mediante el uso de [flake8](https://flake8.pycqa.org/en/latest/).

## Objetivo
Como primer ejercicio y aplicación de los consejos sugeridos, se busca realizar el **mismo** proceso descrito en `./codigo-sucio/house_prices.ipynb` mediante la modularización de algunas funciones, inclusión de *loops* y otras estrategias de modo que el nuevo codigo sea más **legible, sencillo** y **conciso**.

## Estructura del repositorio
├── LICENSE
├── README.md          <- Descripción del proyecto.
├── codigo_limpio
|   ├── data
│       ├── clean             <- Carpeta para almacenar datos limpios.
│       ├── predicciones      <- Carpeta para almacenar predicciones.
│       ├── processed         <- Datos procesados para ingestar al modelo de ML.
│       └── raw               <- Datos en bruto, sin procesar.
|   ├── src                   <- Source code for use in this project.
│       ├── __init__.py       <- Makes src a Python module
│       ├── load_clean.py     <- Scripts to download or generate data
│       ├── preprocessing.py  <- Script de preprocesamiento de datos.
|       ├── visualization.py  <- Script para generare graficas del EDA.
|       └── ordinal_dict.json <- Script para generare graficas del EDA.
|   ├── figures               <- Almacenar graficas del EDA.
│   ├── notebooks             <- Jupyter notebooks.
│   ├── config.yaml
|   ├──main_program.py        <- Make this project python3 main_program.py
│
├── codigo-sucio

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


