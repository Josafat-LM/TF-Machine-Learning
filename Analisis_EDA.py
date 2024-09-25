import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("nuevo_dataset.csv")

print(df.head())
print(df.info())

#datos faltantes
print("Datos faltantes por columna:\n", df.isnull().sum())

#Datos Estadísticos
print(df.describe())

# Calcular la matriz de correlación
correlation_matrix = dataset.corr(numeric_only=True)

# Graficar la matriz de correlación
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de Correlation')
plt.show()

# Gráfico: Cantidad de criptomonedas por blockchain
plt.figure(figsize=(12, 6))
blockchain_counts = dataset['Nombre Blockchain'].value_counts()
sns.barplot(x=blockchain_counts.index, y=blockchain_counts.values, palette='viridis')
plt.xticks(rotation=90)
plt.title('Cantidad de Criptomonedas por Blockchain')
plt.xlabel('Nombre Blockchain')
plt.ylabel('Cantidad de Criptomonedas')
plt.show()

# Gráfico: Blockchain por categoría
plt.figure(figsize=(14, 8))
blockchain_category = dataset.groupby(['Nombre Blockchain', 'Clase']).size().reset_index(name='counts')
blockchain_category_pivot = blockchain_category.pivot(index='Nombre Blockchain', columns='Clase', values='counts').fillna(0)
blockchain_category_pivot.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='tab20')
plt.title('Blockchain por Categoría')
plt.xlabel('Nombre Blockchain')
plt.ylabel('Cantidad de Criptomonedas')
plt.legend(title='Clase', labels=['IA', 'Gaming', 'RWA', 'Meme'])
plt.show()

# Gráfico de dispersión entre Precio y Ranking
plt.figure(figsize=(10, 6))
sns.scatterplot(data=dataset, x='Ranking', y='Precio (en US$)', hue='Clase', palette='viridis', alpha=0.6)
plt.title('Relación entre Ranking y Precio de las Criptomonedas')
plt.xlabel('Ranking')
plt.ylabel('Precio (en US$)')
plt.yscale('log')
plt.show()

# Boxplot de precios por categoría
plt.figure(figsize=(10, 6))
sns.boxplot(x='Clase', y='Precio (en US$)', data=dataset, palette='Set2')
plt.title('Distribución de Precios por Clase de Criptomonedas')
plt.xlabel('Clase (0: IA, 1: Gaming, 2: RWA, 3: Meme)')
plt.ylabel('Precio (en US$)')
plt.yscale('log')
plt.show()

# Gráfico de calor entre blockchain y clase
plt.figure(figsize=(12, 8))
heatmap_data = dataset.pivot_table(index='Nombre Blockchain', columns='Clase', aggfunc='size', fill_value=0)
sns.heatmap(heatmap_data, cmap='YlGnBu', linewidths=0.5, annot=True)
plt.title('Frecuencia de Blockchain por Categoría')
plt.xlabel('Clase (0: IA, 1: Gaming, 2: RWA, 3: Meme)')
plt.ylabel('Nombre Blockchain')
plt.show()


