import requests
import json
from datetime import datetime

# CONFIGURACIo: Canvia per la ciutat que vulguis
latitude = 41.61  # Manresa
longitude = 1.84
timezone = "auto"

# Data d'avui
avui = datetime.now().strftime("%Y-%m-%d")

# Peticio a Open-Meteo
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}&hourly=temperature_2m&timezone={timezone}&start_date={avui}&end_date={avui}"
)

response = requests.get(url)
dades = response.json()

# Llista de temperatures d’avui
temperatures = dades["hourly"]["temperature_2m"]

# Calculs
temp_max = max(temperatures)
temp_min = min(temperatures)
temp_mitjana = sum(temperatures) / len(temperatures)

# Resultat a guardar
resultat = {
    "data": avui,
    "localitzacio": "Manresa",
    "temperatura_maxima": temp_max,
    "temperatura_mínima": temp_min,
    "temperatura_mitjana": round(temp_mitjana, 2)
}

# Nom del fitxer .json amb data
nom_fitxer = f"temp_{datetime.now().strftime('%Y%m%d')}.json"

# Guardar arxiu
with open(nom_fitxer, "w") as f:
    json.dump(resultat, f, indent=4)

print(f"Fitxer {nom_fitxer} creat amb exit.")
