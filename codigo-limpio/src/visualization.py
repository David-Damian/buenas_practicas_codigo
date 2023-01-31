""""
Este script le permite al usuario, crear los objetos necesarios
para el EDA.
Las figuras son alamcendas en el directorio figures
del directorio padre.
"""
from matplotlib import pyplot as plt
from seaborn import heatmap, countplot,violinplot,scatterplot
from load_clean import cargar_datos
import seaborn as sns
import yaml


# Cargar conjunto de entrenamiento
train_data = cargar_datos()[0]

#

# Heat Map
fig, ax = plt.subplots(figsize=(25,10))
heat_map = sns.heatmap(data=train_data.isnull(), yticklabels=False, ax=ax)
figure1 = heat_map.get_figure()         #guarrdamos la grafica en una variable

# Graficas de violin por tipo de casa
fig, ax = plt.subplots(figsize=(25,10))
violin = sns.countplot(x=train_data['SaleCondition'])
violin = sns.histplot(x=train_data['SaleType'], kde=True, ax=ax)
violin = sns.violinplot(x=train_data['HouseStyle'], y=train_data['SalePrice'],ax=ax)
violin = sns.scatterplot(x=train_data["Foundation"], y=train_data["SalePrice"], palette='deep', ax=ax)
figure2 = violin.get_figure()           #guarrdamos la grafica en una variable

# Almacenar las graficas.

# Abrir yaml
with open("../config.yaml", "r") as file:
    config = yaml.safe_load(file)

FIGURES_PATH=config['visualization']['FIGURES_PATH']        #obtener ruta donde se alamcenaran las graficas

nombre_figuras=["heat_map", "violin_plot"]                  #nombre de cada imagen

#Guardar Heatmap
save_heatmap='{}{}'.format(FIGURES_PATH, nombre_figuras[0])
figure1.savefig(save_heatmap, dpi=400)

#Guardar violin plots
save_violinplot='{}{}'.format(FIGURES_PATH, nombre_figuras[1])
figure2.savefig(save_violinplot, dpi=400)
