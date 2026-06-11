import requests
import pandas as pd
from datetime import date, datetime

today = date.today().isoformat()

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

params = {
    "format": "geojson",
    "starttime": "2020-01-01",
    "endtime": today,
    "minmagnitude": 3.0,
    "minlatitude": 24.5,
    "maxlatitude": 49.5,
    "minlongitude": -125.0,
    "maxlongitude": -66.5
}

response = requests.get(url, params=params)
data = response.json()

print(f"Total earthquakes fetched: {data['metadata']['count']}")

earthquakes = data['features']



rows = []
for eq in earthquakes:
    props = eq['properties']
    coords = eq['geometry']['coordinates']
    
    rows.append({
        'magnitude': props['mag'],
        'place': props['place'],
        'date': props['time'],
        'longitude': coords[0],
        'latitude': coords[1],
        'depth': coords[2]
    })

df = pd.DataFrame(rows)
df['date'] = pd.to_datetime(df['date'], unit='ms')
df.dropna(subset=['magnitude'], inplace=True)
df.to_csv("eq_data.csv",index=False)

print(df.head())
print(f"Date range: {df['date'].min()} to {df['date'].max()}")
print(f"Magnitude range: {df['magnitude'].min()} to {df['magnitude'].max()}")
print(f"Rows after cleaning: {len(df)}")