import folium
import pandas as pd
import geopandas as gpd
from folium.plugins import MarkerCluster

faults=gpd.read_file("SHP/Qfaults_US_Database.shp")

m = folium.Map(location=[39.5, -98.35], zoom_start=4, tiles="CartoDB positron")
marker_cluster = MarkerCluster().add_to(m)

df = pd.read_csv("eq_data.csv")

faults = faults[['geometry']]
faults['geometry'] = faults['geometry'].simplify(0.5)
folium.GeoJson(faults, style_function=lambda x: {'color': 'gray', 'weight': 1, 'opacity': 0.5}).add_to(m)

for i, row in df.iterrows():
    if row['magnitude'] < 4:
        color = 'green'
    elif row['magnitude'] <5:
        color = 'yellow'
    elif row['magnitude'] <6:
        color = 'orange'
    else:
        color = 'red'
    folium.CircleMarker(
        fill=True,
        color=color,
        fill_color=color,
        fill_opacity=0.6,
        location = [row['latitude'], row['longitude']],
        popup=folium.Popup(f"Mag: {row['magnitude']} | {row['latitude']:.2f}, {row['longitude']:.2f} | Date: {row['date'][:10]}", max_width=300),
        radius=row['magnitude'] * 2.5,
        
    ).add_to(marker_cluster)

legend_html = '''
<div style="position: fixed; bottom: 30px; left: 30px; z-index: 1000; 
     background-color: white; padding: 10px; border-radius: 5px; 
     border: 1px solid gray; font-size: 14px;">
    <b>Earthquake Magnitude</b><br>
    <i style="background:green; width:12px; height:12px; display:inline-block;"></i> &lt; 4.0<br>
    <i style="background:yellow; width:12px; height:12px; display:inline-block;"></i> 4.0 – 5.0<br>
    <i style="background:orange; width:12px; height:12px; display:inline-block;"></i> 5.0 – 6.0<br>
    <i style="background:red; width:12px; height:12px; display:inline-block;"></i> 6.0+
</div>
'''
m.get_root().html.add_child(folium.Element(legend_html))

 
m.save("map.html")
print("Map saved as map.html")