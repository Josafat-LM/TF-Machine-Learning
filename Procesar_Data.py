import pandas as pd
from datetime import datetime


# Cargar datasets
criptomonedas_df = pd.read_csv("criptomonedas_con_blockchain_actualizado.csv", encoding='unicode_escape')
#tokens_df = pd.read_csv("blockchain_tokens_data.csv", encoding='unicode_escape')
tokens_df = pd.read_csv("blockchain_tokens_data_parte2.csv", encoding='unicode_escape')

# Filtrar criptos presentes en ambos datasets
merged_df = pd.merge(tokens_df, criptomonedas_df, left_on=['token_symbol', 'token_name'], right_on=['symbol', 'name'])


filtered_df = merged_df[['capture_date', 'blockchain', 'symbol', 'name', 'price_usd', 'ranking']]
filtered_df.columns = ['Fecha de la captura', 'Nombre Blockchain', 'Token', 'Nombre', 'Precio (en US$)', 'Ranking']

category_to_class = {
    'ai-big-data': 0,
    'gaming': 1,
    'real-world-assets': 2,
    'memes': 3
}
filtered_df['Clase'] = merged_df['category'].map(category_to_class)

# Guardar
filtered_df.to_csv("nuevo_dataset.csv", index=False)
