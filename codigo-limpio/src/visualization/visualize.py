""""
This script allows to user, create the objects necessary for
an EDA. 
Pictures are stored in the directory figures
"""

# Heat Map
fig, ax = plt.subplots(figsize=(25,10))
heat_map=sns.heatmap(data=train_data.isnull(), yticklabels=False, ax=ax)
figure = heat_map.get_figure()    
figure.savefig('figures/heatmap.png', dpi=400)

# Violin graph of Sales Pirce by HOse Style
fig, ax = plt.subplots(figsize=(25,10))
sns.countplot(x=train_data['SaleCondition'])
sns.histplot(x=train_data['SaleType'], kde=True, ax=ax)
sns.violinplot(x=train_data['HouseStyle'], y=train_data['SalePrice'],ax=ax)
sns.scatterplot(x=train_data["Foundation"], y=train_data["SalePrice"], palette='deep', ax=ax)