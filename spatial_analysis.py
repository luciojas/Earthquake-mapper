import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

df = pd.read_csv("eq_data.csv")

geometry = [Point(lon, lat) for lon, lat in zip(df['longitude'], df['latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
# print(gdf.head())

fault_shp_path = "SHP/Qfaults_US_Database.shp"
fault_gdf = gpd.read_file(fault_shp_path)
# print(fault_gdf.head())

geometry_faults = gpd.sjoin_nearest(gdf.to_crs(3857), fault_gdf.to_crs(3857), distance_col="distance")
# print(geometry_faults.head())

save_path = "eq_faults.csv"
geometry_faults.to_csv(save_path, index=False)