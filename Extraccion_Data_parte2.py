import requests
import csv
import time
from datetime import datetime, timedelta
api_key = 'd4970e9f-a541-4fd0-8dbf-926c730fec28'

# Encabezados para la API
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key
}

# URL para la lista de criptomonedas
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Fecha de inicio y fin
start_date = datetime(2023, 10, 1)
end_date = datetime(2024, 5, 1)

# Crear archivo CSV
with open('blockchain_tokens_data.csv', mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['capture_date', 'blockchain_name', 'token_symbol', 'token_name', 'price_usd', 'ranking']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    # capturar datos diariamente
    current_date = start_date
    while current_date <= end_date:
        capture_date = current_date.strftime('%d/%m/%Y')

        # Parámetros para la solicitud
        params = {
            'start': '1',
            'limit': '5000',  
            'convert': 'USD'
        }

        # Realizar la solicitud GET
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json().get('data', [])

            # Iterar y guardar datos
            for token in data:
                blockchain_name = ', '.join(token.get('tags', ['Desconocida']))
                token_symbol = token.get('symbol', 'N/A')
                token_name = token.get('name', 'N/A')
                price_usd = token['quote']['USD'].get('price', 'N/A')
                ranking = token.get('cmc_rank', 'N/A')

                writer.writerow({
                    'capture_date': capture_date,
                    'blockchain_name': blockchain_name,
                    'token_symbol': token_symbol,
                    'token_name': token_name,
                    'price_usd': price_usd,
                    'ranking': ranking
                })

            print(f"Datos capturados para la fecha: {capture_date}")

        else:
            print(f"Error en la solicitud para la fecha {capture_date}: {response.status_code} - {response.text}")

        # Incrementar el día
        current_date += timedelta(days=1)
        time.sleep(1)


#PARA LAS FECHAS FALTANTES===============================================================================

api_key = 'd4970e9f-a541-4fd0-8dbf-926c730fec28'

# Encabezados para la API
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key
}

# URL para la lista de criptomonedas
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Lista de fechas específicas a capturar en formato dd/mm/yyyy
fechas_especificas = [
    "21/11/2023", "22/11/2023", "23/12/2023", "24/12/2023", "25/12/2023",
    "26/12/2023", "27/12/2023", "28/12/2023", "29/12/2023", "30/12/2023",
    "31/12/2023", "01/01/2024", "02/01/2024", "03/01/2024", "03/03/2024",
    "04/03/2024", "05/03/2024", "06/03/2024", "07/03/2024", "08/03/2024",
    "09/03/2024", "10/03/2024", "10/04/2024", "11/04/2024", "12/04/2024",
    "13/04/2024", "14/04/2024", "15/04/2024"
]

# Crear un archivo CSV para guardar los datos de las fechas faltantes
with open('blockchain_tokens_data_actualizado2.csv', mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['capture_date', 'blockchain_name', 'token_symbol', 'token_name', 'price_usd', 'ranking']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    # Iterar sobre las fechas específicas
    for capture_date in fechas_especificas:
        # Formatear la fecha al objeto datetime
        current_date = datetime.strptime(capture_date, '%d/%m/%Y')

        # Parámetros para la solicitud
        params = {
            'start': '1',
            'limit': '5000',
            'convert': 'USD'
        }

        # Realizar la solicitud GET
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json().get('data', [])

            # Iterar y guardar
            for token in data:
                blockchain_name = ', '.join(token.get('tags', ['Desconocida']))
                token_symbol = token.get('symbol', 'N/A')
                token_name = token.get('name', 'N/A')
                price_usd = token['quote']['USD'].get('price', 'N/A')
                ranking = token.get('cmc_rank', 'N/A')

                writer.writerow({
                    'capture_date': capture_date,
                    'blockchain_name': blockchain_name,
                    'token_symbol': token_symbol,
                    'token_name': token_name,
                    'price_usd': price_usd,
                    'ranking': ranking
                })

            print(f"Datos capturados para la fecha: {capture_date}")

        else:
            print(f"Error en la solicitud para la fecha {capture_date}: {response.status_code} - {response.text}")
        time.sleep(1)

