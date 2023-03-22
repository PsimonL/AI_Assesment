import requests

# https://developer.airly.org/pl/docs#general.coordinates

API_KEY = 'TU_WPROWADZ_SWOJ_KLUCZ_API'
ENDPOINT_URL = 'https://airapi.airly.eu/v2/measurements'

# Współrzędne geograficzne miejsca, dla którego chcesz pobrać dane.
lat = 52.23
lng = 21.01

# Parametry zapytania.
params = {
    'indexType': 'AIRLY_CAQI',
    'lat': lat,
    'lng': lng
}

# Nagłówki zapytania zawierające klucz API.
headers = {
    'Accept': 'application/json',
    'apikey': API_KEY
}

# Wysłanie zapytania.
response = requests.get(ENDPOINT_URL, params=params, headers=headers)
data = response.json()
print(data)