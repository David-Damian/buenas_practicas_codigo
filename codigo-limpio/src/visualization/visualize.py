""""
This script allows to user, create the objects necessary for
an EDA. 
Pictures are stored in the directory called figures.
"""
from matplotlib import pyplot as plt
import seaborn as sns
from seaborn import heatmap, countplot,violinplot,scatterplot
import sys
from codigo_limpio.src import load_clean

#Path donde se almacenaran las graficas.
# Abrir yaml
with open("../../config.yaml", "r") as file:
    config = yaml.safe_load(file)
FIGURES_PATH=config['visualization']['FIGURES_PATH']

#Cargar conjunto de entrenamiento
train_data = cargar_datos()[0]

# Heat Map
fig, ax = plt.subplots(figsize=(25,10))
heat_map=sns.heatmap(data=train_data.isnull(), yticklabels=False, ax=ax)
figure = heat_map.get_figure()
nombre_figura="heat_map"
HEATHMAP_PATH='{} {}'.format(FIGURES_PATH, nombre_figura)
figure.savefig(HEATHMAP_PATH, dpi=400)
