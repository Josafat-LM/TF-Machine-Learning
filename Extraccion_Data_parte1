import pandas as pd
import requests
import time

csv_file = 'criptomonedas_filtradas.csv'
df = pd.read_csv(csv_file)

# Clave de API
API_KEY = 'd4970e9f-a541-4fd0-8dbf-926c730fec28'

#API de CoinMarketCap
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'

#API Key
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

def obtener_blockchain(symbol):
    parameters = {
        'symbol': symbol
    }
    try:
        response = requests.get(url, headers=headers, params=parameters)
        data = response.json()

        # Extraer la información de blockchain
        if 'data' in data and symbol in data['data']:
            blockchain_platform = data['data'][symbol]['platform']
            if blockchain_platform:
                return blockchain_platform['name']
            else:
                return 'No asociado a ningún blockchain'
        else:
            return 'Informacion no disponible'
    except Exception as e:
        return f'Error: {e}'

def obtener_blockchain_R(symbol):
    resultado = obtener_blockchain(symbol)
    time.sleep(1)
    return resultado
df['blockchain'] = df['symbol'].apply(lambda x: obtener_blockchain_R(x))

# Guardar
df.to_csv('criptomonedas_con_blockchain_actualizado.csv', index=False)


#EXTRAER LOS DATOS FALTANTES=========================================================
csv_file = 'criptomonedas_con_blockchain_actualizado.csv'
df = pd.read_csv(csv_file)

# Clave de API
API_KEY = 'd4970e9f-a541-4fd0-8dbf-926c730fec28'

#API de CoinMarketCap
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'

#  API Key
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

def obtener_blockchain(symbol):
    parameters = {
        'symbol': symbol
    }
    try:
        response = requests.get(url, headers=headers, params=parameters)
        data = response.json()

        # Extraer la información de blockchain
        if 'data' in data and symbol in data['data']:
            blockchain_platform = data['data'][symbol]['platform']
            if blockchain_platform:
                return blockchain_platform['name']
            else:
                return 'No asociado a ningún blockchain'
        else:
            return 'Información no disponible'
    except Exception as e:
        return f'Error: {e}'


rangos_indices = [
    list(range(57, 59)), list(range(110, 112)), list(range(213, 215)),
    list(range(262, 264)), list(range(314, 316)), list(range(359, 361)),
    list(range(375, 377)), list(range(407, 428)), list(range(458, 479)),
    list(range(509, 531)), list(range(599, 624)), list(range(653, 670)),
    list(range(692, 721)), list(range(750, 767)), list(range(797, 818)),
    list(range(848, 868)), list(range(898, 916))
]
indices_a_actualizar = [indice for rango in rangos_indices for indice in rango]


for idx in indices_a_actualizar:
    if df.loc[idx, 'blockchain'] == 'Información no disponible':
        symbol = df.loc[idx, 'symbol']
        nuevo_valor = obtener_blockchain(symbol)
        df.at[idx, 'blockchain'] = nuevo_valor
        print(f"Actualizado blockchain para índice {idx} ({symbol}): {nuevo_valor}")
        time.sleep(2)

# Guardar
df.to_csv('criptomonedas_con_blockchain_actualizado2.csv', index=False)

