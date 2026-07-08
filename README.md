# Earthquake-mapper

This is an interactive earthquake mapper. You can customize the area and timeframe yourself, but is currently configured for all earthquakes during 2026 in the United States. 

# Data Sources

-USGS earthquake API
-USGS fault database

# What to expect

The map includes clustered markers (zoom in to see the individual markers) which are colored acording to their magnitude. Clicking on markers provides more information, such as, exact magnitude, coordnates, and date of occurance. 

# How to Run

1. Clone repository
2. Install dependencies: pip install -r requirements.txt
3. Run fetch_data.py to pull earthquake data
4. Run spatial_analysis.py to calculate fault distances
5. Run map.py to generate the map
6. Open map.html in your browser 

Note: Download the USGS Quaternary Fault Database GIS files from 
https://www.usgs.gov/programs/earthquake-hazards/faults 
and place the SHP folder in the project root before running.