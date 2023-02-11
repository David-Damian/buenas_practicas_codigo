""""
Este script le permite al usuario, crear los objetos necesarios
para el EDA.
Las figuras son almacendas en el directorio figures
del directorio padre.
"""
import logging
from matplotlib import pyplot as plt
import seaborn as sns
import yaml
from src import load_clean as cln


def eda(path_train, fig_path):
    """
    Función para hacer un mini EDA.
    Obtiene una grafica tipo heatmap de variables nulas y
    un violinplot de algunas variables.
    """
    # Cargar conjunto de entrenamiento
    train_data = cln.cargar_datos(path_train)

    # Heat Map
    figura, ejes = plt.subplots(figsize=(25, 10))
    heat_map = sns.heatmap(data=train_data.isnull(),
                           yticklabels=False, ax=ejes)
    figure1 = heat_map.get_figure()    # guarrdamos la grafica en una variable

    # Graficas de violin por tipo de casa
    figura, ejes = plt.subplots(figsize=(25, 10))
    violin = sns.countplot(x=train_data['SaleCondition'])
    violin = sns.histplot(x=train_data['SaleType'],
                          kde=True,
                          ax=ejes)
    violin = sns.violinplot(x=train_data['HouseStyle'],
                            y=train_data['SalePrice'],
                            ax=ejes)
    violin = sns.scatterplot(x=train_data["Foundation"],
                             y=train_data["SalePrice"],
                             palette='deep',
                             ax=ejes)
    figure2 = violin.get_figure()       # guardar la grafica en una variable

    # Almacenar las graficas.
    # Verificar que existe el path donde se almacenaran
    try:
        nombre_figuras = ["heat_map", "violin_plot"]

        # Guardar Heatmap
        save_heatmap = f"{fig_path}{nombre_figuras[0]}"
        figure1.savefig(save_heatmap, dpi=400)

        # Guardar violin plots
        save_violinplot = f"{fig_path}{nombre_figuras[1]}"
        figure2.savefig(save_violinplot, dpi=400)
    except FileNotFoundError as file_err:
        logging.error(f"Los datos de entrenamiento no estan en {fig_path}")
        raise file_err

        

